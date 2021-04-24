from django.http import HttpResponse
from django.http.response import Http404
from rest_framework.response import Response
from rest_framework import status, viewsets
from rest_framework.views import APIView
from ..models import Topic, Opinion
from .serializers import TopicSerializer, OpinionSerializer

# Create your views here.

class TopicDetailViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.
    """
    lookup_field = 'pk'
    queryset = Topic.objects.all()
    serializer_class = TopicSerializer

