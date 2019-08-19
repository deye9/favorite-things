from django.test import TestCase
from datetime import datetime
from ..models import Tracker, Metadata, Category


class TrackerTest(TestCase):
    """ Test module for Tracker model """
    meta = None
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

    def test_tracker_creation(self):
        tracker1 = Tracker.objects.get(title='Tracker 1')
        tracker2 = Tracker.objects.get(title='Tracker 2')

        self.assertEqual(tracker1.ranking, 1)
        self.assertEqual(tracker1.title, "Tracker 1")
        self.assertEqual(tracker1.metadata, self.meta)
        self.assertEqual(tracker1.category, self.category)
        self.assertEqual(tracker1.description, "Sample Description")

        self.assertEqual(tracker2.ranking, 2)
        self.assertEqual(tracker2.title, "Tracker 2")
        self.assertEqual(tracker2.metadata, self.meta)
        self.assertEqual(tracker2.category, self.category)
        self.assertEqual(tracker2.description,
                         "Sample Description for Tracker 2")

    def test_tracker_updates(self):
        tracker = Tracker.objects.get(title='Tracker 1')

        tracker.ranking = 3
        tracker.metadata = self.meta
        tracker.category = self.category
        tracker.title = 'Updated Tracker'
        tracker.modified_date = datetime.now()
        tracker.description = 'No new updates here'
        tracker.save()

        self.assertEqual(tracker.ranking, 3)
        self.assertEqual(tracker.metadata, self.meta)
        self.assertEqual(tracker.category, self.category)
        self.assertEqual(tracker.title, 'Updated Tracker')
        self.assertEqual(tracker.description, 'No new updates here')

    def test_tracker_deletion(self):
        tracker = Tracker.objects.get(title='Tracker 1')
        tracker.delete()

        with self.assertRaises(Tracker.DoesNotExist) as context:
            Tracker.objects.get(title='Tracker 1')
