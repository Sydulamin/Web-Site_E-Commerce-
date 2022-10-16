from django.urls import path
from . import views
from django.http import HttpResponse
urlpatterns = [

    # path("blog/",views.index,name="blog"),
    path("",views.index,name="blog"),

    # path("",views.index,name="shopHome"),
]
