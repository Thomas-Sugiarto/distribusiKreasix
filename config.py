import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'distribusi_produk_secret_key'
    
    # Database configuration
    DATABASE_URL = os.environ.get('postgres://avnadmin:AVNS_pLgUM-pJRCFOfGeM295@pg-18f2c735-kreasix-2ab4.d.aivencloud.com:16503/defaultdb?sslmode=require')
    DB_HOST = os.environ.get('DB_HOST') or 'pg-18f2c735-kreasix-2ab4.d.aivencloud.com'
    DB_PORT = os.environ.get('DB_PORT') or '16503'
    DB_NAME = os.environ.get('DB_NAME') or 'defaultdb'
    DB_USER = os.environ.get('DB_USER') or 'avnadmin'
    DB_PASSWORD = os.environ.get('DB_PASSWORD') or 'AVNS_pLgUM-pJRCFOfGeM295'

class DevelopmentConfig(Config):
    DEBUG = True
    FLASK_ENV = 'development'

class ProductionConfig(Config):
    DEBUG = False
    FLASK_ENV = 'production'

config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}