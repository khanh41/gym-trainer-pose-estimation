import os

GRPC_URL = os.getenv("GRPC_URL")
GOOGLE_APPLICATION_CREDENTIALS = os.getenv("GOOGLE_APPLICATION_CREDENTIALS")
FIREBASE_IMAGE_URL = lambda x: f"https://firebasestorage.googleapis.com/v0/b/aift-b7b2c.appspot.com/o/{x}.jpg?alt=media"

VIDEO_TEMPLATE = {
    "path": "app/resources/video.mp4",
    "url": "https://www.dropbox.com/s/o6r4sz3763k55xb/videoplayback.mp4?dl=1"
}

DOMAIN = os.getenv("DOMAIN")
MONGO_DETAILS = os.getenv("MONGO_DETAILS")
SECRET_KEY = os.getenv('SECRET_KEY')
ALGORITHM = os.getenv('ALGORITHM')
ACCESS_TOKEN_EXPIRE_MINUTES = 30

ADMIN_USER = -1
SUPER_USERNAME = os.getenv('SUPER_USERNAME')
SUPER_PASSWORD = os.getenv('SUPER_PASSWORD')
