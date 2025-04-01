from django.test import TestCase
from .models import Category, Product
from django.urls import reverse

class CategoryModelTest(TestCase):
    def setUp(self):
        self.category = Category.objects.create(
            name='Alchohol',
            description='Alchoholic beverage'
        )

    def test_category_creation(self):
        self.assertEqual(self.category.name, 'Alchohol')
        self.assertEqual(self.category.description, 'Alchoholic beverage')

    def test_category_str_method(self):
        self.assertEqual(str(self.category), 'Alchohol')

    def test_category_get_absolute_url(self):
        expected_url = reverse('shop:products_by_category', args=[str(self.category.id)])
        self.assertEqual(self.category.get_absolute_url(), expected_url)

class ProductModelTest(TestCase):
    def setUp(self):
        self.category = Category.objects.create(
        name='Beer',
        description='Fizzy wheat'
        )
        self.product = Product.objects.create(
        name='Heiniken',
        description='dutch fizzy wheat',
        category=self.category,
        price=3.99,
        stock=20,
        available=True
)
    def test_product_creation(self):
        self.assertEqual(self.product.name, 'Heiniken')
        self.assertEqual(self.product.description, 'dutch fizzy wheat')
        self.assertEqual(self.product.category, self.category)
        self.assertEqual(self.product.price, 3.99)
        self.assertEqual(self.product.stock, 20)
        self.assertTrue(self.product.available)

    def test_product_str_method(self):
        self.assertEqual(str(self.product), 'Heiniken')

    def test_product_get_absolute_url(self):
        expected_url = reverse('shop:product_detail', args=[str(self.category.id), str(self.product.id)])
        self.assertEqual(self.product.get_absolute_url(), expected_url)

class ShopViewsTest(TestCase):
    def setUp(self):
        self.category = Category.objects.create(name='Test Category')
        self.product = Product.objects.create(
            name='Test Product',
            category=self.category,
            description='Test Description',
            price=10.99,
            stock=45,
            available=True,
        )

    def test_prod_list_view(self):
        response = self.client.get(reverse('shop:all_products'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Category')
        self.assertTemplateUsed(response, 'shop/category.html')

    def test_prod_list_view_with_category(self):
        response = self.client.get(reverse('shop:products_by_category', args=[self.category.id]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Category')
        self.assertTemplateUsed(response, 'shop/category.html')

    def test_product_detail_view(self):
        response = self.client.get(reverse('shop:product_detail', args=[self.category.id, self.product.id]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Product')
        self.assertTemplateUsed(response, 'shop/product.html')

class ShopUrlsTestCase(TestCase):
    def setUp(self):
        self.category = Category.objects.create(name='Test Category')
        self.product = Product.objects.create(name='Test Product', price='50.00',stock='4',category=self.category)

    def test_all_products_url(self):
        url = reverse('shop:all_products')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_products_by_category_url(self):
        url = reverse('shop:products_by_category', args=[str(self.category.id)])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_product_detail_url(self):
        url = reverse('shop:product_detail', args=[str(self.category.id), str(self.product.id)])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)