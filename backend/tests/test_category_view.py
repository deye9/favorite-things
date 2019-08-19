from rest_framework import status
from django.test import TestCase, Client
from datetime import datetime
from ..models import Category
from rest_framework.test import APIRequestFactory

# initialize the APIClient app
client = Client()


class CategoryViewTest(TestCase):

    category = None

    def setUp(self):
        Category.objects.create(
            name='Person', created_date=datetime.now(), modified_date=None
        )
        Category.objects.create(
            name='Place', created_date=datetime.now(), modified_date=None
        )
        self.category = Category.objects.all()

    def test_get_all_category(self):
        # get API response
        response = self.client.get('/api/categories')
        result = response.data.get('categories')[-1]

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(result.get('name'), self.category.last().name)

    def test_get_specific_category(self):
        # get API response
        response = self.client.get(
            '/api/categories/' + str(self.category.first().id))
        result = response.data.get('category')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(result.get('name'), self.category.first().name)

    def test_post_new_category(self):
        # get API response
        response = self.client.post(
            '/api/categories', {'name': 'New Category'}, content_type='application/json')
        result = response.data

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(result.get('status'), 'success')
        self.assertEqual(result.get('category').get('name'), 'New Category')

    def test_post_new_category_returns_a_400_status_code_when_invalid_data_is_passed_in(self):
        # get API response
        response = self.client.post(
            '/api/categories', {'names': 'New Invalid field Name'}, content_type='application/json')
        result = response.data

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(result.get('status'), 'error')

    def test_update_existing_category(self):
        # get API response
        response = self.client.put(
            '/api/categories/' + str(self.category.last().id), {'name': 'Category updated'}, content_type='application/json')
        result = response.data

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(result.get('status'), 'success')
        self.assertEqual(result.get('category').get('name'), 'Category updated')

    def test_update_existing_category_returns_a_400_status_code_when_invalid_data_is_passed_in(self):
        # get API response
        response=self.client.put(
            '/api/categories/' + str(self.category.last().id), {'names': 'New Invalid field Name'}, content_type='application/json')
        result=response.data

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(result.get('status'), 'error')

    def test_remove_specific_category(self):
        # get API response
        response=self.client.delete(
            '/api/categories/' + str(self.category.first().id))
        result=response.data

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(len(result), 2)
        self.assertEqual(result.get('status'), 'success')
