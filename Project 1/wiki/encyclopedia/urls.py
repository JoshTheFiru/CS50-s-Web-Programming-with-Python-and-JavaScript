from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"), 
    path('wiki/<str:title>', views.entries, name="entries"), 
    path('search', views.search, name="search"),
    path('create', views.create, name="create"), 
    path('process_create', views.process_create, name="process_create")
]
