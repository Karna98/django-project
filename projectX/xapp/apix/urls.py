from django.urls import path
from .views import topic_list, topic_detail 

urlpatterns = [
    path('topics/', topic_list),
    path('topics/<int:pk>/', topic_detail),
]