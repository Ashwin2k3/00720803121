import requests
from django.http import JsonResponse
from django.conf import settings

def get_top_products(request, categoryname):
    top = request.GET.get('top', 10)
    min_price = request.GET.get('minPrice', 0)
    max_price = request.GET.get('maxPrice', 10000)
    
    # API endpoint to fetch products
    url = f"http://20.244.56.144/test/companies/AMZ/categories/{categoryname}/products"
    headers = {
        "Authorization": f"Bearer {settings.ACCESS_TOKEN}"
    }
    params = {
        'top': top,
        'minPrice': min_price,
        'maxPrice': max_price
    }

    print(f"Request URL: {url}")
    print(f"Headers: {headers}")
    print(f"Params: {params}")

    response = requests.get(url, headers=headers, params=params)

    print(f"Status Code: {response.status_code}")
    print(f"Response Content: {response.content}")

    if response.status_code == 200:
        products = response.json()
        return JsonResponse(products, safe=False)
    else:
        return JsonResponse({'error': 'Failed to fetch data from external API', 'details': response.content.decode()}, status=response.status_code)

def get_product_details(request, categoryname, productid):
    # API endpoint to fetch product details
    url = f"http://20.244.56.144/test/companies/AMZ/categories/{categoryname}/products/{productid}"
    headers = {
        "Authorization": f"Bearer {settings.ACCESS_TOKEN}"
    }

    print(f"Request URL: {url}")
    print(f"Headers: {headers}")

    response = requests.get(url, headers=headers)

    print(f"Status Code: {response.status_code}")
    print(f"Response Content: {response.content}")

    if response.status_code == 200:
        product_details = response.json()
        return JsonResponse(product_details, safe=False)
    else:
        return JsonResponse({'error': 'Failed to fetch product details from external API', 'details': response.content.decode()}, status=response.status_code)
