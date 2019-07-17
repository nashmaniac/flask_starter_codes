from celery import Celery


def make_celery(app_name=__name__):
    return Celery(app_name)


celery = make_celery()
