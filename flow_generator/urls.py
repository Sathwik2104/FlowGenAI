# File: D:/code/FlowGenAI/flow_generator/urls.py
from django.urls import path
from . import views

urlpatterns = [
    # This says: "If someone goes to the homepage, show the 'home' view"
    path('', views.home, name='home'),
]