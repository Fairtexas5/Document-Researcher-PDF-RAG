import os
from dotenv import load_dotenv

load_dotenv()

class Config:

    SECRET_KEY = os.environ.get('SECRET_KEY', 'your-secret-key-here')
    UPLOAD_FOLDER = 'uploads'
    VECTOR_DB_PATH = 'vector_db'
    MAX_CONTENT_LENGTH = 16 * 1024 * 1024

    EMBEDDING_MODEL = 'sentence-transformers/all-MiniLM-L6-v2'
    CHUNK_SIZE = 1000
    CHUNK_OVERLAP = 200

    TOP_K = 5

    ALLOWED_EXTENSIONS = {'pdf'}
os.makedirs(Config.UPLOAD_FOLDER, exist_ok=True)
os.makedirs(Config.VECTOR_DB_PATH, exist_ok=True)
