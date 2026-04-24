from django.urls import path
from . import views

app_name = 'trainapp'

urlpatterns = [
    # Add your URL patterns here
    path('',views.Main,name='index')
]