import requests

def make_request(method):
    url = 'https://jsonplaceholder.typicode.com/posts/1'
    response = requests.request(method, url)
    print(response.text)

make_request("GET")