from django.urls import path

from . import views

app_name = 'xapp'

urlpatterns = [
    # /
    path('', views.index, name='index'),

    # /topic/1/
    path('topic/<int:topic_id>/', views.topic, name='topic'),

    # /opinion/1/
    path('opinion/<int:opinion_id>/', views.opinion, name='opinion'),

    # /opinion/1/vote/
    path('opinion/<int:opinion_id>/vote', views.vote, name='vote')
]