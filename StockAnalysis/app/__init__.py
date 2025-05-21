from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager
from flask_caching import Cache
from config import Config

db = SQLAlchemy()
jwt = JWTManager()
cache = Cache()


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    db.init_app(app)
    jwt.init_app(app)
    cache.init_app(app)

    from app.routes.auth import auth_bp
    from app.routes.stocks import stocks_bp
    from app.routes.watchlist import watchlist_bp

    app.register_blueprint(auth_bp)
    app.register_blueprint(stocks_bp)
    app.register_blueprint(watchlist_bp)

    return app