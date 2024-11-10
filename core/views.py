from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .models import JobPosting
from .forms import ProfileUpdateForm

@login_required
def home(request):
    if request.user.is_authenticated:
        jobs = JobPosting.objects.all().order_by('company_name')
    else:
        jobs = []
    return render(request, 'core/home.html', {'jobs': jobs})

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})

@login_required
def profile(request):
    if request.method == 'POST':
        form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your profile has been updated!')
            return redirect('profile')
    else:
        form = ProfileUpdateForm(instance=request.user.profile)
    
    return render(request, 'core/profile.html', {'form': form})

@login_required
def job_listings(request):
    jobs = JobPosting.objects.all().order_by('company_name')
    return render(request, 'core/job_listings.html', {'jobs': jobs}) 