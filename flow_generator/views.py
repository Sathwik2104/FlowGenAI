# flow_generator/views.py
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from .models import Flow
from .utils import get_gemini_flow

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
    return redirect('login')