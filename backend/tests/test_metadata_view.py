from rest_framework import status
from django.test import TestCase, Client
from datetime import datetime
from ..models import Metadata
from rest_framework.test import APIRequestFactory

# initialize the APIClient app
client = Client()


class MetadataViewTest(TestCase):
    meta = None

    def setUp(self):
        Metadata.objects.create(
            key='Metadata 1', value='Test value 1', created_date=datetime.now(), modified_date=None
        )
        Metadata.objects.create(
            key='Metadata 2', value='Test value 2', created_date=datetime.now(), modified_date=None
        )
        self.meta = Metadata.objects.all()

    def test_get_all_metadata(self):
        # get API response
        response = self.client.get('/api/metadata')
        result = response.data.get('metadata')[-1]

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(result.get('key'), self.meta.last().key)
        self.assertEqual(result.get('value'), self.meta.last().value)

    def test_get_specific_metadata(self):
        # get API response
        response = self.client.get(
            '/api/metadata/' + str(self.meta.first().id))
        result = response.data.get('metadata')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(result.get('key'), self.meta.first().key)
        self.assertEqual(result.get('value'), self.meta.first().value)

    def test_post_new_metadata(self):
        # get API response
        response = self.client.post(
            '/api/metadata', {'key': 'New Post', 'value': 'Posted Value'}, content_type='application/json')
        result = response.data

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(result.get('status'), 'success')
        self.assertEqual(result.get('metadata').get('key'), 'New Post')
        self.assertEqual(result.get('metadata').get('value'), 'Posted Value')

    def test_post_new_metadata_returns_a_400_status_code_when_invalid_data_is_passed_in(self):
        # get API response
        response = self.client.post(
            '/api/metadata', {'keyq': 'New Post', 'value': 'Posted Value'}, content_type='application/json')
        result = response.data

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(result.get('status'), 'error')

    def test_update_existing_metadata(self):
        # get API response
        response = self.client.put(
            '/api/metadata/' + str(self.meta.last().id), {'key': 'Last post updated', 'value': 'value has changed'}, content_type='application/json')
        result = response.data

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(result.get('status'), 'success')
        self.assertEqual(result.get('metadata').get(
            'key'), 'Last post updated')
        self.assertEqual(result.get('metadata').get(
            'value'), 'value has changed')

    def test_update_existing_metadata_returns_a_400_status_code_when_invalid_data_is_passed_in(self):
        # get API response
        response = self.client.put(
            '/api/metadata/' + str(self.meta.last().id), {'keyq': 'Last post updated', 'value': 'value has changed'}, content_type='application/json')
        result = response.data

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(result.get('status'), 'error')

    def test_remove_specific_metadata(self):
        # get API response
        response = self.client.delete(
            '/api/metadata/' + str(self.meta.first().id))
        result = response.data

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(len(result), 2)
        self.assertEqual(result.get('status'), 'success')
