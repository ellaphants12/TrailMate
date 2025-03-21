import os
import django

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'trailmate.settings')
django.setup()

from django.contrib.auth.models import User

# Get the admin user
admin = User.objects.get(username='admin')

# Set the password
admin.set_password('adminpassword')
admin.save()

print("Admin password set to 'adminpassword'")