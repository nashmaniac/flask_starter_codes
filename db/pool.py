from psycopg2.pool import SimpleConnectionPool


class Connection(object):
    db_pool = None

    @classmethod
    def get_connection(cls):
        return cls.db_pool.getconn()

    @classmethod
    def put_connection(cls, conn):
        if conn:
            cls.db_pool.putconn(conn)

    @classmethod
    def initiate_db_connection(cls, current_app):
        cls.db_pool = SimpleConnectionPool(
            2, 20,
            user=current_app.config.get('DB_USER'),
            password=current_app.config.get('DB_PASSWORD'),
            host=current_app.config.get('DB_HOST'),
            port=current_app.config.get('DB_PORT'),
            database=current_app.config.get('DB_NAME'),
        )

