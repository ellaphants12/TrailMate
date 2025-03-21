from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.views.generic import ListView, DetailView
from django.contrib import messages
from .models import Mountain, Trail, Review
from .forms import ReviewForm

def home(request):
    """Home page view with interactive map"""
    mountains = Mountain.objects.all()
    return render(request, 'mountains/home.html', {'mountains': mountains})

def mountain_list(request):
    """List all mountains"""
    mountains = Mountain.objects.all()
    return render(request, 'mountains/mountain_list.html', {'mountains': mountains})

def mountain_detail(request, pk):
    """Detail view for a specific mountain"""
    mountain = get_object_or_404(Mountain, pk=pk)
    trails = mountain.trails.all()
    reviews = mountain.reviews.all()
    
    # Handle review form submission
    if request.method == 'POST' and request.user.is_authenticated:
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.mountain = mountain
            review.user = request.user
            review.save()
            messages.success(request, 'Your review has been added!')
            return redirect('mountain_detail', pk=mountain.pk)
    else:
        form = ReviewForm()
    
    return render(request, 'mountains/mountain_detail.html', {
        'mountain': mountain,
        'trails': trails,
        'reviews': reviews,
        'form': form
    })

def mountains_json(request):
    """Return mountains data as JSON for the map"""
    mountains = Mountain.objects.all()
    data = [{
        'id': mountain.id,
        'name': mountain.name,
        'latitude': mountain.latitude,
        'longitude': mountain.longitude,
        'elevation': mountain.elevation,
        'difficulty': mountain.difficulty,
    } for mountain in mountains]
    return JsonResponse(data, safe=False)

@login_required
def add_review(request, mountain_id):
    """Add a review to a mountain"""
    mountain = get_object_or_404(Mountain, pk=mountain_id)
    
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.mountain = mountain
            review.user = request.user
            review.save()
            messages.success(request, 'Your review has been added!')
            return redirect('mountain_detail', pk=mountain.pk)
    else:
        form = ReviewForm()
    
    return render(request, 'mountains/add_review.html', {
        'form': form,
        'mountain': mountain
    })

def search_mountains(request):
    """Search mountains by name, location, or difficulty"""
    from django.db.models import Q
    query = request.GET.get('q', '')
    if query:
        mountains = Mountain.objects.filter(
            Q(name__icontains=query) |
            Q(location__icontains=query) |
            Q(difficulty__icontains=query)
        )
    else:
        mountains = Mountain.objects.all()
    
    return render(request, 'mountains/mountain_list.html', {
        'mountains': mountains,
        'query': query
    })
