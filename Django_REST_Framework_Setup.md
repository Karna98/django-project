# Django REST Framework Setup

## Setup REST Framework

We are building REST API's on [Django Project-*projectX*](Django_Notes.md) for **projectX**-**xapp**

1. Activate virtualenv we created previously.
    ```
    # OS:Windows
    # Terminal:Git Bash
    
    $ source djangovenv/Scripts/activate
    ```
2. Install Django REST Framework
    ```
    # OS:Windows
    # Terminal:Git Bash
    
    $ pip3 install djangorestframework 
    ```
3. Let's create a new app name **apix** (API - X) within **xapp** of **projectX**.
    ```
    # OS:Windows
    # Terminal:Git Bash
    # App name is 'apix'
    
    $ cd projectX/xapp
    $ python manage.py startapp apix
    ```
    Observe **apix** is created.
    ```
    projectX/
        - manage.py
        - projectX
        - xapp
            - __init__.py
            - admin.py
            - apps.py
            - migrations/
                - __init__.py
            - models.py
            - tests.py
            - views.py
            - apix/
                - __init__.py
                - admin.py
                - apps.py
                - migrations/
                    - __init__.py
                - models.py
                - tests.py
                - views.py
    ```
    We are ready to implement our REST APIs using Django REST Framework. 