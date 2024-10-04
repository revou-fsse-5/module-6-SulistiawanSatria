import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'kunci_rahasia_anda'
    DEBUG = False

class DevelopmentConfig(Config):
    DEBUG = True

class ProductionConfig(Config):
    DEBUG = False

config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}
