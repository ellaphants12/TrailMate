from django import forms
from .models import Review, Mountain

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['rating', 'comment']
        widgets = {
            'comment': forms.Textarea(attrs={'rows': 4, 'placeholder': 'Share your experience...'}),
        }

class MountainSearchForm(forms.Form):
    query = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={'placeholder': 'Search mountains...', 'class': 'search-input'})
    )
    difficulty = forms.ChoiceField(
        required=False,
        choices=[('', 'All Difficulties')] + list(Mountain._meta.get_field('difficulty').choices),
        widget=forms.Select(attrs={'class': 'filter-select'})
    )
    min_elevation = forms.IntegerField(
        required=False,
        widget=forms.NumberInput(attrs={'placeholder': 'Min elevation', 'class': 'filter-input'})
    )
    max_elevation = forms.IntegerField(
        required=False,
        widget=forms.NumberInput(attrs={'placeholder': 'Max elevation', 'class': 'filter-input'})
    )