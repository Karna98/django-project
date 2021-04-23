# Notes

Before Starting, read article about [Best Coding Practices For Rest API Design](https://www.geeksforgeeks.org/best-coding-practices-for-rest-api-design/)

Link : [Django REST Framework](https://www.django-rest-framework.org/)

Preview of what we have setup in Django Project 
```
    In Django, we set up **projectX** and hook an application **xapp**.
    xapp is simple application which has following models
    - Topic :  
        - id (default)
        - title
        - published date 
    - Opinion
        - id (default)
        - title (foreign key)
        - opinion
        - votes 
    
    Topic can have multiple opinions and each opinion has total no of votes.
```
On above premise let's build an REST API's using Django REST Framework.

1. Lets first decide endpoints of API's we have to work.

    | EndPoints | Method | Description |
    | --------- | ------ | ----------- |
    | */topics* | GET | Displays all the topics (latest to oldest) |
    | */topics/{**id**}* | GET | Display details of topic with ID = `id` |
    | */topics/create* | POST | Create new topic |
    | */topics/{**id**}/update* | PUT | Update topic with ID = `id` |
    | */topics/{**id**}/delete* | DELETE | Delete topic with ID = `id` |
    | */opinions* | GET | Displays all the opinions |
    | */opinions/{**id**}* | GET | Display details of  opinion with ID = `id` |
    | */opinions/create* | POST | Create new opinion |
    | */opinions/{**id**}/update* | PUT | Update opinion with ID = `id` |
    | */opinions/{**id**}/delete* | DELETE | Delete opinion with ID = `id` |
    | */topics/{**id**}/opinions* | GET | Display all opinions related to topic with ID = `id` |
    | */opinions/{**id**}/topic* | GET | Display topic related to opinion with ID = `id` |

    We are going to set base URL as ***apix/***. So every URL will look like ***/apix/endpoint_described_above***.    
    Since we have defined what will be our endpoints and urls, lets proceed with coding.

2. Create new file **urls.py** and **serializers.py** in **apix**.
    ```
    - urls.py 
        1. In this file we will list all endpoints.
    - serializers.py 
        1. In this file we will defined serialization and validation of objects(data) to be send as response or received over request.  
        2. Serialization means converting object to JSON format and Deserialization is vice versa of Serialization.
    ```

3. Hook **apix** to **projectX**  
    For **projectX** to recognize that there are REST API's created using REST framework, we need to add 'rest_framework' to INSTALLED_APPS.
    ```
    # projectX/settings.py

    INSTALLED_APPS = [
        ...
        'rest_framework',
    ]
    ```

4. Now lets start with writing serializers with `ModelSerializers`
    ```
    # projectX/xapp/apix/serializers.py

    from ..models import {Model_Name}
    from rest_framework import serializers

    # Serializer Class for Model {Model_Name}
    class {Model_Name}Serializer(serializers.ModelSerializer):
        class Meta:
            model = {Model_Name}
            # Fields to be validated or serialized (can be all or partial fields from Model)
            fields = [
                {Fields_Present_in_Model}
            ]
    ```
    To test Serializers created (TopicSerializer),
    ```
    # In projectX directory, execute
    $ python manage.py shell

    >>> from xapp.apix.serializers import TopicSerializer, OpinionSerializer
    >>> from xapp.models import Topic, Opinion
    >>> from django.utils import timezone
    >>> from rest_framework.renderers import JSONRenderer

    # Create New Topic
    >>> newTopic = Topic(title="Testing Serializers", published_date=timezone.now())
    >>> newTopic
    # Output : <Topic: { Title : "Testing Serializers", Published Date : "2021-04-23 15:31:31.675606+00:00" }>
    
    # Save New Topic
    >>> newTopic.save()

    # Serialized New Topic using TopicSerializer
    >>> serializedNewTopic = TopicSerializer(newTopic)
    >>> serializedNewTopic
    # Output : TopicSerializer(<Topic: { Title : "Testing Serializers", Published Date : "2021-04-23 15:31:31.# 675606+00:00" }>):
    #           id = IntegerField(label='ID', read_only=True)
    #           title = CharField(max_length=200)
    #           published_date = DateTimeField(label='Date published')
    
    >>> serializedNewTopic.data
    # Output :{'id': 8, 'title': 'Testing Serializers', 'published_date': '2021-04-23T15:31:31.675606Z'}

    # To finalise the serialization process we render the data into json
    >>> serializedNewTopicRendered = JSONRenderer().render(serializedNewTopic.data)
    >>> serializedNewTopicRendered
    # Output : b'{"id":8,"title":"Testing Serializers","published_date":"2021-04-23T15:31:31.675606Z"}'
    ```
    - [Serializers](https://www.django-rest-framework.org/api-guide/serializers/)

5. Writing Django Views using Serializers  
    ```
    # projectX/xapp/apix/views.py

    def topic_list(request):
        # List all topics, or create a new topic.
    
        if request.method == 'GET':
            ...
        elif request.method == 'POST':
            ...

    def topic_detail(request, pk):
        # Retrieve, update or delete a topic.
        
        try:
            topic = Topic.objects.get(pk=pk)
        except Topic.DoesNotExist:
            return HttpResponse(status=404)

        if request.method == 'GET':
            ...
        elif request.method == 'PUT':
            ...
        elif request.method == 'DELETE':
            ...
    ```
    In the above layout, we have defined two views viz. list and detail view.
    1. For List View, it will display all the topic using **GET** Method and also we can create an new topic using **POST** Method.
    2. For Detail View, it will capture `id` or `pk` from URL and related to specific `id` will display topic using **GET** Method or update details of topic using **PUT** Method or delete topic using **DELETE** Method.

6. Defining URLs
    ```
    # projectX/xapp/apix/urls.py

    from .views import topic_list, topic_detail 

    urlpatterns = [
        path('topics/', topic_list),
        path('topics/<int:pk>/', topic_detail),
    ]
    ```
    Here, we have 2 endpoints `apix/topics/` and `apix/topics/{id}`

    Althought we have defined URL's in `projectX/xapp/apix/urls.py`, but the root URL is still unaware of the new URLs defined. So we need include URL's in `projectX/urls.py`.
    ```
    # projectX/urls.py

    urlpatterns = [
        ...
        # Hooking apix
        path('apix/', include('xapp.apix.urls')),
    ]
    ```
    Then execute runserver command,
    ```
    $ python manage.py runserver
    ```
    Once the server is running, visit 
    1. http://127.0.0.1:8000/apix/topics
    2. http://127.0.0.1:8000/apix/topics/1
