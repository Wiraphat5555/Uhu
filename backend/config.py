# config.py
class Config:
    SECRET_KEY = 'your-secret-key'
    JWT_SECRET_KEY = 'your-jwt-secret'
    MONGODB_SETTINGS = {
        'db': 'mario_notes888',
        'host': 'localhost',
        'port': 27017
    }