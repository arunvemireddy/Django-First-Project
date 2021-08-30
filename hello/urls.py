from django.urls import path
from hello import views


urlpatterns = [
    path("hello/<name>", views.hello_there, name="hello"),
    path("getdata", views.getdata, name="hello"),
]