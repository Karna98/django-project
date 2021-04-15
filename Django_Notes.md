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
[🔗]()