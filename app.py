from core import factory
from asyncs import celery
import blueprints
from db.pool import Connection
if __name__ == '__main__':
    app = factory.create_app(celery=celery.celery)
    Connection.initiate_db_connection(app)
    app.register_blueprint(blueprints.auth_bp)
    app.run(debug=app.config.get('DEBUG'))
