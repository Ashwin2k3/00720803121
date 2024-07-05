import requests
import json

# Replace these with your actual details
registration_url = "http://20.244.56.144/test/register"
auth_url = "http://20.244.56.144/test/auth"
registration_details = {
    "companyName": "goMart",
    "ownerName": "Ashwin",
    "rollNo": "00720803121",
    "ownerEmail": "ashwin.2k3@gmail.com",
    "accessCode": "YkXfTB"  # Replace this with the actual access code
}

# Register the company
response = requests.post(registration_url, json=registration_details)
if response.status_code == 200:
    registration_response = response.json()
    print("Registration successful!")
    print("Save these credentials:")
    print(json.dumps(registration_response, indent=4))

    # Extract clientID and clientSecret
    client_id = registration_response['clientID']
    client_secret = registration_response['clientSecret']

    # Prepare authorization details
    auth_details = {
        "companyName": registration_details["companyName"],
        "clientID": client_id,
        "clientSecret": client_secret,
        "ownerName": registration_details["ownerName"],
        "ownerEmail": registration_details["ownerEmail"],
        "rollNo": registration_details["rollNo"]
    }

    # Obtain authorization token
    auth_response = requests.post(auth_url, json=auth_details)
    if auth_response.status_code == 200:
        auth_data = auth_response.json()
        print("Authorization successful!")
        print("Access Token:")
        print(json.dumps(auth_data, indent=4))
    else:
        print("Authorization failed!")
        print(f"Status Code: {auth_response.status_code}")
        print(auth_response.text)
else:
    print("Registration failed!")
    print(f"Status Code: {response.status_code}")
    print(response.text)
