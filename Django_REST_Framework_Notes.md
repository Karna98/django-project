# Notes

Before Starting, read the article about [Best Coding Practices For Rest API Design](https://www.geeksforgeeks.org/best-coding-practices-for-rest-api-design/)

Link : [Django REST Framework](https://www.django-rest-framework.org/)

Preview of what we have set up in Django Project 
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
    
    A Topic can have multiple opinions and each opinion has a total no of votes.
```
On the above premise let's build a REST API's using Django REST Framework.

1. Let's first decide the endpoints of API's we have to work on.

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
    Since we have defined what will be our endpoints and URLs, let's proceed with coding.

2. Create new file **urls.py** and **serializers.py** in **apix**. [🔗](https://www.django-rest-framework.org/tutorial/1-serialization/#tutorial-1-serialization)
    ```
    - urls.py 
        1. In this file we will list all endpoints.
    - serializers.py 
        1. In this file we will define serialization and validation of objects(data) to be sent as a response or received over request.  
        2. Serialization means converting an object to JSON format and Deserialization is vice versa of Serialization.
    ```

3. Hook **apix** to **projectX**  
    For **projectX** to recognize that there are REST API's created using the REST framework, we need to add 'rest_framework' to INSTALLED_APPS.
    ```
    # projectX/settings.py

    INSTALLED_APPS = [
        ...
        'rest_framework',
    ]
    ```

4. Now let's start with writing serializers with `ModelSerializers`
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
        # List all topics or create a new topic.
    
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
    1. For List View, it will display all the topic using **GET** Method and also we can create a new topic using **POST** Method.
    2. For Detail View, it will capture `id` or `pk` from URL and related to specific `id` will display topic using **GET** Method or update details of the topic using **PUT** Method or delete topic using **DELETE** Method.

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

    Although we have defined URL's in `projectX/xapp/apix/urls.py`, the root URL is still unaware of the new URLs defined. So we need to include URLs in `projectX/urls.py`.
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

7. Requests and Responses [🔗](https://www.django-rest-framework.org/tutorial/2-requests-and-responses/)  
    - Request objects
        ```
        request.POST  # Only handles form data.  Only works for 'POST' method.
        request.data  # Handles arbitrary data.  Works for the 'POST', 'PUT' and 'PATCH' methods.
        ```
    - Response objects
        ```
        return Response(data)  # Renders to content type as requested by the client.
        ```
    - [Status codes](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status)

8. Wrapping API views [🔗](https://www.django-rest-framework.org/tutorial/2-requests-and-responses/#wrapping-api-views)
    > REST framework provides two wrappers you can use to write API views.  
        1. The `@api_view` decorator for working with function-based views.  
        2. The APIView class for working with class-based views.
    
    ```
    # projectX/xapp/apix/views.py

    from django.views.decorators.csrf import api_view

    @api_view(['GET', 'POST'])
    def topic_list(request):
        # List all topics, or create a new topic.
        # Method Defined for 'GET', 'POST' 

    @api_view(['GET', 'PUT', 'DELETE'])
    def topic_detail(request, pk):
        # Retrieve, update or delete a topic.
        # Method Defined for 'GET', 'PUT', 'DELETE'
    ```
    Try to remove 'GET' from the list of allowed method and observe the response.

9. Rewriting our API using class-based views [🔗](https://www.django-rest-framework.org/tutorial/3-class-based-views/#rewriting-our-api-using-class-based-views)
    - Rewriting our API using class-based views
        ```
        # projectX/xapp/apix/views.py

        # Class To be linked in urls.py
        class TopicList(APIView):
            # Each class contains different types of views
            def get(self, request):
                topics = Topic.objects.all()
                serializer = TopicSerializer(topics, many=True)
                return Response(serializer.data, safe=False)

            def post(self, request):
                serializer = TopicSerializer(data=request.data)
                if serializer.is_valid():
                    serializer.save()
                    return Response(serializer.data, status=status.HTTP_201_CREATED)
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        ```
        and 
        ```
        # projectX/xapp/apix/urls.py

        urlpatterns = [
            path('topics/', TopicList.as_view()),
        ]
        ```
        - [Using mixins](https://www.django-rest-framework.org/tutorial/3-class-based-views/#using-mixins)
        - [Using generic class-based views](https://www.django-rest-framework.org/tutorial/3-class-based-views/#using-generic-class-based-views)

10. Authentication & Permissions [🔗](https://www.django-rest-framework.org/tutorial/4-authentication-and-permissions/#tutorial-4-authentication-permissions)
    Refer to this link to understand how it works.

11. Creating an endpoint for the root of our API [🔗](https://www.django-rest-framework.org/tutorial/5-relationships-and-hyperlinked-apis/#creating-an-endpoint-for-the-root-of-our-api) 
    Refer to this link to understand how it works.

12. Refactoring to use ViewSets [🔗](https://www.django-rest-framework.org/tutorial/6-viewsets-and-routers/#refactoring-to-use-viewsets)
    - Using ViewSet,
        ```
        # projectX/xapp/apix/views.py

        class TopicViewSet(viewsets.ReadOnlyModelViewSet):
            """
            This viewset automatically provides `list` and `retrieve` actions.
            """
            queryset = Topic.objects.all()
            serializer_class = TopicSerializer

        class TopicDetailViewSet(viewsets.ModelViewSet):
            """
            This viewset automatically provides `list`, `create`, `retrieve`,
            `update` and `destroy` actions.
            """
            lookup_field = 'pk'
            queryset = Topic.objects.all()
            serializer_class = TopicSerializer
        ```
    - [Binding ViewSets to URLs explicitly](https://www.django-rest-framework.org/tutorial/6-viewsets-and-routers/#binding-viewsets-to-urls-explicitly)
        ```
        # projectX/xapp/apix/urls.py

        urlpatterns = [
            path('topics/',
                TopicViewSet.as_view({
                    'get': 'list'
                }),
                name='topic-list'
            ),
            path('topics/<int:pk>/',
                TopicDetailViewSet.as_view({
                    'get': 'retrieve',
                    'post': 'create',
                    'patch': 'partial_update',
                    'delete': 'destroy'
                }),
                name='topic-detail'
            ),
        ]
        ```
    - [Using Routers](https://www.django-rest-framework.org/tutorial/6-viewsets-and-routers/#using-routers)
        ```
        # projectX/xapp/apix/urls.py

        from rest_framework.routers import DefaultRouter

        # Create a router and register our viewsets with it.
        router = DefaultRouter()
        router.register(r'topics',TopicDetailViewSet)

        urlpatterns = [
            path('', include(router.urls)),
        ]
        ```
    Now visit all the Endpoints and check if it works.

    > **Trade-offs between views vs viewsets**  
        1. Using viewsets can be a really useful abstraction. It helps ensure that URL conventions will be consistent across your API, minimizes the amount of code you need to write, and allows you to concentrate on the interactions and representations your API provides rather than the specifics of the URL conf.   
        2. That doesn't mean it's always the right approach to take. There's a similar set of trade-offs to consider as when using class-based views instead of function based views. Using viewsets is less explicit than building your views individually.

In this part, we dealt with the Topic table only. Implement all the Endpoints described at the start can be extended as part of learning and practice.