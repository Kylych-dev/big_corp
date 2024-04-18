from django.test import TestCase
from django.core.files.uploadedfile import SimpleUploadedFile
from apps.product.models import Product

class ProductTestCase(TestCase):
    def setUp(self):
        self.product = Product.objects.create()