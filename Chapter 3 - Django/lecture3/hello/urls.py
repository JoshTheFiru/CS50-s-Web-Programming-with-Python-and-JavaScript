from django.urls import path

from . import views         #. means the same directory where we are placed

urlpattterns = [
    path("", views.index, name="index")     #when some visits the default (empty) route, run the index function in the views.py file
]