from django.shortcuts import render
from django.http import HttpResponse
# from django.template import loader
from django.shortcuts import render, get_object_or_404
# from django.http import Http404
from .models import Topic, Opinion
# Create your views here.

# Displays list of all topics.
def index(request):
    # Retreiving all the topics order_by published_date. '-published_date' for descending order. 
    listOfTopic = Topic.objects.order_by('-published_date')
    
    # loading the template
    # template = loader.get_template('xapp/index.html')
    
    # variable to be sent to view
    context = {
        'topics' : listOfTopic
    }
    
    # return HttpResponse(template.render(context, request))
    return render(request, 'xapp/index.html', context)

# Displays all details related to specific topic.
def topic(request, topic_id):
    # Get details of topic with id = topic_id
    getDetailsOfTopic = get_object_or_404(Topic, id=topic_id)
    context = {
        'topic' : getDetailsOfTopic
    }
    return render(request, 'xapp/topic.html', context)

# Displays all details related to specific opinion
def opinion(request, opinion_id):
    response = "You're looking at the opinion %s."
    return HttpResponse(response % opinion_id)

# Vote action related to specific opinion
def vote(request, opinion_id):
    return HttpResponse("You're voting for Opinion %s." % opinion_id)