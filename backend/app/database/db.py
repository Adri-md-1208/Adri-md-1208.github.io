import psycopg
from app.core.config import db_user, db_password, db_host, db_port, db_name


def execute_query(query: str):
    with psycopg.connect(
        user=db_user,
        password=db_password,
        host=db_host,
        port=db_port,
        dbname=db_name
    ) as conn:
        with conn.cursor() as cur:
            cur.execute(query)
            records = cur.fetchall()
        conn.commit()
    if records:
        return records
    return []
