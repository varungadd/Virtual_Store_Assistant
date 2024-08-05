from django.shortcuts import render
from store_assistant.models import Product
from store_assistant import templates

"""
def index(request):
    return render(request, 'store_assistant/index.html')
"""
import requests
import pandas as pd
from django.shortcuts import render
import logging
from django.core.cache import cache
import time


logger = logging.getLogger(__name__)

# Index view to load products and categories
def index(request):
    # Load product data from CSV
    #products_df = pd.read_csv(r'D:\CODER\Wallmart_Hackathon\virtual_store\products.csv')
    products_df = pd.read_csv(r'D:\CODER\Wallmart_Hackathon\virtual_store\products_1.csv')
    # Prepare categories and products for the template
    categories = products_df['category'].unique()
    products_by_category = []

    for category in categories:
        category_products = products_df[products_df['category'] == category]
        products_list = category_products.head(9).to_dict(orient='records')  # Convert to list of dictionaries
        for product in products_list:
            product['image_url'] = fetch_product_image(product['product_name'])
        products_by_category.append({
            'category': category,
            'products': products_list
        })

    context = {
        'products_by_category': products_by_category,
    }

    return render(request, 'store_assistant/index.html', context)

def fetch_product_image(product_name):
    image_url = fetch_from_pexels(product_name)
    if image_url:
        return image_url

    time.sleep(1)  # Introduce a delay to prevent hitting rate limits

    image_url = fetch_from_unsplash(product_name)
    if image_url:
        return image_url

    time.sleep(1)  # Introduce a delay to prevent hitting rate limits

    image_url = fetch_from_pixabay(product_name)
    return image_url
def fetch_from_pexels(product_name):
    API_KEY = 'YOUR_API_KEY'
    headers = {
        'Authorization': API_KEY
    }
    params = {
        'query': product_name,
        'per_page': 1
    }

    cache_key = f"product_image_pexels_{product_name}"
    cached_image_url = cache.get(cache_key)
    if cached_image_url:
        return cached_image_url

    response = requests.get('https://api.pexels.com/v1/search', headers=headers, params=params)
    if response.status_code == 200:
        data = response.json()
        if data['photos']:
            image_url = data['photos'][0]['src']['medium']
            cache.set(cache_key, image_url, timeout=86400)
            return image_url
    else:
        logger.error(f"Failed to fetch image for {product_name} from Pexels: {response.status_code} {response.text}")
    
    return None

def fetch_from_unsplash(product_name):
    ACCESS_KEY = 'YOUR_API_KEY'
    params = {
        'query': product_name,
        'per_page': 1,
        'client_id': ACCESS_KEY
    }

    cache_key = f"product_image_unsplash_{product_name}"
    cached_image_url = cache.get(cache_key)
    if cached_image_url:
        return cached_image_url

    response = requests.get('https://api.unsplash.com/search/photos', params=params)
    if response.status_code == 200:
        data = response.json()
        if data['results']:
            image_url = data['results'][0]['urls']['regular']
            cache.set(cache_key, image_url, timeout=86400)
            return image_url
    else:
        logger.error(f"Failed to fetch image for {product_name} from Unsplash: {response.status_code} {response.text}")
    
    return None

def fetch_from_pixabay(product_name):
    API_KEY = 'YOUR_API_KEY'
    params = {
        'q': product_name,
        'per_page': 1,
        'key': API_KEY
    }

    cache_key = f"product_image_pixabay_{product_name}"
    cached_image_url = cache.get(cache_key)
    if cached_image_url:
        return cached_image_url

    response = requests.get('https://pixabay.com/api/', params=params)
    if response.status_code == 200:
        data = response.json()
        if data['hits']:
            image_url = data['hits'][0]['webformatURL']
            cache.set(cache_key, image_url, timeout=86400)
            return image_url
    else:
        logger.error(f"Failed to fetch image for {product_name} from Pixabay: {response.status_code} {response.text}")
    
    return None

"""
from django.shortcuts import render
import pandas as pd
from store_assistant.models import Product, ProductDescription

from django.shortcuts import render
import pandas as pd

def index(request):
    # Load product data from CSV
    products_df = pd.read_csv(r'D:\CODER\Wallmart_Hackathon\virtual_store\products.csv')

    # Prepare categories and products for the template
    categories = products_df['category'].unique()
    products_by_category = []

    for category in categories:
        category_products = products_df[products_df['category'] == category]
        products_list = category_products.head(18).to_dict(orient='records')  # Convert to list of dictionaries
        products_by_category.append({
            'category': category,
            'products': products_list
        })

    context = {
        'products_by_category': products_by_category,
        'fetch_product_image': fetch_product_image,
    }

    return render(request, 'store_assistant/index.html', context)
"""


def product_location(request, product_id):
    """Render product location information."""
    try:
        product = Product.objects.get(product_id=product_id)
    except Product.DoesNotExist:
        product = None
    return render(request, 'store_assistant/product_location.html', {'product': product})

from django.shortcuts import render, get_object_or_404
from .models import Product
""" 
def category_products(request, category):
    products = Product.objects.filter(category=category)
    return render(request, 'store_assistant/category_products.html', {'products': products})

from django.shortcuts import render
from .models import Product

def category_products(request, category):
    products = Product.objects.filter(category=category)
    return render(request, 'store_assistant/category_products.html', {'category': category, 'products': products})

"""

def category_products(request, category):
    products_df = pd.read_csv(r'D:\CODER\Wallmart_Hackathon\virtual_store\products_1.csv')
    products = products_df[products_df['category'] == category].to_dict(orient='records')
    
    for product in products:
        product['image_url'] = fetch_product_image(product['product_name'])

    context = {
        'category': category,
        'products': products,
    }

    return render(request, 'store_assistant/category_products.html', context)



from django.shortcuts import render

def contact_us(request):
    return render(request, 'store_assistant/contact_us.html')

def login(request):
    return render(request, 'store_assistant/login.html')

# views.py

from django.shortcuts import render, get_object_or_404
from .models import Product, ProductDescription

import requests
from django.conf import settings

def fetch_images(product_name):
    images = []

    # Pexels API
    pexels_url = f'https://api.pexels.com/v1/search?query={product_name}&per_page=3'
    pexels_headers = {'Authorization': settings.PEXELS_API_KEY}
    pexels_response = requests.get(pexels_url, headers=pexels_headers)
    if pexels_response.status_code == 200:
        for photo in pexels_response.json().get('photos', []):
            images.append(photo['src']['medium'])

    # Unsplash API
    unsplash_url = f'https://api.unsplash.com/search/photos?query={product_name}&per_page=3'
    unsplash_headers = {'Authorization': f'Client-ID {settings.UNSPLASH_ACCESS_KEY}'}
    unsplash_response = requests.get(unsplash_url, headers=unsplash_headers)
    if unsplash_response.status_code == 200:
        for photo in unsplash_response.json().get('results', []):
            images.append(photo['urls']['regular'])

    # Pixabay API
    pixabay_url = f'https://pixabay.com/api/?key={settings.PIXABAY_API_KEY}&q={product_name}&per_page=3'
    pixabay_response = requests.get(pixabay_url)
    if pixabay_response.status_code == 200:
        for photo in pixabay_response.json().get('hits', []):
            images.append(photo['webformatURL'])

    return images

from django.shortcuts import render, get_object_or_404, redirect
from .models import Product, ProductDescription

def view_details(request, product_id):
    product = get_object_or_404(Product, product_id=product_id)
    description = get_object_or_404(ProductDescription, product_id=product_id)
    images = fetch_images(product.product_name)
    return render(request, 'store_assistant/view_details.html', {
        'product': product,
        'description': description,
        'images': images
    })

def add_to_cart(request, product_id):
    cart = request.session.get('cart', {})
    product = get_object_or_404(Product, product_id=product_id)
    images = fetch_images(product.product_name)

    if str(product_id) in cart:
        cart[str(product_id)]['quantity'] += 1
    else:
        cart[str(product_id)] = {
            'name': product.product_name,
            'price': float(product.price),  # Convert Decimal to float
            'quantity': 1,
            'image': images[0] if images else '',  # Use the first image if available
            'stock_availability': product.stock_availability  # Directly store stock_availability
        }

    request.session['cart'] = cart
    return redirect('view_cart')

def view_cart(request):
    cart = request.session.get('cart', {})
    total_amount = sum(float(item['price']) * item['quantity'] for item in cart.values())
    return render(request, 'store_assistant/cart.html', {'cart': cart, 'total_amount': total_amount})

def update_cart_quantity(request, product_id, action):
    cart = request.session.get('cart', {})
    product_id_str = str(product_id)

    if product_id_str in cart:
        if action == 'increase':
            cart[product_id_str]['quantity'] += 1
        elif action == 'decrease' and cart[product_id_str]['quantity'] > 1:
            cart[product_id_str]['quantity'] -= 1

        request.session['cart'] = cart

    return redirect('view_cart')

def remove_from_cart(request, product_id):
    cart = request.session.get('cart', {})
    product_id_str = str(product_id)

    if product_id_str in cart:
        del cart[product_id_str]
        request.session['cart'] = cart

    return redirect('view_cart')

from django.shortcuts import render
from .models import Product

def ar_view(request):
    products = Product.objects.all()
    return render(request, 'store_assistant/ar_template.html', {'products': products})

from django.shortcuts import render

def customer_id(request):
    return render(request, 'store_assistant/customer_id.html')


import requests
from django.conf import settings
import pandas as pd
from django.shortcuts import render, get_object_or_404
from sklearn.preprocessing import MinMaxScaler
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.neighbors import NearestNeighbors
from .models import Product, ProductDescription, CustomerBehavior

# Load and prepare the data
file_path_modified = r'D:\CODER\Wallmart_Hackathon\virtual_store\store_assistant\customer_behavior_with_padded_search_queries.csv'
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

def fetch_images_1(product_name):
    images = []

    # Pexels API
    pexels_url = f'https://api.pexels.com/v1/search?query={product_name}&per_page=3'
    pexels_headers = {'Authorization': settings.PEXELS_API_KEY}
    pexels_response = requests.get(pexels_url, headers=pexels_headers)
    if pexels_response.status_code == 200:
        for photo in pexels_response.json().get('photos', []):
            images.append(photo['src']['medium'])

    # Unsplash API
    unsplash_url = f'https://api.unsplash.com/search/photos?query={product_name}&per_page=3'
    unsplash_headers = {'Authorization': f'Client-ID {settings.UNSPLASH_ACCESS_KEY}'}
    unsplash_response = requests.get(unsplash_url, headers=unsplash_headers)
    if unsplash_response.status_code == 200:
        for photo in unsplash_response.json().get('results', []):
            images.append(photo['urls']['regular'])

    # Pixabay API
    pixabay_url = f'https://pixabay.com/api/?key={settings.PIXABAY_API_KEY}&q={product_name}&per_page=3'
    pixabay_response = requests.get(pixabay_url)
    if pixabay_response.status_code == 200:
        for photo in pixabay_response.json().get('hits', []):
            images.append(photo['webformatURL'])

    return images

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



def recommendations(request):
    if request.method == 'POST':
        customer_id = int(request.POST.get('customer_id'))
        recommended_product_ids = get_hybrid_recommendations(customer_id, top_n=5)
        
        recommended_products_details = Product.objects.filter(product_id__in=recommended_product_ids)
        
        product_images = {}
        for product in recommended_products_details:
            product.image_url = fetch_product_image(product.product_name)
        
        return render(request, 'store_assistant/recommendations.html', {
            'recommendations': recommended_products_details,
            'product_images': product_images
        })
    return render(request, 'store_assistant/customer_id.html')


from django.shortcuts import render

def payments(request):
    # You can retrieve the cart total from session or database as per your implementation
    cart = request.session.get('cart', {})
    cart_total = sum(float(item['price']) * item['quantity'] for item in cart.values())
    return render(request, 'store_assistant/payments.html', {'cart_total': cart_total})

def checkout(request):
    if request.method == 'POST':
        # Handle payment processing logic here
        # For now, we'll just simulate a successful payment
        return render(request, 'store_assistant/checkout_success.html')
    else:
        # Redirect to payment page if the request is not POST
        return redirect('payment_page')


def checkout_success(request):
    return render(request, 'store_assistant/checkout_success.html')

def categories(request):
    return render(request, 'store_assistant/categories.html')
