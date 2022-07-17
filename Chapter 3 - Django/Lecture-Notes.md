# CHAPTER 3 - Django

## Web applications

Django is a Python web framework. which will allow, through Python, dynamically generate HTML and CSS, allowing to build a dynamic web application.

## HTTP

HyperText Transfer Protocol. We are going to write Django web applications that will run on a server, and the users, who are the clients, will be making requests to that server. Once the server process the request, will return some sort of response. That request might look something like:

    GET / HTTP/1.1
    Host:www.example.com
    ...

When the server process this request, will get back with a response, which will look generally like:

    HTTP/1.1 200 OK
    Contente-type: text/html
    ...

Some of the more popular status code would be:

|STATUS CODE | Description |
|------------|-------------|
|    200     |      OK     |
|    301     | Moved Permanently   |
|    403     | Forbidden   |
|    404     | Not Found   |
|    500     | Internal Server Error  |

## Django

Django is a web framework. It's a set of tools that is already built for us, making it easy to get started by writing. It brings to the table basic features all web pages have to do in order we can focus in building interesting logic for our web applications without needing to worry too much about rutinary stuff.

Once Django is installed through pip by stating in the terminal:

    pip3 install Django

Once install, you can write a command to start a Django project, which looks like:

    django-admin startproject PROJECT_NAME

This will create all the file structure to build a new web application.

- The file *manage.py* will be used to be able to execute commands on the Django project of its own.
- Another important file created is the *settings.py* which contains important configuration settings for the Django application.
- *urls.py* is a sort of table of contents for our web application that will store all of the urls of the web application that you can visit.

To be able to run the application created, once in the path of the folder:

    python manage.py runserver

What it creates is a Django project. Normally, a Django project consist of one or multiple Django applications. The reason for this is, if you think of big websites, they are a sort of separate service that operate within it. So Django comes with this ability to take a project and divide it into multiple distintc apps.

So to start after creating the project, is to create a Django app, by going to the terminal and stating:

    python manage.py startapp APP_NAME


