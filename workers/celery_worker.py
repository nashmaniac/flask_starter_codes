from asyncs.celery import celery
from core.factory import create_app
from asyncs.utils import init_celery

app = create_app()
init_celery(celery, app)
