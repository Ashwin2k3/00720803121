# products/services.py

from django.core.cache import cache

def fetch_and_update_products(category, min_price, max_price):
    cache_key = f'products_{category}_{min_price}_{max_price}'
    products = cache.get(cache_key)
    
    if not products:
        ecommerce_apis = [
            'https://api.ecommerce1.com/products',
            'https://api.ecommerce2.com/products',
            'https://api.ecommerce3.com/products',
            'https://api.ecommerce4.com/products',
            'https://api.ecommerce5.com/products',
        ]
        
        products = []
        for api in ecommerce_apis:
            response = requests.get(api, params={'category': category, 'minPrice': min_price, 'maxPrice': max_price})
            if response.status_code == 200:
                products.extend(response.json())
        
        for product_data in products:
            product, created = Product.objects.update_or_create(
                product_id=product_data['id'],
                defaults={
                    'name': product_data['productName'],
                    'category': category,
                    'price': product_data['price'],
                    'rating': product_data['rating'],
                    'discount': product_data['discount'],
                    'company': product_data['company'],
                    'availability': product_data['availability'],
                }
            )
        cache.set(cache_key, products, timeout=3600)  # Cache for 1 hour

    return products
