import cloudinary
import cloudinary.uploader
import cloudinary.api
from dotenv import load_dotenv
import os

load_dotenv()

images = [
    'images/alexender.jpeg',
    'images/andrew.jpeg',
    'images/bruno.jpeg',
    'images/cole.jpeg',
    'images/diogo.jpeg',
    'images/dominik.jpeg',
    'images/ederson.jpeg',
    'images/gabriel.jpeg',
    'images/james.jpeg',
    'images/josko.jpeg',
    'images/kevin.jpeg',
    'images/phil.jpeg',
    'images/trent.jpeg',
]
# Configure Cloudinary with credentials
cloudinary.config(
    cloud_name=os.getenv("CLOUD_NAME"),
    api_key=os.getenv("API_KEY"),
    api_secret=os.getenv("API_SECRET")
)


def upload_image(image_path):
    response = cloudinary.uploader.upload(image_path)
    return response['url']  # This returns the URL of the uploaded image


for image in images:
    image_url = upload_image(image)
    print(f"Uploaded image URL: {image_url}")
