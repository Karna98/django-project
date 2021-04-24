from django.http import HttpResponse, JsonResponse
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from rest_framework import status
from ..models import Topic, Opinion
from .serializers import TopicSerializer, OpinionSerializer

# Create your views here.

@api_view(['GET', 'POST'])
def topic_list(request):
    """
    List all topics, or create a new topic.
    """
    if request.method == 'GET':
        topics = Topic.objects.all()
        serializer = TopicSerializer(topics, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = TopicSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def topic_detail(request, pk):
    """
    Retrieve, update or delete a topic.
    """
    try:
        topic = Topic.objects.get(pk=pk)
    except Topic.DoesNotExist:
        return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = TopicSerializer(topic)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = TopicSerializer(topic, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        topic.delete()
        return HttpResponse(status=status.HTTP_204_NO_CONTENT)

