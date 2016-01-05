from database.tables import Post
from database.connection import Connection
from pymysql import Error

__author__ = "Aishwarya Sharma"


def get_posts(post_id=None):

    if post_id is None:
        procedure_name = "get_all_posts()"
    else:
        procedure_name = "get_post({0})".format(post_id)

    conn = None
    posts = []
    try:
        conn = Connection().get_connection()
        with conn.cursor() as cursor:
            sql = "call " + procedure_name
            cursor.execute(sql)

            for row in cursor.fetchall():
                posts.append(Post().dictionary_mapper(row))

    except Error as e:
        print("There was a database error.")
        for arg in e.args:
            print(arg)
    finally:
        conn.close()

    return posts


def add_post(title, content):
    conn = None
    result = False
    try:
        conn = Connection().get_connection()
        with conn.cursor() as cursor:
            sql = "call add_post('{0}', '{1}')".format(title, content)
            cursor.execute(sql)
        conn.commit()
        result = True
    except Error as e:
        print("There was a database error.")
        for arg in e.args:
            print(arg)
        conn.rollback()
    finally:
        conn.close()

    return result


def edit_post(post_id, title, content):
    conn = None
    result = False
    try:
        conn = Connection().get_connection()
        with conn.cursor() as cursor:
            sql = "call edit_post({0}, '{1}', '{2}')".format(post_id, title, content)
            cursor.execute(sql)
        conn.commit()
        result = True
    except Error as e:
        print("There was a database error.")
        for arg in e.args:
            print(arg)
        conn.rollback()
    finally:
        conn.close()

    return result
