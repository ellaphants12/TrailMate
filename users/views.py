from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile, Guide
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm, GuideForm

def register(request):
    """Register a new user"""
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}! You can now log in.')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})

@login_required
def profile(request):
    """User profile view"""
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, 'Your profile has been updated!')
            return redirect('profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)
    
    context = {
        'u_form': u_form,
        'p_form': p_form,
    }
    
    return render(request, 'users/profile.html', context)

@login_required
def become_guide(request):
    """Form for users to become guides"""
    # Check if user is already a guide
    if hasattr(request.user, 'guide'):
        messages.info(request, 'You are already registered as a guide!')
        return redirect('guide_profile')
    
    if request.method == 'POST':
        form = GuideForm(request.POST)
        if form.is_valid():
            guide = form.save(commit=False)
            guide.user = request.user
            guide.save()
            
            # Update user profile
            profile = request.user.profile
            profile.is_guide = True
            profile.save()
            
            messages.success(request, 'You are now registered as a guide!')
            return redirect('guide_profile')
    else:
        form = GuideForm()
    
    return render(request, 'users/become_guide.html', {'form': form})

@login_required
def guide_profile(request):
    """Guide profile view"""
    # Check if user is a guide
    if not hasattr(request.user, 'guide'):
        messages.error(request, 'You are not registered as a guide!')
        return redirect('profile')
    
    if request.method == 'POST':
        form = GuideForm(request.POST, instance=request.user.guide)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your guide profile has been updated!')
            return redirect('guide_profile')
    else:
        form = GuideForm(instance=request.user.guide)
    
    return render(request, 'users/guide_profile.html', {'form': form})

def guide_list(request):
    """List all guides"""
    guides = Guide.objects.all()
    return render(request, 'users/guide_list.html', {'guides': guides})

def guide_detail(request, pk):
    """Detail view for a specific guide"""
    guide = get_object_or_404(Guide, pk=pk)
    return render(request, 'users/guide_detail.html', {'guide': guide})
