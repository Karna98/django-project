from django.http import HttpResponse, JsonResponse
from django.http.response import Http404
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from rest_framework import status
from rest_framework.views import APIView
from ..models import Topic, Opinion
from .serializers import TopicSerializer, OpinionSerializer

# Create your views here.

class TopicList(APIView):
    """
    List all topics, or create a new topic.
    """
    def get(self, request):
        topics = Topic.objects.all()
        serializer = TopicSerializer(topics, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = TopicSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class TopicDetail(APIView):
    """
    Retrieve, update or delete a topic.
    """
    def get_object(self, pk):
        try:
            topic = Topic.objects.get(pk=pk)
        except Topic.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        topic = self.get_object(pk)
        serializer = TopicSerializer(topic)
        return Response(serializer.data)

    def put(self, request, pk):
        topic = self.get_object(pk)
        serializer = TopicSerializer(topic, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        topic = self.get_object(pk)
        topic.delete()
        return HttpResponse(status=status.HTTP_204_NO_CONTENT)

