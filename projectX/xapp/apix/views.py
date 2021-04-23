from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from ..models import Topic, Opinion
from .serializers import TopicSerializer, OpinionSerializer

# Create your views here.

# Note that because we want to be able to POST to this view from clients
# that won't have a CSRF token we need to mark the view as csrf_exempt temporarily.
@csrf_exempt
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
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def topic_detail(request, pk):
    """
    Retrieve, update or delete a topic.
    """
    try:
        topic = Topic.objects.get(pk=pk)
    except Topic.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = TopicSerializer(topic)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = TopicSerializer(topic, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        topic.delete()
        return HttpResponse(status=204)

