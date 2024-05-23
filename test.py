import requests

url = "https://api.kurobbs.com/gamer/role/default"

data = {
  "queryUserId": 1
}
response = requests.post(url, json=data)

print(response.status_code)
print(response.json())