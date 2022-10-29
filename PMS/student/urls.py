
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.homepage),
    path('/index',views.index),
    path('student/',views.studentpage),
    path('company/',views.Companydetails)
]
