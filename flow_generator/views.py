# flow_generator/views.py
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Flow
from .utils import get_gemini_flow

def landing_page_view(request):
    """
    Landing page for unauthenticated users.
    Redirects to the main app if already authenticated.
    """
    if request.user.is_authenticated:
        return redirect('home')
    return render(request, 'landing.html')

@login_required
def home(request):
    generated_content = None #initial value
    
    # Check if loading a specific history item
    flow_id = request.GET.get('flow_id')
    if flow_id:
        try:
            flow = Flow.objects.get(id=flow_id, user=request.user)
            generated_content = flow.content
        except Flow.DoesNotExist:
            pass

    if request.method == "POST":   # if the request method is post
        topic = request.POST.get('topic') # get the topic from the request
        if topic:
            # 1. Call AI
            generated_content = get_gemini_flow(topic)
            
            # 2. Save to Database
            flow = Flow.objects.create(user=request.user, topic=topic, content=generated_content)
            
            # Post/Redirect/Get pattern to avoid duplicate submissions on refresh
            from django.urls import reverse
            return redirect(f"{reverse('home')}?flow_id={flow.id}")

    # 3. Show past history
    recent_flows = Flow.objects.filter(user=request.user).order_by('-created_at')[:10]

    # 4. Render the template
    return render(request, 'home.html', { 
        'generated_content': generated_content,
        'recent_flows': recent_flows
    })

def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('landing')

@login_required
def profile_view(request):
    if request.method == 'POST':
        user = request.user
        user.first_name = request.POST.get('first_name', '')
        user.last_name = request.POST.get('last_name', '')
        user.email = request.POST.get('email', '')
        # Optional: check if username is unique if changing it, but keeping it simple.
        new_username = request.POST.get('username')
        if new_username and new_username != user.username:
            if not User.objects.filter(username=new_username).exists():
                user.username = new_username
            else:
                messages.error(request, "Username is already taken.")
                return render(request, 'profile.html', {'user': user})
                
        user.save()
        messages.success(request, "Profile updated successfully.")
        return redirect('profile')
        
    return render(request, 'profile.html', {'user': request.user})

@login_required
def delete_account_view(request):
    if request.method == 'POST':
        user = request.user
        user.delete()
        messages.success(request, "Your account has been deleted.")
        return redirect('home')
    return redirect('profile')

@login_required
def delete_flow_view(request, flow_id):
    if request.method == 'POST':
        try:
            flow = Flow.objects.get(id=flow_id, user=request.user)
            flow.delete()
        except Flow.DoesNotExist:
            pass
    return redirect('home')

@login_required
def delete_all_flows_view(request):
    if request.method == 'POST':
        Flow.objects.filter(user=request.user).delete()
    return redirect('home')
