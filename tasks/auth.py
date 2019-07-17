from asyncs.celery import celery


@celery.task()
def add(a, b):
    print(a+b)
    return a+b
