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

So the way to start after creating the project, is to create a Django app, by going to the terminal and stating:

    python manage.py startapp APP_NAME

This will create the file structure necessary to build and run a Django web app.

Among those files, *views.py* is the file that lets us describe what it is the user sees when they visit a particular route, for example, where we can decide what gets rendered to the user.

## Routes

First of all, we add the hello app to the INSTALLED_APPS variable in [settings.py](lecture3/lecture3/settings.py).

Now, in the hello folder, in the [views.py](lecture3/hello/views.py) file, we create a view for the user to see.

From here is where we now begin to create some URL configuration, some sort of setting that tell Django when a particular URL is visited, this function created in the *views.py* should be run in order to return that particular HTTP response.

In order to do that, we need to create a [urls.py](lecture3/hello/urls.py) file for this particular app. Django has a *urls.py* file for the entire project, but in order to not to mess things up, sometimes we need to create a new *urls.py* file in the separate application.

The last step for this artifact to be able to run is to go into the lecture3 directory and open [urls.py](lecture3/lecture3/urls.py), which is the one for all of the apps that might be contained within this project and add the "global" path for the hello application, saying it something like link all its own app urls into a main global url. Something like "*Inside of the hello module, get all the urls file there.*"

The advantage of these mechanisms is that you can parametrize de URLs by using placeholders, so with one function you can for example, personalize a url depending on the user that gets into your application.

## Templates

Templates are the way to introduce the HTML views that we need for our application. So in the *urls.py* file, instead of returning HttpResponses, on the definition of the function that return the view, you will say:

    def index(request):
        return render(request, "TEMPLATE_NAME")

And this is what **templates** are usefull for. They let us write HTML and CSS (like the "frontend") for our app, and that be rendered once the user visits certain URL. Furthermore, this templates can be rendered and receive data from Django, so variables can be passed once they render in order to personalize the views for a user or a feature in specific.

All this can seem like to many files to handle, but is just for the purpose of keeping things apart one from another. Modularity is one of the key benefits of Django, and once you understand the data flow, things become very poweful.

Now, if we wanted to introduce some CSS, Django has a way to introduce static files. For example, the conditional HTML will not be a static file, because it will render different things depending on the request we are sending it. But you can think that does not matter which HTML is rendering, the CSS will style the same tags, so can be considered static.

So for Django to deal with these static files, inside of the app folder, we create a new folder called static that will contain all the static files that we would like to include in this application. Then, as we did with templates, we need to create another new folder with the app name.

Once finished creating the static files, into the HTML where you want to "load" the static file(s), add the Django insertions:

    {% load static %}

and now go ahead and link a style sheet as you would normally do, with some exception which is to insert the href as a Django variable:

    <link href="{% static 'folderName/fileName.css' %}" rel="stylesheet">

In Django, we have the ability to use something called template inheritance. So you can create a parent HTML as kind of a layout, and let another HTMLs which are similar in content, inherit from that in order to no redudant the code and make ir more manteinable.

## Forms

To prevent CSRF (Croos-Site Request Forgery), Django has by default an add-on called Django Middleware which is able to prevent attacks like these and protect forms that contain sensitive content. This software is able to intervene in the request response processing of a Django request. You can check all the middle ware available by default when creating a project, in [setings.py](settings.py), stored in the MIDDLEWARE variable.

Its a must to remember, that this middleware will interfere if the form sends data via a **POST REQUEST**, which is meant to change the state of the application in some way, that we need to have a CSRF validation. So what this does is to create a token to the form to make sure that Django is able to authenticate the validity of this form.

Django has added a number of ways to make it easier to create forms, to validate the data inside of those forms to make the programmers lives a little bit easier when it comes to dealing with and interacting with forms.
You can see how to make use of this feature in the [tasks/views.py](tasks/views.py) example.

Apart from these, and the client-side validation of the data, Django also has features that provide facility to make use of server-side validation that we probably will need in our forms.

## Sessions

For mantaining data from user secured from other users, we should never be using a global variable or data structure to store data from the application, does not matter if it is sensitive or not, as it will create malfunctioning for users.

Imagining a to-do app, one user won't want to add a new task and that be mixed with tasks from another user. That's why we will need sessions.

In order to get advantage of sessions, you can check [views.py](tasks/views.py) to see how they are used to store a user list of tasks in their own session.

To be able to store session data for users, we will need to migrate data into a database (we will see this display in Chapter 4. For now, what we need to write in the terminal to make sessions work is:

    python manage.py migrate
