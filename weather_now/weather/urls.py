from django.urls import path
from .views import home_view, deleteAll

urlpatterns = [
    path('', home_view, name = "home"),
    path('deleteAll/', deleteAll, name= "deleteAll"),
]
