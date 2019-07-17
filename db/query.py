from .pool import Connection
from psycopg2.extras import RealDictCursor


def run_query(query, fetch_one=False):
    conn = None
    try:
        conn = Connection.get_connection()
        cur = conn.cursor(cursor_factory=RealDictCursor)
        cur.execute(query)
        if fetch_one:
            return cur.fetchone()
        else:
            return cur.fetchall()
    except Exception as exc:
        print(exc)
    # finally:
    #     if conn:
    #         Connection.put_connection(conn)
