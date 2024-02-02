import requests 

endpoint = 'http://localhost/5000/products/'

data = {
    "title":"This is the new title"
}

get_response = requests.post(endpoint, json = data)  

print(get_response.json())