from flask import Flask


def create_app(config_object="config.ProductionConfig") -> Flask:
    app = Flask(__name__)

    app.config.from_object(config_object)

    from .pages import pages_bp
    from .api.api import api_bp
    app.register_blueprint(pages_bp)
    app.register_blueprint(api_bp, url_prefix="/api")

    return app
