from django.urls import path
from . import views

urlpatterns = [
    path('', views.community_home, name='community_home'),
    path('posts/', views.post_list, name='post_list'),
    path('posts/<int:pk>/', views.post_detail, name='post_detail'),
    path('posts/create/', views.create_post, name='create_post'),
    path('posts/<int:pk>/edit/', views.edit_post, name='edit_post'),
    path('posts/<int:pk>/delete/', views.delete_post, name='delete_post'),
    
    path('events/', views.event_list, name='event_list'),
    path('events/<int:pk>/', views.event_detail, name='event_detail'),
    path('events/create/', views.create_event, name='create_event'),
    path('events/<int:pk>/register/', views.register_for_event, name='register_for_event'),
    path('events/<int:pk>/unregister/', views.unregister_from_event, name='unregister_from_event'),
    
    path('inbox/', views.inbox, name='inbox'),
    path('messages/send/', views.send_message, name='send_message'),
    path('messages/send/<int:recipient_id>/', views.send_message, name='send_message_to'),
    path('messages/<int:pk>/', views.view_message, name='view_message'),
]