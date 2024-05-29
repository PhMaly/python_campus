import mariadb
import sys
from bottle import route, run
import identify as identity


def connect_db():
    # Connect to MariaDB Platform
    try:
        conn = mariadb.connect(
            user=identity.user(),
            password=identity.password(),
            host="localhost",
            port=3306,
        )
        return conn
    except mariadb.Error as e:
        print(f"Error connecting to MariaDB Platform: {e}")
        sys.exit(1)


@route('/todo')
def todo_list():
    conn = mariadb.connect('todo.db')
    c = conn.cursor()
    c.execute("SELECT id, task FROM todo LIKE '1'")
    result = c.fetchall()
    return str(result)


run(host='localhost', port=8080, debug=True)
