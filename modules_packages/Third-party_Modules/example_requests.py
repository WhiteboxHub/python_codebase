import requests

# Send a GET request to a URL
response = requests.get("https://jsonplaceholder.typicode.com/posts")
print(response.status_code)  # Output: 200
print(response.json())  # Output: JSON data from the API
