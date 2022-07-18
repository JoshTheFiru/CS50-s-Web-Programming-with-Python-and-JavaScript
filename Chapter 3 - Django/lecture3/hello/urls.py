from django.urls import path

from hello import views         #. means the same directory where we are placed

urlpatterns = [
    path('', views.index, name="index"),
    path('<str:name>', views.greet, name="greet")               #str:name represents a parametrized URL
]