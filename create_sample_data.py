import os
import django
import random
from datetime import datetime, timedelta

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'trailmate.settings')
django.setup()

# Import models after Django setup
from django.contrib.auth.models import User
from mountains.models import Mountain, Trail, Review
from users.models import Profile, Guide
from community.models import Post, Comment, Event, EventParticipant, Message

def create_sample_data():
    print("Creating sample data for TrailMate...")
    
    # Create admin user if it doesn't exist
    if not User.objects.filter(username='admin').exists():
        admin_user = User.objects.create_superuser(
            username='admin',
            email='admin@trailmate.ph',
            password='adminpassword'
        )
        print("Created admin user")
    else:
        admin_user = User.objects.get(username='admin')
        print("Admin user already exists")
    
    # Create sample mountains
    mountains_data = [
        {
            'name': 'Mount Pulag',
            'location': 'Benguet, Ifugao, and Nueva Vizcaya',
            'elevation': 2926,
            'difficulty': 'moderate',
            'description': 'Mount Pulag is the third highest mountain in the Philippines and the highest peak in Luzon. It is famous for its "sea of clouds" and stunning sunrise views. The mountain hosts a diverse range of flora and fauna and is considered sacred by local indigenous communities.',
            'latitude': 16.5847,
            'longitude': 120.8854
        },
        {
            'name': 'Mount Apo',
            'location': 'Davao del Sur and North Cotabato',
            'elevation': 2954,
            'difficulty': 'hard',
            'description': 'Mount Apo is the highest mountain in the Philippines, standing at 2,954 meters above sea level. It is an active stratovolcano with a large crater lake and features diverse ecosystems including montane forests, mossy forests, and grasslands. The mountain is home to over 272 bird species, including the critically endangered Philippine Eagle.',
            'latitude': 6.9889,
            'longitude': 125.2710
        },
        {
            'name': 'Mount Mayon',
            'location': 'Albay',
            'elevation': 2463,
            'difficulty': 'expert',
            'description': 'Mount Mayon is an active stratovolcano known for its perfect symmetrical conical shape. It is the most active volcano in the Philippines, having erupted over 50 times in the past 400 years. The mountain and its surroundings form part of Mayon Volcano Natural Park.',
            'latitude': 13.2535,
            'longitude': 123.6864
        },
        {
            'name': 'Mount Pinatubo',
            'location': 'Zambales, Tarlac, and Pampanga',
            'elevation': 1486,
            'difficulty': 'moderate',
            'description': 'Mount Pinatubo is an active stratovolcano that had its last major eruption in 1991, which was one of the largest volcanic eruptions of the 20th century. Today, it is a popular hiking destination known for its beautiful crater lake with changing colors from blue to green depending on the season.',
            'latitude': 15.1429,
            'longitude': 120.3496
        },
        {
            'name': 'Mount Ulap',
            'location': 'Benguet',
            'elevation': 1846,
            'difficulty': 'easy',
            'description': 'Mount Ulap is one of the most popular hiking destinations near Baguio City. It offers breathtaking views of the Cordillera mountain range and is known for its sea of clouds, pine forests, and grassland slopes. The trail also passes by traditional burial caves of the indigenous people.',
            'latitude': 16.3166,
            'longitude': 120.6307
        }
    ]
    
    created_mountains = []
    for mountain_data in mountains_data:
        mountain, created = Mountain.objects.get_or_create(
            name=mountain_data['name'],
            defaults=mountain_data
        )
        if created:
            print(f"Created mountain: {mountain.name}")
        else:
            print(f"Mountain already exists: {mountain.name}")
        created_mountains.append(mountain)
    
    # Create sample trails
    trails_data = [
        {
            'mountain': 'Mount Pulag',
            'name': 'Ambangeg Trail',
            'length': 4.0,
            'estimated_time': '4-5 hours',
            'difficulty': 'easy',
            'description': 'The Ambangeg Trail is the easiest and most popular route to the summit of Mount Pulag. It is also known as the "executive trail" and is suitable for beginners.'
        },
        {
            'mountain': 'Mount Pulag',
            'name': 'Akiki Trail',
            'length': 8.0,
            'estimated_time': '10-11 hours',
            'difficulty': 'hard',
            'description': 'The Akiki Trail is known as the "killer trail" due to its steep ascent and challenging terrain. It offers a more adventurous route to the summit with diverse scenery.'
        },
        {
            'mountain': 'Mount Apo',
            'name': 'Kidapawan Trail',
            'length': 12.0,
            'estimated_time': '2-3 days',
            'difficulty': 'hard',
            'description': 'The Kidapawan Trail is one of the most challenging routes to the summit of Mount Apo. It passes through diverse ecosystems including rainforests, grasslands, and boulder fields.'
        },
        {
            'mountain': 'Mount Mayon',
            'name': 'Buyuan Trail',
            'length': 10.0,
            'estimated_time': '2 days',
            'difficulty': 'expert',
            'description': 'The Buyuan Trail is a challenging route that requires technical climbing skills. It offers stunning views of the Albay Gulf and surrounding landscapes.'
        },
        {
            'mountain': 'Mount Pinatubo',
            'name': 'Capas Trail',
            'length': 5.5,
            'estimated_time': '5-6 hours',
            'difficulty': 'moderate',
            'description': 'The Capas Trail involves a 4x4 ride through lahar canyons followed by a trek to the crater lake. It is the standard route for day hikers visiting Mount Pinatubo.'
        },
        {
            'mountain': 'Mount Ulap',
            'name': 'Ampucao-Sta. Fe Trail',
            'length': 8.0,
            'estimated_time': '5-6 hours',
            'difficulty': 'easy',
            'description': 'This trail takes hikers through pine forests, grasslands, and ridges with panoramic views of the Cordillera mountains. It is a popular day hike destination.'
        }
    ]
    
    for trail_data in trails_data:
        mountain_name = trail_data.pop('mountain')
        mountain = Mountain.objects.get(name=mountain_name)
        
        trail, created = Trail.objects.get_or_create(
            mountain=mountain,
            name=trail_data['name'],
            defaults=trail_data
        )
        
        if created:
            print(f"Created trail: {trail.name} for {mountain.name}")
        else:
            print(f"Trail already exists: {trail.name}")
    
    # Create sample users
    users_data = [
        {
            'username': 'hiker1',
            'email': 'hiker1@example.com',
            'password': 'hikerpassword',
            'first_name': 'Juan',
            'last_name': 'Dela Cruz',
            'is_guide': False
        },
        {
            'username': 'guide1',
            'email': 'guide1@example.com',
            'password': 'guidepassword',
            'first_name': 'Maria',
            'last_name': 'Santos',
            'is_guide': True,
            'guide_data': {
                'experience_years': 5,
                'specialization': 'Mountain climbing, Trekking',
                'certification': 'Certified Mountain Guide',
                'contact_number': '+63 912 345 6789',
                'hourly_rate': 500.00
            }
        },
        {
            'username': 'hiker2',
            'email': 'hiker2@example.com',
            'password': 'hikerpassword',
            'first_name': 'Pedro',
            'last_name': 'Reyes',
            'is_guide': False
        }
    ]
    
    created_users = []
    for user_data in users_data:
        is_guide = user_data.pop('is_guide')
        guide_data = user_data.pop('guide_data', None)
        
        user, created = User.objects.get_or_create(
            username=user_data['username'],
            defaults={
                'email': user_data['email'],
                'first_name': user_data.get('first_name', ''),
                'last_name': user_data.get('last_name', '')
            }
        )
        
        if created:
            user.set_password(user_data['password'])
            user.save()
            print(f"Created user: {user.username}")
        else:
            print(f"User already exists: {user.username}")
        
        # Update profile
        profile = user.profile
        profile.is_guide = is_guide
        profile.save()
        
        # Create guide profile if needed
        if is_guide and guide_data:
            guide, created = Guide.objects.get_or_create(
                user=user,
                defaults=guide_data
            )
            if created:
                print(f"Created guide profile for: {user.username}")
            else:
                print(f"Guide profile already exists for: {user.username}")
        
        created_users.append(user)
    
    # Create sample reviews
    reviews_data = [
        {
            'mountain': 'Mount Pulag',
            'user': 'hiker1',
            'rating': 5,
            'comment': 'Amazing experience! The sea of clouds at sunrise was breathtaking. The Ambangeg trail was relatively easy and well-maintained. Highly recommended for beginners.'
        },
        {
            'mountain': 'Mount Apo',
            'user': 'guide1',
            'rating': 4,
            'comment': 'Mount Apo offers a challenging but rewarding climb. The diverse ecosystems you pass through make it a unique experience. Be prepared for a multi-day trek and changing weather conditions.'
        },
        {
            'mountain': 'Mount Ulap',
            'user': 'hiker2',
            'rating': 5,
            'comment': 'Perfect for a day hike! The views along the trail are spectacular, especially at the summit. The trail is well-marked and not too difficult.'
        }
    ]
    
    for review_data in reviews_data:
        mountain_name = review_data.pop('mountain')
        username = review_data.pop('user')
        
        mountain = Mountain.objects.get(name=mountain_name)
        user = User.objects.get(username=username)
        
        review, created = Review.objects.get_or_create(
            mountain=mountain,
            user=user,
            defaults=review_data
        )
        
        if created:
            print(f"Created review for {mountain.name} by {user.username}")
        else:
            print(f"Review already exists for {mountain.name} by {user.username}")
    
    # Create sample community posts
    posts_data = [
        {
            'user': 'hiker1',
            'title': 'My First Climb: Mount Ulap',
            'content': 'Just completed my first climb to Mount Ulap and it was an amazing experience! The trail was well-maintained and the views were spectacular. I would recommend it to anyone looking for a beginner-friendly mountain to climb.',
            'mountain': 'Mount Ulap'
        },
        {
            'user': 'guide1',
            'title': 'Tips for Climbing Mount Pulag',
            'content': 'As a guide who has climbed Mount Pulag numerous times, here are some tips for those planning to visit:\n\n1. Always check the weather forecast before your climb.\n2. Pack warm clothes as temperatures can drop to near freezing at night.\n3. Respect the mountain and local customs.\n4. Stay hydrated throughout your climb.\n5. Leave no trace - pack out all your trash.',
            'mountain': 'Mount Pulag'
        },
        {
            'user': 'hiker2',
            'title': 'Looking for Climbing Buddies for Mount Apo',
            'content': 'Planning to climb Mount Apo next month and looking for climbing buddies to join me. I\'m planning a 3-day trek via the Kidapawan Trail. If you\'re interested, please message me!',
            'mountain': 'Mount Apo'
        }
    ]
    
    for post_data in posts_data:
        username = post_data.pop('user')
        mountain_name = post_data.pop('mountain')
        
        user = User.objects.get(username=username)
        mountain = Mountain.objects.get(name=mountain_name)
        
        post, created = Post.objects.get_or_create(
            user=user,
            title=post_data['title'],
            defaults={
                'content': post_data['content'],
                'mountain': mountain
            }
        )
        
        if created:
            print(f"Created post: {post.title}")
        else:
            print(f"Post already exists: {post.title}")
    
    # Create sample events
    events_data = [
        {
            'title': 'Mount Pulag Sunrise Hike',
            'description': 'Join us for a weekend hike to Mount Pulag to witness the famous sea of clouds and sunrise. This guided hike will take the Ambangeg Trail and is suitable for beginners.',
            'mountain': 'Mount Pulag',
            'organizer': 'guide1',
            'start_date': datetime.now() + timedelta(days=30),
            'end_date': datetime.now() + timedelta(days=31),
            'max_participants': 10
        },
        {
            'title': 'Mount Ulap Day Hike',
            'description': 'A one-day hike to Mount Ulap to enjoy the beautiful scenery and take photos. This is a beginner-friendly hike with a guide.',
            'mountain': 'Mount Ulap',
            'organizer': 'guide1',
            'start_date': datetime.now() + timedelta(days=15),
            'end_date': datetime.now() + timedelta(days=15),
            'max_participants': 15
        }
    ]
    
    for event_data in events_data:
        mountain_name = event_data.pop('mountain')
        organizer_name = event_data.pop('organizer')
        
        mountain = Mountain.objects.get(name=mountain_name)
        organizer = User.objects.get(username=organizer_name)
        
        event, created = Event.objects.get_or_create(
            title=event_data['title'],
            mountain=mountain,
            organizer=organizer,
            defaults={
                'description': event_data['description'],
                'start_date': event_data['start_date'],
                'end_date': event_data['end_date'],
                'max_participants': event_data['max_participants']
            }
        )
        
        if created:
            print(f"Created event: {event.title}")
        else:
            print(f"Event already exists: {event.title}")
    
    print("Sample data creation completed!")

if __name__ == '__main__':
    create_sample_data()