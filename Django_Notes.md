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
    Here we will be creating two tables named "Topics" and "Opinions".  
    - **Topics**
        - Title of Topic
        - Date Published
    - **Opinions**
        - Related to which original topic
        - Opinion
        - No. of votes

    ```
    # xapp/models.py
    
    class Topics(models.Model):
        # Define different fields for 'Topics' table.

    class Opinions(models.Model):
        # Define different fields for 'Opinions' table.
    ```

    - [Models](https://docs.djangoproject.com/en/3.2/topics/db/models/)
    - [Field Types](https://docs.djangoproject.com/en/3.2/ref/models/fields/#field-types)
6. Activating models [🔗](https://docs.djangoproject.com/en/3.2/intro/tutorial02/#activating-models)  
    To include **xapp** in **projectX**, we need to add refrence to its configuration class in INSTALLED_APPS setting.
    ```
    # projectX/settings.py
    
    INSTALLED_APPS = [
        'django.contrib.admin',
        . . .
        'xapp.apps.XappConfig'
    ]

    ```
    
    Once the 'projectX' about 'xapp' config, lets migrate the models of 'xapp' by running following command
    ```
    $ python manage.py makemigrations xapp
    ```

    To check what SQL that migration would run, 
    ```
    # here 0001, considering 'xapp/migrations/0001_initial.py'
    
    $ python manage.py sqlmigrate xapp 0001
    ```

    Finally to create the models in database, run
    ```
    $ python manage.py migrate
    ```
    'xapp_topics' and 'xapp_opinions' can be seen in database.

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
    Lets open Python shell,
    ```
    $ python manage.py shell
    ```

    Once python shell opens, lets execute following commands
    - Import the model classes we just wrote
    ```
    >>> from xapp.models import Topics, Opinions
    ```
    - Retrive all Topics
    ```
    >>> Topics.objects.all()
    ```
    - Insert a new topic in DB
    ```
    >>> from django.utils import timezone
    
    # Create a new Topic
    >>> newTopic = Topics(title="Title 1", published_date=timezone.now())

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
    >>> Topics.objects.all()
    # Output : <QuerySet [<Topics: Topics object (1)>]>  
    ``` 

    Observe the Output of last query. was it any helpful ? **NO**  
    Lets fix by modiying the output in *xapp/models.py*

    To get the output as desired,
    ```
    # xapp/models.py
    
    class Topics(models.Model):
        . . .
        # Defining desired output by modifying __str__().
        def __str__(self):
            return '{ Title : "' + self.title + '", Published Date : "' + str(self.published_date) + '" }'

    class Opinions(models.Model):
        . . .
        # Defining desired output  by modifying __str__().
        def __str__(self):
            return return '{ Opinion : "' + self.opinion + '", Votes : "' + str(self.votes) + '" }'
    ```

    Lets also add custom method, 
    ```
    # xapp/models.py
    
    class Topics(models.Model):
        . . .
        # Custom Method : How old is title (published)?
        def published_ago(self):
            return current_date - published_date
    ```

    Lets test above added methods,
    ```
    >>> from django.utils import timezone
    >>> from xapp.models import Topics, Opinions
    
    # See all the topics with new modified __str__()
    >>> Topics.objects.all()
    # <QuerySet [<Topics: { Title : "Title 1", Published Date : "2021-04-16 19:17:20.814756+00:00" }>, <Topics: { Title : "Title 1.1", Published Date : "2021-04-17 16:56:01.784471+00:00" }>]>

    # Testing custom function published_ago() 
    >>> topic = Topics.objects.get(id=1)
    >>> topic.published_ago()
    # Output : datetime.timedelta(seconds=75129, microseconds=618923)

    # Get Topic with id = 1
    >>> Topics.objects.get(id=1)
    # Output : <Topics: { Title : "Title 1", Published Date : "2021-04-16 19:17:20.814756+00:00" }>

    # Get Topic with invalid id = 4
    >>> Topics.objects.get(id=4)
    # Output : Traceback (most recent call last):
    #          ...
    #          xapp.models.Topics.DoesNotExist: Topics matching query does not exist.

    # Get Topic published today (i.e. on 17-04-2021)
    >>> Topics.objects.get(published_date__date='2021-04-17')
    # Output : <Topics: { Title : "Title 1.1", Published Date : "2021-04-17 16:56:01.784471+00:00" }>

    # Get Topic with pk = 1 (pk is primary key)
    >>> Topics.objects.get(pk=1)
    # Output : <Topics: { Title : "Title 1", Published Date : "2021-04-16 19:17:20.814756+00:00" }>

    # Get Published Date of newTopic inserted
    >>> newTopic.published_date
    # Output : datetime.datetime(2021, 4, 16, 19, 44, 32, 177653, tzinfo=<UTC>)

    # Using Filters 
    >>> Topics.objects.filter(id=2)
    # Ouptut : <QuerySet [<Topics: { Title : "Title 1.1", Published Date : "2021-04-17 16:56:01.784471+00:00" }>]>
    >>> Topics.objects.filter(title__startswith='Title')
    # Output : <QuerySet [<Topics: { Title : "Title 1", Published Date : "2021-04-16 19:17:20.814756+00:00" }>, <Topics: { Title : "Title 1.1", Published Date : "2021-04-17 16:56:01.784471+00:00" }>]>
    
    # Get Opinions related to Topic with id=1
    >>> topic = Topics.objects.get(id=1)
    # Display any opinion from the related object set -- none so far.
    >>> topic.opinions_set.all()
    # Output : <QuerySet []>

    # Let's create 3 opinions
    >>> topic_one = Topics.objects.get(id=1)
    >>> topic_one.opinions_set.create(opinion="Opinion 1 related to Topic Title 1", votes=1)
    # Output : <Opinions: { Opinion : "Opinion 1 related to Topic Title 1", Votes : "1" }>
    >>> topic_two = Topics.objects.get(id=2)   
    >>> topic_two.opinions_set.create(opinion="Opinion 1 related to Topic Title 1.1", votes=0)
    # Output : <Opinions: { Opinion : "Opinion 1 related to Topic Title 1.1", Votes : "0" }>
    >>> topic_two.opinions_set.create(opinion="Opinion 2 related to Topic Title 1.1", votes=5)
    # Output : <Opinions: { Opinion : "Opinion 2 related to Topic Title 1.1", Votes : "5" }>

    # objects.all() displays all the opinions in the database.
    >>> Opinions.objects.all()
    # Output : <QuerySet [<Opinions: { Opinion : "Opinion 1 related to Topic Title 1", Votes : "1" }>, <Opinions: { Opinion : "Opinion 1 related to Topic Title 1.1", Votes : "0" }>, <Opinions: { Opinion : "Opinion 2 related to Topic Title 1.1", Votes : "5" }>]>

    >>> topic_one.opinions_set.all()
    # Output : <QuerySet [<Opinions: { Opinion : "Opinion 1 related to Topic Title 1", Votes : "1" }>]>
    >>> topic_two.opinions_set.all()
    # Output : <QuerySet [<Opinions: { Opinion : "Opinion 1 related to Topic Title 1.1", Votes : "0" }>, <Opinions: { Opinion : "Opinion 2 related to Topic Title 1.1", Votes : "5" }>]>

    >>> topic_one.opinions_set.count()
    # Output : 1
    >>> topic_two.opinions_set.count()
    # Output : 2

    # Get opinions which are related to topic published on date '2021-04-17'
    >>> Opinions.objects.filter(topic__published_date__date='2021-04-17')
    # Output : <QuerySet [<Opinions: { Opinion : "Opinion 1 related to Topic Title 1.1", Votes : "0" }>, <Opinions: { Opinion : "Opinion 2 related to Topic Title 1.1", Votes : "5" }>]>

    # Let's delete one of the opinion which starts with "Opinion 2"
    >>> opinion_two = topic_two.opinions_set.filter(opinion__startswith='Opinion 2')
    >>> opinion_two.delete()
    # Output : (1, {'xapp.Opinions': 1})
    ```

    - [Database Queries API](https://docs.djangoproject.com/en/3.2/topics/db/queries/)
    - [__str __()](https://docs.djangoproject.com/en/3.2/ref/models/instances/#django.db.models.Model.__str__)
    - [Timezones](https://docs.djangoproject.com/en/3.2/topics/i18n/timezones/)
    - [ Accessing related objects](https://docs.djangoproject.com/en/3.2/ref/models/relations/)
    - [Field lookups](https://docs.djangoproject.com/en/3.2/topics/db/queries/#field-lookups-intro)

[🔗]()