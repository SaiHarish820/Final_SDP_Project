from django.contrib import admin
from django.urls import path
from .import views

urlpatterns = [
     path("", views.index, name='home'),
     path("participate", views.participate),
     path("categories", views.categories),
     path("createbid",views.createbid),

]
