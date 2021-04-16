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
        .
        .
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

[🔗]()