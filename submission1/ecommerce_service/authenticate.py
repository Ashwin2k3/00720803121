import requests
import json

# Replace these with your actual details
auth_url = "http://20.244.56.144/test/auth"
auth_details = {
    "companyName": "goMart",
    "clientID": "cba0db24-aec7-4fcb-b74f-9782ffffbe23",
    "clientSecret": "RYrtxOGZWcMbFrwv",
    "ownerName": "Ashwin",
    "ownerEmail": "ashwin.2k3@gmail.com",
    "rollNo": "00720803121"
}

# Obtain authorization token
response = requests.post(auth_url, json=auth_details)
if response.status_code == 200:
    auth_data = response.json()
    print("Authorization successful!")
    print("Access Token:")
    print(json.dumps(auth_data, indent=4))
else:
    print("Authorization failed!")
    print(f"Status Code: {response.status_code}")
    print(response.text)
