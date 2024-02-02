import requests 

endpoint = 'http://localhost/5000/products/1/update/'

data = {
    'title': 'Hellow world my old friend',
    # 'content':'This is the new chnage'
    'price':129.11
}
get_response = requests.put(endpoint, json=data) 

print(get_response.json())