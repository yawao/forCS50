from django.urls import path
# Indicate to use views
from . import views

urlpatterns = [
    path("", views.index, name="index"), #views means views.py, and index means function that you want to call when visiting url
    path("yuki", views.yuki, name ="yuki"),
    path("asai", views.asai, name ="asai"),
    path("<str:name>", views.greet, name="greet")
]