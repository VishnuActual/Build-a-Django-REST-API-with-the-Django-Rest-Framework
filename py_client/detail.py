import requests 

endpoint = 'http://localhost/5000/products/1/'

get_response = requests.get(endpoint) 

print(get_response.json())