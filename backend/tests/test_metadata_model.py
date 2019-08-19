from django.test import TestCase
from datetime import datetime
from ..models import Metadata


class MetadataTest(TestCase):
    """ Test module for Metadata model """

    def setUp(self):
        Metadata.objects.create(
            key='Metadata 1', value='Test value 1', created_date=datetime.now(), modified_date=datetime.now()
        )
        Metadata.objects.create(
            key='Metadata 2', value='Test value 2', created_date=datetime.now(), modified_date=datetime.now()
        )

    def test_metadata_creation(self):
        meta1 = Metadata.objects.get(key='Metadata 1')
        meta2 = Metadata.objects.get(key='Metadata 2')

        self.assertEqual(meta1.key, "Metadata 1")
        self.assertEqual(meta1.value, "Test value 1")
        self.assertEqual(meta2.key, "Metadata 2")
        self.assertEqual(meta2.value, "Test value 2")

    def test_metadata_updates(self):
        meta1 = Metadata.objects.get(key='Metadata 1')

        meta1.key = 'Updated Metadata'
        meta1.value = 'Updated value'
        meta1.modified_date = datetime.now()
        meta1.save()

        self.assertEqual(meta1.key, "Updated Metadata")
        self.assertEqual(meta1.value, "Updated value")

    def test_metadata_deletion(self):
        meta1 = Metadata.objects.get(key='Metadata 1')
        meta1.delete()

        with self.assertRaises(Metadata.DoesNotExist) as context:
            Metadata.objects.get(key='Metadata 1')
