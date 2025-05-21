from flask import Flask
from flask_migrate import Migrate
from app.config import Config
from app.models.user import db
from app.routes import auth, stocks, watchlist

migrate = Migrate()

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    db.init_app(app)
    migrate.init_app(app, db)

    # Register blueprints
    app.register_blueprint(auth.auth_bp, url_prefix='/auth')
    app.register_blueprint(stocks.stocks_bp, url_prefix='/stocks')
    app.register_blueprint(watchlist.watchlist_bp, url_prefix='/watchlist')

    return app

