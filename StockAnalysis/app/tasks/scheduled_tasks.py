from celery import Celery
from app import create_app
from app.models import User, Watchlist
from nselib import equity_list

def make_celery(app):
    celery = Celery(
        app.import_name,
        broker=app.config['CELERY_BROKER_URL']
    )
    celery.conf.update(app.config)
    return celery

celery = make_celery(create_app())

@celery.task
def update_market_data():
    """Periodic task to update market data"""
    # Implementation from original code