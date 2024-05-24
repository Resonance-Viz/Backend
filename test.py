import requests

# Define the URL and payload
url = "https://api.kurobbs.com/gamer/role/default"
payload = {
    "queryUserId": 10009928
}

# Make the POST request
response = requests.post(url, json=payload)

# Check if the request was successful
if response.status_code == 200:
    print("Success!")
    # Print the response JSON
    print(response.json())
else:
    print(f"Failed with status code: {response.status_code}")
    print(response.text)
