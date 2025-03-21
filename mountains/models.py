from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

class Mountain(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    elevation = models.IntegerField(help_text="Elevation in meters")
    difficulty = models.CharField(max_length=20, choices=[
        ('easy', 'Easy'),
        ('moderate', 'Moderate'),
        ('hard', 'Hard'),
        ('expert', 'Expert'),
    ])
    description = models.TextField()
    image = models.ImageField(upload_to='mountains/', blank=True, null=True)
    latitude = models.FloatField()
    longitude = models.FloatField()
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('mountain_detail', args=[str(self.id)])

class Trail(models.Model):
    mountain = models.ForeignKey(Mountain, on_delete=models.CASCADE, related_name='trails')
    name = models.CharField(max_length=100)
    length = models.FloatField(help_text="Length in kilometers")
    estimated_time = models.CharField(max_length=50, help_text="Estimated completion time")
    difficulty = models.CharField(max_length=20, choices=[
        ('easy', 'Easy'),
        ('moderate', 'Moderate'),
        ('hard', 'Hard'),
        ('expert', 'Expert'),
    ])
    description = models.TextField()
    
    def __str__(self):
        return f"{self.name} - {self.mountain.name}"

class Review(models.Model):
    mountain = models.ForeignKey(Mountain, on_delete=models.CASCADE, related_name='reviews')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField(choices=[(i, i) for i in range(1, 6)])
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-created_at']
    
    def __str__(self):
        return f"{self.user.username}'s review of {self.mountain.name}"
