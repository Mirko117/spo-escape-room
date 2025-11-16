import app_secrets


class Config:
    SECRET_KEY = app_secrets.SECRET_KEY
    FLASK_ENV = app_secrets.FLASK_ENV


class DevelopmentConfig(Config):
    DEBUG = True


class ProductionConfig(Config):
    DEBUG = False
