from django.urls import path
from app1 import views 

urlpatterns = [
    path("",views.v1_inicio),
    path("v2/",views.v2_inicio),
]