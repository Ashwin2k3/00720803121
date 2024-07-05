import requests

# Replace with your API endpoint URL
url = 'http://127.0.0.1:8000/api/categories/laptop/products?top=5&minPrice=100&maxPrice=10000'

# Replace with your actual Bearer token
headers = {
    'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJNYXBDbGFpbXMiOnsiZXhwIjoxNzIwMTU4NDI5LCJpYXQiOjE3MjAxNTgxMjksImlzcyI6IkFmZm9yZG1lZCIsImp0aSI6ImNiYTBkYjI0LWFlYzctNGZjYi1iNzRmLTk3ODJmZmZmYmUyMyIsInN1YiI6ImFzaHdpbi4yazNAZ21haWwuY29tIn0sImNvbXBhbnlOYW1lIjoiZ29NYXJ0IiwiY2xpZW50SUQiOiJjYmEwZGIyNC1hZWM3LTRmY2ItYjc0Zi05NzgyZmZmZmJlMjMiLCJjbGllbnRTZWNyZXQiOiJSWXJ0eE9HWldjTWJGcnd2Iiwib3duZXJOYW1lIjoiQXNod2luIiwib3duZXJFbWFpbCI6ImFzaHdpbi4yazNAZ21haWwuY29tIiwicm9sbE5vIjoiMDA3MjA4MDMxMjEifQ.PojVxtBMfzZesStC24_OiOlweGWF2F-mBsONL_S4Je4'
}

try:
    response = requests.get(url, headers=headers)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        data = response.json()
        print('Received data:')
        print(data)
    else:
        print(f'Failed to fetch data. Status code: {response.status_code}')

except requests.exceptions.RequestException as e:
    print(f'Error fetching data: {str(e)}')
