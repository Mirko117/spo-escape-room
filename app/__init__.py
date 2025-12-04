from flask import Flask


def create_app(config_object="config.ProductionConfig") -> Flask:
    app = Flask(__name__)

    app.config.from_object(config_object)

    from .pages import pages_bp
    app.register_blueprint(pages_bp)

    return app
