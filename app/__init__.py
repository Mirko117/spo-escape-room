from flask import Flask


def create_app(config_object="config.ProductionConfig") -> Flask:
    app = Flask(__name__)

    app.config.from_object(config_object)

    from .pages import index_bp
    app.register_blueprint(index_bp)

    return app
