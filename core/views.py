from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import JsonResponse
from .models import Skill, Project, ContactMessage
from .forms import ContactForm

def home(request):
    form = ContactForm()
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            if request.headers.get('x-requested-with') == 'XMLHttpRequest':
                return JsonResponse({'success': True, 'message': 'Message sent successfully!'})
            messages.success(request, 'Your message has been sent successfully!')
            return redirect('home')
        else:
            if request.headers.get('x-requested-with') == 'XMLHttpRequest':
                return JsonResponse({'success': False, 'message': 'Please fix the errors below.'})

    context = {
        'skills': Skill.objects.all().order_by('order'),
        'projects': Project.objects.all().order_by('order'),
        'form': form,
    }
    return render(request, 'core/index.html', context)
