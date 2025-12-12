# APIs requests
# * https://jsonplaceholder.typicode.com/todos/1

# ? Without dependencies
import urllib.request, json, urllib.error

api_todos1 = "https://jsonplaceholder.typicode.com/todos/1"

try:
    response = urllib.request.urlopen(api_todos1)
    data = response.read() # data in binary format, not decoded
    json_data = json.loads(data.decode('utf-8'))
    print(json_data) # {'userId': 1, 'id': 1, 'title': 'delectus aut autem', 'completed': False}
    response.close() #!!
except urllib.error.URLError as e:
    print(f"ERROR OF REQUEST: { e }")


# ? With dependencies (requests | pip, uv)
import requests

print("\nGET:")
response = requests.get(api_todos1)
print(response.json()) # {'userId': 1, 'id': 1, 'title': 'delectus aut autem', 'completed': False}

api_posts = "https://jsonplaceholder.typicode.com/posts/"
print("\nPOST:")
try:
    response = requests.post(api_posts, json={ "title": "david", "body": "dev", "userId": 15 })
    print(response.status_code) # 201 (created)     
except requests.exceptions.RequestException as e:
    print(f"ERROR OF REQUEST: { e }")
