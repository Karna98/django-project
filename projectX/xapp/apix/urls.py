from django.urls import path
from .views import TopicList, TopicDetail 

urlpatterns = [
    path('topics/', TopicList.as_view()),
    path('topics/<int:pk>/', TopicDetail.as_view()),
]