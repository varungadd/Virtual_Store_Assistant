import pandas as pd
from flask import Flask, request, render_template
from sklearn.preprocessing import MinMaxScaler
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.neighbors import NearestNeighbors

app = Flask(__name__)

# Load and prepare the data
file_path_modified = 'customer_behavior_with_padded_search_queries.csv'
data_recommendation = pd.read_csv(file_path_modified)

# Normalize the purchase amounts
scaler = MinMaxScaler()
data_recommendation['purchase_amount_scaled'] = scaler.fit_transform(data_recommendation[['purchase_amount']])

# Combine features to create item profiles
data_recommendation['combined_features'] = data_recommendation['search_queries'] + ' ' + data_recommendation['review']

# Vectorize the combined text features
vectorizer = TfidfVectorizer(stop_words='english')
item_profiles = vectorizer.fit_transform(data_recommendation['combined_features'])
cosine_similarities = cosine_similarity(item_profiles, item_profiles)

# Create a user-item interaction matrix
user_item_matrix = data_recommendation.pivot_table(index='customer_id', columns='product_id', values='purchase_amount_scaled').fillna(0)

# Fit a NearestNeighbors model for collaborative filtering
user_based_model = NearestNeighbors(metric='cosine', algorithm='brute')
user_based_model.fit(user_item_matrix)

def get_cb_recommendations(item_id, top_n=5):
    idx = data_recommendation[data_recommendation['product_id'] == item_id].index[0]
    sim_scores = list(enumerate(cosine_similarities[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    top_indices = [i[0] for i in sim_scores[1:top_n+1]]
    top_product_ids = data_recommendation.iloc[top_indices]['product_id'].values
    return top_product_ids

def get_user_based_recommendations(user_id, top_n=5):
    user_index = user_item_matrix.index.get_loc(user_id)
    distances, indices = user_based_model.kneighbors(user_item_matrix.iloc[user_index, :].values.reshape(1, -1), n_neighbors=top_n+1)
    similar_users = indices.flatten()[1:]
    recommended_items = user_item_matrix.iloc[similar_users, :].mean(axis=0).sort_values(ascending=False).index.values
    return recommended_items[:top_n]

def get_hybrid_recommendations(user_id, top_n=5):
    user_based_recommendations = get_user_based_recommendations(user_id, top_n=top_n)
    if len(user_based_recommendations) > 0:
        cb_recommendations = get_cb_recommendations(user_based_recommendations[0], top_n=top_n)
    else:
        cb_recommendations = []

    combined_recommendations = list(user_based_recommendations) + list(cb_recommendations)
    recommendation_counts = pd.Series(combined_recommendations).value_counts()
    sorted_recommendations = recommendation_counts.index.values
    return sorted_recommendations[:top_n]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/recommendations', methods=['POST'])
def recommendations():
    customer_id = int(request.form['customer_id'])
    recommendations = get_hybrid_recommendations(customer_id, top_n=5)
    
    print(f"Customer ID: {customer_id}")  # Debugging
    print(f"Recommendations: {recommendations}")  # Debugging
    
    recommended_products_details = data_recommendation[data_recommendation['product_id'].isin(recommendations)][['product_id', 'search_queries', 'review']].drop_duplicates(subset=['product_id'])
    
    print(f"Recommended Products Details: {recommended_products_details}")  # Debugging

    return render_template('recommendations.html', recommendations=recommended_products_details.to_dict(orient='records'))

if __name__ == '__main__':
    app.run(debug=True)