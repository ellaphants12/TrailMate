# TrailMate

TrailMate is a Django web application that serves as a platform for mountain hikers in the Philippines. It features an interactive map highlighting climbable mountains, user reviews, and direct communication between hikers and local guides.

## Features

- **Interactive Map**: Explore mountains across the Philippines with an interactive map
- **Mountain Profiles**: Detailed information about each mountain, including trails, difficulty, and elevation
- **User Reviews**: Read and write reviews about mountains and trails
- **Community Section**: Connect with other hikers, share experiences, and join events
- **Guide Connection**: Find and communicate with local mountain guides

## Tech Stack

- **Backend**: Django 5.1
- **Database**: SQLite (development), PostgreSQL (production)
- **Frontend**: HTML, CSS, JavaScript, Bootstrap 5
- **Maps**: Leaflet.js
- **Media Storage**: Local file system (development), AWS S3 (production)

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/trailmate.git
cd trailmate
```

2. Create and activate a virtual environment:
```bash
python -m venv trailmate_venv
source trailmate_venv/bin/activate  # On Windows: trailmate_venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Apply migrations:
```bash
python manage.py migrate
```

5. Create a superuser:
```bash
python manage.py createsuperuser
```

6. Load sample data (optional):
```bash
python create_sample_data.py
```

7. Run the development server:
```bash
python manage.py runserver
```

8. Access the application at http://localhost:8000

## Project Structure

- `mountains/`: App for mountain-related functionality
- `users/`: App for user authentication and profiles
- `community/`: App for community features (posts, events, messaging)
- `templates/`: HTML templates
- `static/`: Static files (CSS, JavaScript, images)
- `media/`: User-uploaded files

## Contributing

1. Fork the repository
2. Create a feature branch: `git checkout -b feature-name`
3. Commit your changes: `git commit -m 'Add some feature'`
4. Push to the branch: `git push origin feature-name`
5. Submit a pull request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgements

- Mountain data sourced from various hiking resources in the Philippines
- Special thanks to the Filipino hiking community for inspiration