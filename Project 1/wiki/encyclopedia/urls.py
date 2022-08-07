from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"), 
    path('wiki/<str:title>', views.entries, name="entries"), 
    path('search', views.search, name="search"),
    path('create', views.create, name="create"), 
    path('process_create', views.process_create, name="process_create"), 
    path('edit_content?content=<str:content>', views.edit, name="edit_content"), 
    path('process_edit?content<str:content>', views.process_edit, name="process_edit"), 
    path('random', views.random, name="random")
]
