from django.contrib import admin
from django.urls import path
from faleeapp import views

urlpatterns = [path('', views.Churn_rate, name='Churn_rate'),]
