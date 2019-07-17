from flask import Flask, jsonify
import os

PKG_NAME = os.path.dirname(os.path.dirname(os.path.realpath(__file__))).split('/')[-1].strip()
print(PKG_NAME)
from asyncs.utils import init_celery


def load_config(a):
    print(a.config.get('TAG'))
    if a.config.get('ENV') == 'development':
        a.config.from_pyfile('config/development.py')
    elif a.config.get('ENV') == 'staging':
        a.config.from_pyfile('config/staging.py')
    elif a.config.get('ENV') == 'production':
        a.config.from_pyfile('config/production.py')
    else:
        a.config.from_pyfile('config/default.py')
    print(a.config.get('TAG'))


def create_app(app_name=PKG_NAME, **kwargs):
    app = Flask(app_name)
    app.config.from_pyfile('configuration.py')
    load_config(app)
    if 'celery' in kwargs:
        init_celery(kwargs.get('celery'), app)

    @app.route('/')
    def hello_world():
        print(app.config)
        return jsonify(dict(
            message=app.config.get('TAG')
        ))

    return app
