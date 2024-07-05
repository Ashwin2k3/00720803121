# products/management/commands/fetchdata.py

from django.core.management.base import BaseCommand
import requests

class Command(BaseCommand):
    help = 'Fetches data from an external API'

    def handle(self, *args, **options):
        url = 'http://20.244.56.144/test/companies/AMZ/categories/Laptop/products'
        headers = {
            'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJNYXBDbGFpbXMiOnsiZXhwIjoxNzIwMTU4NDI5LCJpYXQiOjE3MjAxNTgxMjksImlzcyI6IkFmZm9yZG1lZCIsImp0aSI6ImNiYTBkYjI0LWFlYzctNGZjYi1iNzRmLTk3ODJmZmZmYmUyMyIsInN1YiI6ImFzaHdpbi4yazNAZ21haWwuY29tIn0sImNvbXBhbnlOYW1lIjoiZ29NYXJ0IiwiY2xpZW50SUQiOiJjYmEwZGIyNC1hZWM3LTRmY2ItYjc0Zi05NzgyZmZmZmJlMjMiLCJjbGllbnRTZWNyZXQiOiJSWXJ0eE9HWldjTWJGcnd2Iiwib3duZXJOYW1lIjoiQXNod2luIiwib3duZXJFbWFpbCI6ImFzaHdpbi4yazNAZ21haWwuY29tIiwicm9sbE5vIjoiMDA3MjA4MDMxMjEifQ.PojVxtBMfzZesStC24_OiOlweGWF2F-mBsONL_S4Je4'
        }

        try:
            response = requests.get(url, headers=headers)
            if response.status_code == 200:
                products = response.json()
                self.stdout.write(self.style.SUCCESS(f'Successfully fetched data: {products}'))
            else:
                self.stderr.write(f'Failed to fetch data from external API: {response.status_code}')
        except requests.exceptions.RequestException as e:
            self.stderr.write(f'Error fetching data: {str(e)}')
