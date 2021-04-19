from django.urls import path

from . import views

app_name = 'xapp'

urlpatterns = [
    # /
    # path('', views.index, name='index'),
    # Generic View 
    path('', views.IndexView.as_view(), name='index'),

    # /topic/1/
    # path('topic/<int:topic_id>/', views.topic, name='topic'),
    # Generic View
    path('topic/<int:pk>/', views.TopicView.as_view(), name='topic'),

    # /opinion/1/
    # path('opinion/<int:opinion_id>/', views.opinion, name='opinion'),
    # Generic View
    path('opinion/<int:pk>/', views.OpinionView.as_view(), name='opinion'),

    # /opinion/1/vote/
    path('opinion/<int:opinion_id>/vote', views.vote, name='vote')
]