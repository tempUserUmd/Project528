from django.urls import path
from . import views

appname = "main"


urlpatterns = [ path('route', views.route, name="route"),
    path('map', views.map, name="map"),
]