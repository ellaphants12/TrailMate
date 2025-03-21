import os
import shutil

# Create placeholder images
def create_placeholder_images():
    # Create directories if they don't exist
    os.makedirs('static/images', exist_ok=True)
    
    # Create logo.png
    with open('static/images/logo.png', 'w') as f:
        f.write('This is a placeholder for the logo image')
    
    # Create mountain-placeholder.jpg
    with open('static/images/mountain-placeholder.jpg', 'w') as f:
        f.write('This is a placeholder for the mountain image')
    
    # Create hero-bg.jpg
    with open('static/images/hero-bg.jpg', 'w') as f:
        f.write('This is a placeholder for the hero background image')
    
    print("Created placeholder images in static/images/")

if __name__ == '__main__':
    create_placeholder_images()