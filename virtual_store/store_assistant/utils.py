import requests

API_KEY = 'lEK6qUcCxAZs0Qo4IdKjfQsc1vlwbxptLTt5PhqQHjFYx9V7uaWChNfW'
headers = {
    'Authorization': API_KEY
}
params = {
    'query': 'Apple Iphone 13',  # Replace with actual product name
    'per_page': 1
}
response = requests.get('https://api.pexels.com/v1/search', headers=headers, params=params)
print(response.json())
