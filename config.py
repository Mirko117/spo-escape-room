import variables


class Config:
    SECRET_KEY = variables.SECRET_KEY
    FLASK_ENV = variables.FLASK_ENV


class DevelopmentConfig(Config):
    DEBUG = True


class ProductionConfig(Config):
    DEBUG = False
