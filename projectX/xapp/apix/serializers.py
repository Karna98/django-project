from ..models import Topic, Opinion
from rest_framework import serializers

# Serializer Class for Model Topic
class TopicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Topic
        # Fields to be validated or serialized
        fields = [
            'id',
            'title',
            'published_date'
        ]

# Serializer Class for Model Opinion
class OpinionSerializer(serializers.ModelSerializer):
    class Meta:
        # Model Name
        model = Opinion
        # Fields to be validated or serialized
        fields = [
            'id',
            'topic',
            'opinion',
            'votes'
        ]
