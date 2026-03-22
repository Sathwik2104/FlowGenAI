# File: D:/code/FlowGenAI/flow_generator/urls.py
from django.urls import path
from . import views

urlpatterns = [
    # Landing page for unauthenticated users
    path('', views.landing_page_view, name='landing'),
    
    # Main application route
    path('app/', views.home, name='home'),
    
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    
    # Profile & Account Management
    path('profile/', views.profile_view, name='profile'),
    path('profile/delete/', views.delete_account_view, name='delete_account'),
    
    # Flow Deletion
    path('delete_flow/<int:flow_id>/', views.delete_flow_view, name='delete_flow'),
    path('delete_all_flows/', views.delete_all_flows_view, name='delete_all_flows'),
]