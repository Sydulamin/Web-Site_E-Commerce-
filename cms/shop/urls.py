from django.urls import path
from . import views
from django.http import HttpResponse

urlpatterns = [

    path("",views.index,name="shopHome"),
    path("about/",views.index,name="AboutUs"),
    path("contact/",views.contact,name="ContactUs"),
    path("tracker/",views.tracker,name="TrackingStatus"),
    path("search/",views.search,name="search"),
    path("productView/",views.prodView,name="search"),
    path("Checkout/",views.checkout,name="search"),

]
