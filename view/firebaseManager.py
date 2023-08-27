import firebase_admin
from firebase_admin import credentials, firestore, storage

class FirebaseManager:
    _instance = None

    def __new__(cls, service_account_path):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.connect_firebase(service_account_path)
        return cls._instance

    def connect_firebase(self, service_account_path):
        cred = credentials.Certificate(service_account_path)
        firebase_admin.initialize_app(cred, {'storageBucket': 'tesis-ee155.appspot.com'})
        self.bucket = storage.bucket()

    @property
    def storage_bucket(self):
        return self.bucket
    
    
