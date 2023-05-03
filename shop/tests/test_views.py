from django.test import Client, TestCase
from django.urls import reverse
from shop.models import Product

# Create your tests here.
# use the line below for debugging so that you can see what is on the page
#  print(response.content)

class ShopViewsTests(TestCase):
        @classmethod
        def setUpTestData(cls):
            # set up test data in database
            Product.objects.create(name = "Boateng Toaster", price= 23.99)
            Product.objects.create(name = "Boateng Stool", price= 3.99)
            

        def test_home(self):
            client = Client()
            response = client.get('/')
            self.assertEqual(response.status_code, 200)
            self.assertContains(response, "Boateng Shopping Home")
            self.assertContains(response, "Boateng Toaster")
        
        
    
