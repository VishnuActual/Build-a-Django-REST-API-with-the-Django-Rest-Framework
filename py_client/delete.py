import requests 

product_id = int(input()) 
endpoint = f'http://localhost/5000/products/{product_id}/delete/'


get_response = requests.delete(endpoint) 

print(get_response.json())