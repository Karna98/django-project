# Django Project Setup

## Setup Project

1. Setup Virtual environment
    ```
    # OS:Windows
    # Terminal:Git Bash  
    virtualenv djangovenv
    ```  
2. Activate Virtual environment
    ```
    # OS:Windows
    # Terminal:Git Bash
    source djangovenv/Scripts/activate
    ```
3. Install Django [🔗](https://www.djangoproject.com/download/)
    ``` 
    # OS:Windows
    # Terminal:Git Bash
    pip3 install Django
    ```
4. Create Project with basic setup [🔗](https://docs.djangoproject.com/en/3.2/intro/tutorial01/#creating-a-project)
    ```
    # OS:Windows
    # Terminal:Git Bash
    django-admin startproject projectX
    ```
    Observe **projectX** is created.
    ```
    projectX/
        - manage.py
        - projectX/
            - __init__.py
            - settings.py
            - urls.py
            - asgi.py
            - wsgi.py
    ```
5.  To run the project on local server [🔗](https://docs.djangoproject.com/en/3.2/intro/tutorial01/#the-development-server)
    ```
    # OS:Windows
    # Terminal:Git Bash
    cd projectX
    python manage.py runserver
    ```
6. Create App (within Project) [🔗](https://docs.djangoproject.com/en/3.2/intro/tutorial01/#creating-the-polls-app)
    ```
    # OS:Windows
    # Terminal:Git Bash
    # App name is 'xapp'
    python manage.py startapp xapp
    ```
    Observe **xapp** is created.
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
    ```

    Basic Setup Completed !!

