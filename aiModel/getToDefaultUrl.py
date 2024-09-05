import requests

URL="http://localhost:10001/"

r=requests.get(url=URL)

data = r.text

print("The returned data is:", data)