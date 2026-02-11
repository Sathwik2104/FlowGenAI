# flow_generator/views.py
from django.shortcuts import render
from .models import Flow
from .utils import get_gemini_flow

def home(request):
    generated_content = None
    
    if request.method == "POST":
        topic = request.POST.get('topic')
        if topic:
            # 1. Call AI
            generated_content = get_gemini_flow(topic)
            
            # 2. Save to Database
            Flow.objects.create(topic=topic, content=generated_content)

    # 3. Show past history (optional, helps verify DB works)
    recent_flows = Flow.objects.all().order_by('-created_at')[:5]

    return render(request, 'home.html', {
        'generated_content': generated_content,
        'recent_flows': recent_flows
    })