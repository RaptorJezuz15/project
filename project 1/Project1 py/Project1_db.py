import psycopg2
from psycopg2._psycopg import OperationalError


def create_connection():
    try:
        conn = psycopg2.connect(
            database='Project 1',
            user='postgres',
            password='ZoJG16frie0kmoPto10h',
            host='database-1.c2yyb8tirfrh.us-east-2.rds.amazonaws.com',
            port='5432'
        )
        return conn

    except OperationalError as e:
        print(f'{e}')
        return 'none'


connection = create_connection()


def _test():
    print(connection)