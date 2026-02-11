# File: D:/code/FlowGenAI/core/urls.py
from django.contrib import admin
from django.urls import path, include  # <--- Make sure 'include' is imported!

urlpatterns = [
    path('admin/', admin.site.urls),
    # This says: "Send any web traffic to the flow_generator app"
    path('', include('flow_generator.urls')), 
]