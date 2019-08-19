from django.test import TestCase
from datetime import datetime
from ..models import Category


class CategoryTest(TestCase):
    """ Test module for Category model """

    def setUp(self):
        Category.objects.create(
            name='Person', created_date=datetime.now(), modified_date=datetime.now()
        )
        Category.objects.create(
            name='Place', created_date=datetime.now(), modified_date=datetime.now()
        )

    def test_category_creation(self):
        category1 = Category.objects.get(name='Person')
        category2 = Category.objects.get(name='Place')
        self.assertEqual(category1.name, "Person")
        self.assertEqual(category2.name, 'Place')

    def test_category_updates(self):
        category = Category.objects.get(name='Person')

        category.name = 'Updated Person'
        category.save()

        self.assertEqual(category.name, "Updated Person")

    def test_category_deletion(self):
        category = Category.objects.get(name="Place")
        category.delete()

        with self.assertRaises(Category.DoesNotExist) as context:
            Category.objects.get(name='Place')

