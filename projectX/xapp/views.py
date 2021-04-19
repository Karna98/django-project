from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
# from django.template import loader
from django.shortcuts import render, get_object_or_404
# from django.http import Http404
from django.urls import reverse
from django.views import generic

from .models import Topic, Opinion
# Create your views here.

'''
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
'''

# Displays list of all topics.
# Generic List View
class IndexView(generic.ListView):
    template_name = 'xapp/index.html'
    context_object_name = 'topics'

    def get_queryset(self):
        # Retreiving all the topics order_by published_date. '-published_date' for descending order.
        return Topic.objects.order_by('-published_date')

'''
# Displays all details related to specific topic.
def topic(request, topic_id):
    # Get details of topic with id = topic_id
    getDetailsOfTopic = get_object_or_404(Topic, id=topic_id)
    context = {
        'topic' : getDetailsOfTopic
    }
    return render(request, 'xapp/topic.html', context)
'''

# Displays all details related to specific topic.
# Generic Detail View
class TopicView(generic.DetailView):
    model = Topic
    template_name = 'xapp/topic.html'

'''
# Displays all details related to specific opinion
def opinion(request, opinion_id):
        # Get details of topic with id = topic_id
    getDetailsOfTOpininon = get_object_or_404(Opinion, id=opinion_id)
    context = {
        'opinion' : getDetailsOfTOpininon
    }
    return render(request, 'xapp/opinion.html', context)
'''

# Displays all details related to specific opinion
# Generic Detail View
class OpinionView(generic.DetailView):
    model = Opinion
    template_name = 'xapp/opinion.html'

# Vote action related to specific opinion
def vote(request, opinion_id):
    if request.method =='POST':
        # Get the Opinion with opinion_id from URL, if present else throw 404 Error
        opinion = get_object_or_404(Opinion, pk=opinion_id)

        # Check data type of variable using type()
        # print(type(request.POST['opinion-vote']))
        # print(type(opinion_id))

        # If opinion_id from URL matched the data obtained from request.POST then validate the vote  
        if (int(request.POST['opinion-vote']) == opinion_id):
            opinion.votes += 1
            opinion.save()

            # Always return an HttpResponseRedirect after successfully dealing
            # with POST data. This prevents data from being posted twice if a
            # user hits the Back button.
            return HttpResponseRedirect(reverse('xapp:opinion', args=(opinion_id, )))
        else:
            return HttpResponseRedirect(render(request, 'xapp/opinion.html', {
                'opinion': opinion,
                'error_message': "Error encountered while registering your vote",
            }))

    else:
        return HttpResponse('Method Not allowed !')
