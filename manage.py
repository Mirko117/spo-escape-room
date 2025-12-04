from app import create_app
import variables

FLASK_ENV = variables.FLASK_ENV

if FLASK_ENV == 'development':
    app = create_app(config_object='config.DevelopmentConfig')
elif FLASK_ENV == 'production':
    app = create_app(config_object='config.ProductionConfig')
else:
    raise ValueError('FLASK_ENV not set properly')
    

if __name__ == "__main__":
    app.run()