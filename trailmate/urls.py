from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from users import views as user_views
from mountains import views as mountain_views

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # Mountains app
    path('', mountain_views.home, name='home'),
    path('mountains/', mountain_views.mountain_list, name='mountain_list'),
    path('mountains/<int:pk>/', mountain_views.mountain_detail, name='mountain_detail'),
    path('mountains/search/', mountain_views.search_mountains, name='search_mountains'),
    path('mountains/data/', mountain_views.mountains_json, name='mountains_json'),
    path('mountains/<int:mountain_id>/review/', mountain_views.add_review, name='add_review'),
    
    # Community app
    path('community/', include('community.urls')),
    
    # User authentication
    path('register/', user_views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    path('profile/', user_views.profile, name='profile'),
    path('guides/', user_views.guide_list, name='guide_list'),
    path('guides/<int:pk>/', user_views.guide_detail, name='guide_detail'),
    path('become-guide/', user_views.become_guide, name='become_guide'),
    path('guide-profile/', user_views.guide_profile, name='guide_profile'),
    
    # Password reset
    path('password-reset/', 
         auth_views.PasswordResetView.as_view(template_name='users/password_reset.html'), 
         name='password_reset'),
    path('password-reset/done/', 
         auth_views.PasswordResetDoneView.as_view(template_name='users/password_reset_done.html'), 
         name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/', 
         auth_views.PasswordResetConfirmView.as_view(template_name='users/password_reset_confirm.html'), 
         name='password_reset_confirm'),
    path('password-reset-complete/', 
         auth_views.PasswordResetCompleteView.as_view(template_name='users/password_reset_complete.html'), 
         name='password_reset_complete'),
]

# Serve media files in development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
