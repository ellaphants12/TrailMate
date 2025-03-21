from django import forms
from .models import Post, Comment, Message, Event
from django.contrib.auth.models import User

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'mountain', 'image']
        widgets = {
            'content': forms.Textarea(attrs={'rows': 5, 'placeholder': 'Share your thoughts...'}),
        }

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
        widgets = {
            'content': forms.Textarea(attrs={'rows': 3, 'placeholder': 'Write a comment...'}),
        }
        labels = {
            'content': '',
        }

class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ['recipient', 'content']
        widgets = {
            'content': forms.Textarea(attrs={'rows': 4, 'placeholder': 'Write your message...'}),
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Filter users who are guides
        self.fields['recipient'].queryset = User.objects.filter(profile__is_guide=True)
        self.fields['recipient'].label_from_instance = lambda obj: f"{obj.username} ({obj.profile.location})"

class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['title', 'description', 'mountain', 'start_date', 'end_date', 'max_participants']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 4}),
            'start_date': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            'end_date': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }