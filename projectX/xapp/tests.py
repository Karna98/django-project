from django.test import TestCase
import datetime
from django.utils import timezone
from .models import Topic

# Create your tests here.

class TopicModelTests(TestCase):

    def test_published_ago_with_future_topic(self):
        # published_ago() returns -ve value of days for Topics whose published_date is in the future.
        time = timezone.now() + datetime.timedelta(days=30)
        # Create new topic with future date
        future_topic = Topic(title="Future Title",published_date=time)
        # Stores value of returns form published_ago() 
        getPublishedAgo = future_topic.published_ago()
        # Extract days component from getPublishedAgo 
        days = getPublishedAgo.days
        self.assertIs(days > 0, True)