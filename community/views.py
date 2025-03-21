from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import JsonResponse
from django.db.models import Q
from django.utils import timezone
from .models import Post, Comment, Message, Event, EventParticipant
from .forms import PostForm, CommentForm, MessageForm, EventForm

def community_home(request):
    """Community home page with recent posts and events"""
    posts = Post.objects.all()[:5]
    events = Event.objects.filter(start_date__gte=timezone.now())[:5]
    return render(request, 'community/home.html', {
        'posts': posts,
        'events': events
    })

def post_list(request):
    """List all community posts"""
    posts = Post.objects.all()
    return render(request, 'community/post_list.html', {'posts': posts})

def post_detail(request, pk):
    """Detail view for a specific post"""
    post = get_object_or_404(Post, pk=pk)
    comments = post.comments.all()
    
    # Handle comment form submission
    if request.method == 'POST' and request.user.is_authenticated:
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.user = request.user
            comment.save()
            messages.success(request, 'Your comment has been added!')
            return redirect('post_detail', pk=post.pk)
    else:
        form = CommentForm()
    
    return render(request, 'community/post_detail.html', {
        'post': post,
        'comments': comments,
        'form': form
    })

@login_required
def create_post(request):
    """Create a new community post"""
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            messages.success(request, 'Your post has been created!')
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    
    return render(request, 'community/create_post.html', {'form': form})

@login_required
def edit_post(request, pk):
    """Edit an existing post"""
    post = get_object_or_404(Post, pk=pk)
    
    # Check if user is the author
    if post.user != request.user:
        messages.error(request, 'You can only edit your own posts!')
        return redirect('post_detail', pk=post.pk)
    
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your post has been updated!')
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    
    return render(request, 'community/edit_post.html', {
        'form': form,
        'post': post
    })

@login_required
def delete_post(request, pk):
    """Delete a post"""
    post = get_object_or_404(Post, pk=pk)
    
    # Check if user is the author
    if post.user != request.user:
        messages.error(request, 'You can only delete your own posts!')
        return redirect('post_detail', pk=post.pk)
    
    if request.method == 'POST':
        post.delete()
        messages.success(request, 'Your post has been deleted!')
        return redirect('post_list')
    
    return render(request, 'community/delete_post.html', {'post': post})

@login_required
def inbox(request):
    """User's message inbox"""
    messages_received = Message.objects.filter(recipient=request.user)
    return render(request, 'community/inbox.html', {'messages': messages_received})

@login_required
def send_message(request, recipient_id=None):
    """Send a message to another user"""
    recipient = None
    if recipient_id:
        recipient = get_object_or_404(User, pk=recipient_id)
    
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            message = form.save(commit=False)
            message.sender = request.user
            message.save()
            messages.success(request, 'Your message has been sent!')
            return redirect('inbox')
    else:
        form = MessageForm(initial={'recipient': recipient})
    
    return render(request, 'community/send_message.html', {'form': form})

@login_required
def view_message(request, pk):
    """View a specific message"""
    message = get_object_or_404(Message, pk=pk)
    
    # Check if user is the recipient
    if message.recipient != request.user and message.sender != request.user:
        messages.error(request, 'You can only view your own messages!')
        return redirect('inbox')
    
    # Mark as read if user is recipient
    if message.recipient == request.user and not message.is_read:
        message.is_read = True
        message.save()
    
    return render(request, 'community/view_message.html', {'message': message})

def event_list(request):
    """List all community events"""
    events = Event.objects.filter(start_date__gte=timezone.now())
    past_events = Event.objects.filter(start_date__lt=timezone.now())
    return render(request, 'community/event_list.html', {
        'events': events,
        'past_events': past_events
    })

def event_detail(request, pk):
    """Detail view for a specific event"""
    event = get_object_or_404(Event, pk=pk)
    participants = event.participants.all()
    user_registered = request.user.is_authenticated and EventParticipant.objects.filter(event=event, user=request.user).exists()
    
    return render(request, 'community/event_detail.html', {
        'event': event,
        'participants': participants,
        'user_registered': user_registered
    })

@login_required
def create_event(request):
    """Create a new community event"""
    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            event = form.save(commit=False)
            event.organizer = request.user
            event.save()
            messages.success(request, 'Your event has been created!')
            return redirect('event_detail', pk=event.pk)
    else:
        form = EventForm()
    
    return render(request, 'community/create_event.html', {'form': form})

@login_required
def register_for_event(request, pk):
    """Register for an event"""
    event = get_object_or_404(Event, pk=pk)
    
    # Check if already registered
    if EventParticipant.objects.filter(event=event, user=request.user).exists():
        messages.info(request, 'You are already registered for this event!')
        return redirect('event_detail', pk=event.pk)
    
    # Check if event is full
    if event.max_participants > 0 and event.participants.count() >= event.max_participants:
        messages.error(request, 'This event is already full!')
        return redirect('event_detail', pk=event.pk)
    
    # Register user
    EventParticipant.objects.create(event=event, user=request.user)
    messages.success(request, 'You have successfully registered for this event!')
    return redirect('event_detail', pk=event.pk)

@login_required
def unregister_from_event(request, pk):
    """Unregister from an event"""
    event = get_object_or_404(Event, pk=pk)
    registration = get_object_or_404(EventParticipant, event=event, user=request.user)
    
    if request.method == 'POST':
        registration.delete()
        messages.success(request, 'You have unregistered from this event!')
        return redirect('event_detail', pk=event.pk)
    
    return render(request, 'community/unregister_event.html', {'event': event})
