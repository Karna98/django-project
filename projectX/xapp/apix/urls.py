from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TopicDetailViewSet

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'topics',TopicDetailViewSet)


urlpatterns = [
    # path('topics/',
    #     TopicViewSet.as_view({
    #         'get': 'list'
    #     }),
    #     name='topic-list'
    # ),

    # path('topics/<int:pk>/',
    #     TopicDetailViewSet.as_view({
    #         'get': 'retrieve',
    #         'post': 'create',
    #         'patch': 'partial_update',
    #         'delete': 'destroy'
    #     }),
    #     name='topic-detail'
    # ),
    path('', include(router.urls)),
]