import firebase_admin
from firebase_admin import credentials
from firebase_admin import storage

def connect(url):
    cred = credentials.Certificate(url)
    firebase_admin.initialize_app(cred, {'databaseURL': 'https://your-firebase-project.firebaseio.com'})