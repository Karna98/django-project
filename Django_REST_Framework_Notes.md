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
    Since we have defined what will be our endpoints and urls, lets proceed with coding
2. 