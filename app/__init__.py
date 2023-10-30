# In your app/__init__.py
from flask import Flask
from flask_cors import CORS
from pymongo import MongoClient
from dotenv import load_dotenv
import os
from pymongo.errors import ConnectionFailure

# Load environment variables from .env
load_dotenv()

app = Flask(__name__)

# MongoDB Configuration
app.config['MONGO_URI'] = os.getenv('MONGO_URI')



# In your app/__init__.py
try:
    mongo = MongoClient(app.config['MONGO_URI'])
    print("Connected to MongoDB")
except ConnectionFailure as e:
    print(f"MongoDB Connection Error: {e}")


# Allow requests from the frontend
CORS(app)

# Import routes
from app import routes
