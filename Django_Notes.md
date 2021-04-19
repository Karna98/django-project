# Notes

1. Editing **xapp**-*view* [🔗](https://docs.djangoproject.com/en/3.2/intro/tutorial01/#write-your-first-view)
    ```
    # xapp/views.py

    def index(request):
        return HttpResponse
    ```

2. Mapping **xapp**-*view* to **xapp**-*url* 
    ```
    # xapp/views.py
    
    urlpatterns = [
        path('', views.index, name='index')
    ]
    ```
    - [path(route, view, kwargs=None, name=None)](https://docs.djangoproject.com/en/3.2/ref/urls/#django.urls.path)
        - [route](https://docs.djangoproject.com/en/3.2/intro/tutorial01/#path-argument-route)
        - [view](https://docs.djangoproject.com/en/3.2/intro/tutorial01/#path-argument-view)
        - [kwargs](https://docs.djangoproject.com/en/3.2/intro/tutorial01/#path-argument-kwargs)
        - [name](https://docs.djangoproject.com/en/3.2/intro/tutorial01/#path-argument-name)

3. Hooking **xapp**-*url* to **projectX**-*url*
    ```
    # projectX/views.py
    
    urlpatterns = [
        path('xapp/', include('xapp.urls'))
    ]
    ```
    - [include()](https://docs.djangoproject.com/en/3.2/ref/urls/#django.urls.include) - function allows referencing other URLconfs

4. Playing with **projectX**-*settings* [🔗](https://docs.djangoproject.com/en/3.2/intro/tutorial02/#database-setup)  
    ```
    # To migrate databases of app's present in INSTALLED_APP in projectX/settings.py
    python manage.py migrate
    ```

5. Creating Models[🔗](https://docs.djangoproject.com/en/3.2/intro/tutorial02/#creating-models)  
    Here we will be creating two tables named "Topic" and "Opinion".  
    - **Topic**
        - Title of Topic
        - Date Published
    - **Opinion**
        - Related to which original topic
        - Opinion
        - No. of votes

    ```
    # xapp/models.py
    
    class Topic(models.Model):
        # Define different fields for 'Topic' table.

    class Opinion(models.Model):
        # Define different fields for 'Opinion' table.
    ```

    - [Models](https://docs.djangoproject.com/en/3.2/topics/db/models/)
    - [Field Types](https://docs.djangoproject.com/en/3.2/ref/models/fields/#field-types)

6. Activating models [🔗](https://docs.djangoproject.com/en/3.2/intro/tutorial02/#activating-models)  
    To include **xapp** in **projectX**, we need to add a reference to its configuration class in INSTALLED_APPS setting.
    ```
    # projectX/settings.py
    
    INSTALLED_APPS = [
        'django.contrib.admin',
        . . .
        'xapp.apps.XappConfig'
    ]

    ```
    
    Once the 'projectX' about 'xapp' config, let's migrate the models of 'xapp' by running the following command
    ```
    $ python manage.py makemigrations xapp
    ```

    To check what SQL that migration would run, 
    ```
    # here 0001, considering 'xapp/migrations/0001_initial.py'
    
    $ python manage.py sqlmigrate xapp 0001
    ```

    Finally, to create the models in database, run
    ```
    $ python manage.py migrate
    ```
    'xapp_Topic' and 'xapp_Opinion' can be seen in database.

    If you want to make changes in models again then
    - To create migrations for new changes
        ```
        $ python manage.py makemigrations
        ```
    - To apply new changes to the database
        ```
        $ python manage.py migrate
        ```

7. Play with tables created using Python Shell [🔗](https://docs.djangoproject.com/en/3.2/intro/tutorial02/#playing-with-the-api)  
    Let's open Python shell,
    ```
    $ python manage.py shell
    ```

    Once the python shell opens, let's execute the following commands
    - Import the model classes we just wrote
        ```
        >>> from xapp.models import Topic, Opinion
        ```
    - Retrieve all Topic
        ```
        >>> Topic.objects.all()
        ```
    - Insert a new topic in DB
        ```
        >>> from django.utils import timezone
        
        # Create a new Topic
        >>> newTopic = Topic(title="Title 1", published_date=timezone.now())

        # Save the object into the database. You have to call save() explicitly.
        >>> newTopic.save()

        # Get ID of newTopic inserted
        >>> newTopic.id
        # Output : 1

        # Get title of newTopic inserted
        >>> newTopic.title
        # Output : 'Title 1'

        # Get Published Date of newTopic inserted
        >>> newTopic.published_date
        # Output : datetime.datetime(2021, 4, 16, 19, 44, 32, 177653, tzinfo=<UTC>)

        # Change values by changing the attributes, then calling save().
        >>> newTopic.title = 'Title 1.1'
        >>> newTopic.save()

        # objects.all() displays all the questions in the database.
        >>> Topic.objects.all()
        # Output : <QuerySet [<Topic: Topic object (1)>]>  
        ``` 

    Observe the output of the last query. was it any helpful? **NO**  
    Let's fix this by modifying the output in *xapp/models.py*

    To get the output as desired,
    ```
    # xapp/models.py
    
    class Topic(models.Model):
        . . .
        # Defining desired output by modifying __str__().
        def __str__(self):
            return '{ Title : "' + self.title + '", Published Date : "' + str(self.published_date) + '" }'

    class Opinion(models.Model):
        . . .
        # Defining desired output  by modifying __str__().
        def __str__(self):
            return return '{ Opinion : "' + self.opinion + '", Votes : "' + str(self.votes) + '" }'
    ```

    Let's also add a custom method, 
    ```
    # xapp/models.py
    
    class Topic(models.Model):
        . . .
        # Custom Method : How old is title (published)?
        def published_ago(self):
            return current_date - published_date
    ```

    Let's test above added methods,
    ```
    >>> from django.utils import timezone
    >>> from xapp.models import Topic, Opinion
    
    # See all the Topic with new modified __str__()
    >>> Topic.objects.all()
    # <QuerySet [<Topic: { Title : "Title 1", Published Date : "2021-04-16 19:17:20.814756+00:00" }>, <Topic: { Title : "Title 1.1", Published Date : "2021-04-17 16:56:01.784471+00:00" }>]>

    # Testing custom function published_ago() 
    >>> topic = Topic.objects.get(id=1)
    >>> topic.published_ago()
    # Output : datetime.timedelta(seconds=75129, microseconds=618923)

    # Get Topic with id = 1
    >>> Topic.objects.get(id=1)
    # Output : <Topic: { Title : "Title 1", Published Date : "2021-04-16 19:17:20.814756+00:00" }>

    # Get Topic with invalid id = 4
    >>> Topic.objects.get(id=4)
    # Output : Traceback (most recent call last):
    #          ...
    #          xapp.models.Topic.DoesNotExist: Topic matching query does not exist.

    # Get Topic published today (i.e. on 17-04-2021)
    >>> Topic.objects.get(published_date__date='2021-04-17')
    # Output : <Topic: { Title : "Title 1.1", Published Date : "2021-04-17 16:56:01.784471+00:00" }>

    # Get Topic with pk = 1 (pk is primary key)
    >>> Topic.objects.get(pk=1)
    # Output : <Topic: { Title : "Title 1", Published Date : "2021-04-16 19:17:20.814756+00:00" }>

    # Get Published Date of newTopic inserted
    >>> newTopic.published_date
    # Output : datetime.datetime(2021, 4, 16, 19, 44, 32, 177653, tzinfo=<UTC>)

    # Using Filters 
    >>> Topic.objects.filter(id=2)
    # Ouptut : <QuerySet [<Topic: { Title : "Title 1.1", Published Date : "2021-04-17 16:56:01.784471+00:00" }>]>
    >>> Topic.objects.filter(title__startswith='Title')
    # Output : <QuerySet [<Topic: { Title : "Title 1", Published Date : "2021-04-16 19:17:20.814756+00:00" }>, <Topic: { Title : "Title 1.1", Published Date : "2021-04-17 16:56:01.784471+00:00" }>]>
    
    # Get Opinion related to Topic with id=1
    >>> topic = Topic.objects.get(id=1)
    # Display any opinion from the related object set -- none so far.
    >>> topic.opinion_set.all()
    # Output : <QuerySet []>

    # Let's create 3 opinions
    >>> topic_one = Topic.objects.get(id=1)
    >>> topic_one.opinion_set.create(opinion="Opinion 1 related to Topic Title 1", votes=1)
    # Output : <Opinion: { Opinion : "Opinion 1 related to Topic Title 1", Votes : "1" }>
    >>> topic_two = Topic.objects.get(id=2)   
    >>> topic_two.opinion_set.create(opinion="Opinion 1 related to Topic Title 1.1", votes=0)
    # Output : <Opinion: { Opinion : "Opinion 1 related to Topic Title 1.1", Votes : "0" }>
    >>> topic_two.opinion_set.create(opinion="Opinion 2 related to Topic Title 1.1", votes=5)
    # Output : <Opinion: { Opinion : "Opinion 2 related to Topic Title 1.1", Votes : "5" }>

    # objects.all() displays all the opinions in the database.
    >>> Opinion.objects.all()
    # Output : <QuerySet [<Opinion: { Opinion : "Opinion 1 related to Topic Title 1", Votes : "1" }>, <Opinion: { Opinion : "Opinion 1 related to Topic Title 1.1", Votes : "0" }>, <Opinion: { Opinion : "Opinion 2 related to Topic Title 1.1", Votes : "5" }>]>

    >>> topic_one.opinion_set.all()
    # Output : <QuerySet [<Opinion: { Opinion : "Opinion 1 related to Topic Title 1", Votes : "1" }>]>
    >>> topic_two.opinion_set.all()
    # Output : <QuerySet [<Opinion: { Opinion : "Opinion 1 related to Topic Title 1.1", Votes : "0" }>, <Opinion: { Opinion : "Opinion 2 related to Topic Title 1.1", Votes : "5" }>]>

    >>> topic_one.opinion_set.count()
    # Output : 1
    >>> topic_two.opinion_set.count()
    # Output : 2

    # Get opinions which are related to topic published on date '2021-04-17'
    >>> Opinion.objects.filter(topic__published_date__date='2021-04-17')
    # Output : <QuerySet [<Opinion: { Opinion : "Opinion 1 related to Topic Title 1.1", Votes : "0" }>, <Opinion: { Opinion : "Opinion 2 related to Topic Title 1.1", Votes : "5" }>]>

    # Let's delete one of the opinion which starts with "Opinion 2"
    >>> opinion_two = topic_two.opinion_set.filter(opinion__startswith='Opinion 2')
    >>> opinion_two.delete()
    # Output : (1, {'xapp.Opinion': 1})
    ```

    - [Database Queries API](https://docs.djangoproject.com/en/3.2/topics/db/queries/)
    - [__str __()](https://docs.djangoproject.com/en/3.2/ref/models/instances/#django.db.models.Model.__str__)
    - [Timezones](https://docs.djangoproject.com/en/3.2/topics/i18n/timezones/)
    - [ Accessing related objects](https://docs.djangoproject.com/en/3.2/ref/models/relations/)
    - [Field lookups](https://docs.djangoproject.com/en/3.2/topics/db/queries/#field-lookups-intro)

8. Introducing the Django Admin [🔗](https://docs.djangoproject.com/en/3.2/intro/tutorial02/#introducing-the-django-admin)
    - Creating an admin user
        ```
        python manage.py createsuperuser
        ```
        Enter the desired username and press Enter
        ```
        Username : admin        
        ```
        Enter the email address and press Enter
        ```
        Email address : admin@django.in        
        ```
        Enter password and press Enter
        ```
        Password : 123@dmin
        Password (again) : 123@dmin        
        ```
        On successfully creating superuser, "_Superuser created successfully_." will be displayed

        Now visit http://127.0.0.1:8000/admin/ and log in with superuser credentials created above.

    - Adding **xapp** in Admin Panel
        ```
        # xapp/admin.py
    
        from .models import Topic, Opinion
        
        # Registering Topic and Opinion Model
        admin.site.register([Topic, Opinion])
        ```
    - Observe on [Admin Panel](http://127.0.0.1:8000/admin/), **xapp** will be displayed along with *Topic* and *Opinion* listed under **xapp**. 

    - Explore the Admin Functionality by adding, editing, deleting topic and opinions. [🔗](https://docs.djangoproject.com/en/3.2/intro/tutorial02/#explore-the-free-admin-functionality)

9. Writing Views for **xapp**
    - Understand what is a view? [🔗](https://docs.djangoproject.com/en/3.2/intro/tutorial03/#overview)
    
    > In Django, web pages and other content are delivered by views. Each view is represented by a Python function (or method, in the case of class-based views). Django will choose a view by examining the URL that’s requested (to be precise, the part of the URL after the domain name).

    - Let's decide the Flow of the Project
        1. Home Page (index) - Displaying all topics (from Latest to oldest).
        2. Topic Page (topic) - It will display details of the Topic.
        3. Opinion Page (opinion) - It will display all the opinion related to the topic page.
        4. Votes action - Handles voting for a particular Opinion for a particular Topic. 

    - Adding views
    ```
    # xapp/views.py

    # Displays list of all topics.
    def index(request):
        # Display "Home Page"

    # Displays all details related to a specific topic.
    def topic(request, topic_id):
        # Captures topic_id from URL and displays topic_id.

    # Displays all details related to specific opinion
    def opinion(request, opinion_id):
        # Captures opinion_id from URL and displays opinion_id.

    # Vote action related to specific opinion
    def vote(request, opinion_id):
        # Captures opinion_id from URL and displays opinion_id.
    ```

    - Adding views to urls
    ```
    # xapp/urls.py

    urlpatterns = [
        # /xapp/
        path('', views.index, name='index'),

        # /xapp/topic/1/
        path('topic/<int:topic_id>/', views.topic, name='topic'),

        # /xapp/opinion/1/
        path('opinion/<int:opinion_id>/', views.opinion, name='opinion'),

        # /xapp/opinion/1/vote/
        path('opinion/<int:opinion_id>/vote', views.vote, name='vote')
    ]
    ```
    
    Once Url are saved, visit the different url defined.
    - http://127.0.0.1:8000/xapp/
    - http://127.0.0.1:8000/xapp/topic/5
    - http://127.0.0.1:8000/xapp/opinion/10
    - http://127.0.0.1:8000/xapp/opinion/9/vote

10. Writing Views that actually do something [🔗](https://docs.djangoproject.com/en/3.2/intro/tutorial03/#write-views-that-actually-do-something)  
    
    > Each view is responsible for doing one of two things: returning an HttpResponse object containing the content for the requested page or raising an exception.

    - Displaying all topics on Home Page (index)
        ```
        # xapp/views.py

        # Displays list of all topics.
        def index(request):
            # Update the logic to list down all topics from database
            # Retreiving all the topics order_by published_date. '-published_date' for descending order. 
            listOfTopic = Topic.objects.order_by('-published_date')
            output = '<br>'.join([ '"' + topic.title + '" published at ' + str(topic.published_date) for topic in listOfTopic])
            return HttpResponse(output)
        ```

        Now visit http://127.0.0.1:8000/xapp/ and observe a list of all topics displayed in descending order w.r.t published_date.
    
    - Using Django’s template system  
        > Your project’s TEMPLATES setting describes how Django will load and render templates. The default settings file configures a DjangoTemplates backend whose APP_DIRS option is set to True. convention, DjangoTemplates looks for a “templates” subdirectory in each of the INSTALLED_APPS.


        1. First create a 'templates' folder inside **xapp**.
        2. Create 'xapp' folder inside the 'templates' folder.
        3. Create an index.html inside 'xapp' folder.
            ```
            # xapp/templates/xapp/index.html
            
            # 'topics' will be sent from index() in views.py 
            {% if topics %}
                <ul>
                {% for topic in topics %}
                    <li><a href="/xapp/topic/{{ topic.id }}/">{{ topic.title }}</a></li>
                {% endfor %}
                </ul>
            {% else %}
                <p>No Topics are available.</p>
            {% endif %}
            ```
        4. Updating index in views.py to use the template
            ```
            # xapp/views.py

            from django.template import loader

            # Displays list of all topics.
            def index(request):
                # Retreiving all the topics order_by published_date. '-published_date' for descending order. 
                listOfTopic = Topic.objects.order_by('-published_date')
                
                # loading the lemplate
                template = loader.get_template('xapp/index.html')
                
                # context variable to be sent to view
                context = {
                    'topics' : listOfTopic
                }
                return HttpResponse(template.render(context, request))
            ```
            One more common practice to render a template is to use render()

            ```
            # xapp/views.py

            from django.shortcuts import render

            # Displays list of all topics.
            def index(request):
                ...
                return render(request, 'xapp/index.html', context)
            ```
        5. Raising a 404 Error  
            Let's define the topic() in views.py and display details on topic.html
            ```
            # xapp/views.py

            # Displays all details related to specific topic.
            def topic(request, topic_id):
                # Get details of topic with id = topic_id
                getDetailsOfTopic = Topic.objects.get(id=topic_id)
                context = {
                    'topic' : getDetailsOfTopic
                }
                return render(request, 'xapp/topic.html', context)
            ```
            ```
            # xapp/templates/xapp/topic.html
            
            # 'topics' will be sent from topic() in views.py
            <h1> {{ topic.title }} </h1>
            <p> Published at  {{ topic.published_date }} </p>
            ```
            Now visit, 
            1. http://127.0.0.1:8000/xapp/topic/1
            2. http://127.0.0.1:8000/xapp/topic/69   (Error will be thrown if topic_id=69 do not exist)

            To avoid any error page, we can add try..except block to catch an exception.  
            Updated topic() will be
            ```
            # xapp/views.py

            from django.http import Http404

            # Displays all details related to specific topic.
            def topic(request, topic_id):
                try:
                    # Get details of topic with id = topic_id
                    getDetailsOfTopic = Topic.objects.get(id=topic_id)
                    context = {
                        'topic' : getDetailsOfTopic
                    }
                except Topic.DoesNotExist:
                    # Raising 404 Error
                    raise Http404("Topic does not exist")
                return render(request, 'xapp/topic.html', context)
            ```
            Again visit the same url and observe changes.

            One more shortcut way to get object or 404 Error,
            ```
            # xapp/views.py

            from django.shortcuts import get_object_or_404

            # Displays all details related to specific topic.
            def topic(request, topic_id):
                # Get details of topic with id = topic_id
                getDetailsOfTopic = get_object_or_404(Topic, id=topic_id)
                context = {
                    'topic' : getDetailsOfTopic
                }
                return render(request, 'xapp/topic.html', context)
            ```
            Let's get all the related opinions related to the specific topic and display it on topic.html
            ```
            # xapp/templates/xapp/topic.html
            
            # 'topics' will be sent from topic() in views.py
            <h1> {{ topic.title }} </h1>
            <p> Published at  {{ topic.published_date }} </p>
            <ul>
            {% for opinion in topic.opinion_set.all %}
                <li>{{ opinion.opinion }}</li>
            {% endfor %}
            </ul>
            ```
            The above example shows, where we are fetching data in topic.html. This can also be done in topic() in views.py and send the result to topic.html

    - [HttpResponse](https://docs.djangoproject.com/en/3.2/ref/request-response/#django.http.HttpResponse)
    - [Settings-TEMPLATES](https://docs.djangoproject.com/en/3.2/ref/settings/#std:setting-TEMPLATES)
    - [Settings-APP_DIRS](https://docs.djangoproject.com/en/3.2/ref/settings/#std:setting-TEMPLATES-APP_DIRS)
    - [render()](https://docs.djangoproject.com/en/3.2/topics/http/shortcuts/#django.shortcuts.render)
    - [get_object_or_404](https://docs.djangoproject.com/en/3.2/topics/http/shortcuts/#django.shortcuts.get_object_or_404)
    - [Template Guide](https://docs.djangoproject.com/en/3.2/topics/templates/)

11. URLs in templates
    - Removing hardcoded URLs in templates [🔗](https://docs.djangoproject.com/en/3.2/intro/tutorial03/#removing-hardcoded-urls-in-templates)
        ```
        # xapp/templates/xapp/index.html
        
        <li><a href="/xapp/topic/{{ topic.id }}/">{{ topic.title }}</a></li>
        ```
        Since the above URL is hardcoded in templates, we will replace it with the `{% url %}` template tag.
        ```
        # xapp/templates/xapp/index.html
        
        # {% url '__named_url_in_xapp/urls.py__' __parameter__ %}
        <li><a href="{% url 'topic' topic.id %}">{{ topic.title }}</a></li>
        ```
        Using url template, changes made in url will be reflected wherever url has been used and user don't have to change individually in the respective template.

    - Namespacing URL names [🔗](https://docs.djangoproject.com/en/3.2/intro/tutorial03/#namespacing-url-names)  
        As we can observe in **xapp**-*urls* (in 9th Point), every URL has a structure starting with '/xapp/'. This can be improvised by setting 'app_name' to the application namespace.
        ```
        # xapp/urls.py

        app_name = 'xapp'

        urlpatterns = [
            # /xapp/
            path('', views.index, name='index'),

            # /xapp/topic/1/
            path('topic/<int:topic_id>/', views.topic, name='topic'),

            # /xapp/opinion/1/
            path('opinion/<int:opinion_id>/', views.opinion, name='opinion'),

            # /xapp/opinion/1/vote/
            path('opinion/<int:opinion_id>/vote', views.vote, name='vote')
        ]
        ``` 
        After updating **xapp**-*urls*, we have to update the hyperlink using the `{% url %}` template tag.
        ```
        # xapp/templates/xapp/index.html
        
        # {% url 'app_name:__named_url_in_xapp/urls.py__' __parameter__ %}
        <li><a href="{% url 'xapp:topic' topic.id %}">{{ topic.title }}</a></li>
        ```

11. Forms [🔗](https://docs.djangoproject.com/en/3.2/intro/tutorial04/#write-a-minimal-form)  
    Let's add HTML form to opinions page,
    ```
    # xapp/templates/xapp/opinion.html

    {% if error_message %}
        <p><strong>{{ error_message }}</strong></p>
    {% endif %}

    # Using Form with method POST and action set to url for vote defined in xapp/urls.py
    <form action="{% url 'xapp:vote' opinion.id %}" method="post">
        # To prevent Cross Site Request Forgeries
        {% csrf_token %}
        <label> Like the Opinion? Show support by voting</label>
        <input type="submit" id="{{ opinion.id }}" value="Vote">
    </form>
    ```
    Now, let’s create a Django view that handles the submitted data and does something with it. Remember, we created a URLconf for the xapp application that includes this line:
    ```
    # /opinion/1/vote/
    path('opinion/<int:opinion_id>/vote', views.vote, name='vote')
    ```
    We also created a dummy implementation of the vote() function. Let’s create a real version. Add the following
    ```
    # xapp/views.py

    # If method is "POST"
    if request.method =='POST':
        # Get the Opinion with opinion_id from URL, if present else throw 404 Error
        opinion = get_object_or_404(Opinion, pk=opinion_id)

        # If opinion_id from URL matched the data obtained from request.POST then validate the vote  
        if (int(request.POST['opinion-vote']) == opinion_id):
            # increment vote and save the updated votes
            ...

            # Always return an HttpResponseRedirect after successfully dealing
            # with POST data. This prevents data from being posted twice if a
            # user hits the Back button.
            return HttpResponseRedirect(reverse('xapp:opinion', args=(opinion_id, )))
        else:
            # Return to previous page with error message displayed
            return HttpResponseRedirect(render(request, 'xapp/opinion.html', {
                'opinion': opinion,
                'error_message': "Error encountered while registering your vote",
            }))
    else:
        # If method is other than "POST"
        return HttpResponse('Method Not allowed !')
    ```

    - [Django Tutorial Part 9: Working with forms
](https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Forms)
    - [ Avoiding race conditions using F()](https://docs.djangoproject.com/en/3.2/ref/models/expressions/#avoiding-race-conditions-using-f)

[🔗]()