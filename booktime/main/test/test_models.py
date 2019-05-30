from decimal import Decimal
from django.test import TestCase
from main import models

class TestModel(TestCase):
    def test_active_manager_work(self):
        models.Product.objects.create(
            name="Expensive Clothes",
            price=Decimal("10.00")
        )
        models.Product.objects.create(
            name="New Shoes",
            price=Decimal("132.00")
        )
        models.Product.objects.create(
            name="Wood Table",
            price=Decimal("1000"),
            active=False
        )
        self.assertEqual(len(models.Product.objects.active()), 2)
        