from django.test import TestCase
from django.urls import reverse

from .models import Product


class ProductAddViewTests(TestCase):
    def test_product_add_creates_product_with_minimum_stock_level(self):
        response = self.client.post(
            reverse("product_add"),
            {
                "product_name": "Keyboard",
                "category": "Accessories",
                "price": "49.99",
                "quantity": "10",
                "supplier": "Supplier",
                "minimum_stock_level": "3",
            },
        )

        self.assertEqual(response.status_code, 302)
        product = Product.objects.get(product_name="Keyboard")
        self.assertEqual(product.minimum_stock_level, 3)


class ProductListViewTests(TestCase):
    def test_product_list_without_search_renders_first_page(self):
        Product.objects.create(
            product_name="Keyboard",
            category="Accessories",
            price=49.99,
            quantity=10,
            minimum_stock_level=3,
        )

        response = self.client.get(reverse("product_list"))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Keyboard")
