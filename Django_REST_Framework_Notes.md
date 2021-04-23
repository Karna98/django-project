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

    # Serializer Class for Model Topic
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