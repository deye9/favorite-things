from rest_framework import status
from django.test import TestCase, Client
from datetime import datetime
from ..models import Tracker, Metadata, Category
from rest_framework.test import APIRequestFactory

# initialize the APIClient app
client = Client()


class TrackerViewTest(TestCase):

    meta = None
    tracker = None
    category = None

    def setUp(self):
        Metadata.objects.create(
            key='Metadata 1', value='Test value 1', created_date=datetime.now(), modified_date=datetime.now()
        )
        self.meta = Metadata.objects.get(key='Metadata 1')

        Category.objects.create(
            name='Person', created_date=datetime.now(), modified_date=datetime.now()
        )
        self.category = Category.objects.get(name='Person')

        Tracker.objects.create(
            title='Tracker 1', description='Sample Description', ranking=1, metadata=self.meta, category=self.category, created_date=datetime.now(), modified_date=datetime.now()
        )
        Tracker.objects.create(
            title='Tracker 2', description='Sample Description for Tracker 2', ranking=2, metadata=self.meta, category=self.category, created_date=datetime.now(), modified_date=datetime.now()
        )
        self.tracker = Tracker.objects.all()

    def test_get_all_items(self):
        # get API response
        response = self.client.get('/api/items')
        result = response.data.get('items')[-1]

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(result.get('title'), self.tracker.last().title)
        self.assertEqual(result.get('description'),
                         self.tracker.last().description)
        self.assertEqual(result.get('ranking'), self.tracker.last().ranking)
        self.assertEqual(result.get('metadata'), self.meta.id)
        self.assertEqual(result.get('category'), self.category.id)

    def test_get_specific_item(self):
        # get API response
        response = self.client.get(
            '/api/items/' + str(self.tracker.first().id))
        result = response.data.get('item')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(result.get('title'), self.tracker.first().title)
        self.assertEqual(result.get('description'),
                         self.tracker.first().description)
        self.assertEqual(result.get('ranking'), self.tracker.first().ranking)
        self.assertEqual(result.get('metadata'), self.meta.id)
        self.assertEqual(result.get('category'), self.category.id)

    def test_post_new_item(self):
        # get API response
        response = self.client.post(
            '/api/items', {'title':'My laptop', 'description':'My laptop is new', 'ranking':1, 'metadata':self.meta.id, 'category':self.category.id}, content_type='application/json')
        result = response.data

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(result.get('status'), 'success')
        self.assertEqual(result.get('items').get('title'), 'My laptop')
        self.assertEqual(result.get('items').get('description'), 'My laptop is new')
        self.assertEqual(result.get('items').get('ranking'), 1)
        self.assertEqual(result.get('items').get('metadata'), self.meta.id)
        self.assertEqual(result.get('items').get('category'), self.category.id)

    def test_post_new_item_returns_a_400_status_code_when_invalid_data_is_passed_in(self):
        # get API response
        response = self.client.post(
            '/api/items', {'titlew': 'My laptop', 'description': 'My laptop is new', 'ranking': 1, 'metadata': self.meta.id, 'category': self.category.id}, content_type='application/json')
        result = response.data

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(result.get('status'), 'error')

    def test_post_new_item_returns_a_400_status_code_when_invalid_metadata_is_passed_in(self):
        # get API response
        response = self.client.post(
            '/api/items', {'title': 'My laptop', 'description': 'My laptop is new', 'ranking': 1, 'metadata': 10, 'category': self.category.id}, content_type='application/json')
        result = response.data

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(result.get('status'), 'error')

    def test_post_new_item_returns_a_400_status_code_when_invalid_category_is_passed_in(self):
        # get API response
        response = self.client.post(
            '/api/items', {'title': 'My laptop', 'description': 'My laptop is new', 'ranking': 1, 'metadata': self.meta.id, 'category': 50}, content_type='application/json')
        result = response.data

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(result.get('status'), 'error')

    def test_update_existing_item(self):
        # get API response
        response = self.client.put(
            '/api/items/' + str(self.tracker.last().id), {'title': 'My laptop.', 'description': 'Is my laptop really new', 'ranking': 2, 'metadata': self.meta.id, 'category': self.category.id}, content_type='application/json')
        result = response.data

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(result.get('status'), 'success')
        self.assertEqual(result.get('items').get('title'), 'My laptop.')
        self.assertEqual(result.get('items').get(
            'description'), 'Is my laptop really new')
        self.assertEqual(result.get('items').get('ranking'), 2)
        self.assertEqual(result.get('items').get('metadata'), self.meta.id)
        self.assertEqual(result.get('items').get('category'), self.meta.id)

    def test_update_existing_item_returns_a_400_status_code_when_invalid_data_is_passed_in(self):
        # get API response
        response = self.client.put(
            '/api/items/' + str(self.tracker.last().id), {'titles': 'My laptop.', 'description': 'Is my laptop really new', 'ranking': 2, 'metadata': self.meta.id, 'category': self.category.id}, content_type='application/json')
        result = response.data

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(result.get('status'), 'error')

    def test_post_existing_item_returns_a_400_status_code_when_invalid_metadata_is_passed_in(self):
        # get API response
        response = self.client.put(
            '/api/items/' + str(self.tracker.last().id), {'title': 'My laptop', 'description': 'My laptop is new', 'ranking': 1, 'metadata': 10, 'category': self.category.id}, content_type='application/json')
        result = response.data

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(result.get('status'), 'error')

    def test_post_existing_item_returns_a_400_status_code_when_invalid_category_is_passed_in(self):
        # get API response
        response = self.client.put(
            '/api/items/' + str(self.tracker.last().id), {'title': 'My laptop', 'description': 'My laptop is new', 'ranking': 1, 'metadata': self.meta.id, 'category': 50}, content_type='application/json')
        result = response.data

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(result.get('status'), 'error')

    def test_remove_specific_item(self):
        # get API response
        response = self.client.delete(
            '/api/items/' + str(self.tracker.first().id))
        result = response.data

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(len(result), 2)
        self.assertEqual(result.get('status'), 'success')
