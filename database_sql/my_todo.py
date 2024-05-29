import mariadb
import sys
from bottle import route, run, debug, template, TEMPLATE_PATH
import identify as identity
import os

path_directory = os.path.join(os.getcwd(), '..', 'views')
TEMPLATE_PATH.insert(0, path_directory)


# connection à ma DB todoPython
def connect_db():
    try:
        conn = mariadb.connect(
            user=identity.user(),
            password=identity.password(),
            host="localhost",
            port=3306,
            database='todoPython'
        )
        return conn
    except mariadb.Error as e:
        print(f"Error connecting to MariaDB Platform: {e}")
        sys.exit(1)


# création d'une table todo
def setup_database(con):
    try:
        cur = con.cursor()
        cur.execute(
            "CREATE table if not exists todoPython.todo (id integer not null auto_increment, task varchar(100), status bool, primary key(id))engine=InnoDB")
        cur.close()

    except mariadb.Error as e:
        print(f"Error connecting to MariaDB Platform: {e}")
        sys.exit(1)


# insertion de données dans ma table todo
def insert_into_todo_table(con):
    try:
        print("Connecting to the database...")
        cur = con.cursor()
        print("Connected to the database.")

        print("Inserting data...")
        cur.execute(
            "INSERT INTO todo (task,status) VALUES ('Read A-byte-of-python to get a good introduction into Python',0)")
        cur.execute("INSERT INTO todo (task,status) VALUES ('Visit the Python website',1)")
        cur.execute(
            "INSERT INTO todo (task,status) VALUES ('Test various editors for and check the syntax highlighting',1)")
        cur.execute("INSERT INTO todo (task,status) VALUES ('Choose your favorite WSGI-Framework',0)")
        print("Data inserted.")

        print("Committing the transaction...")
        con.commit()
        print("Transaction committed.")
        cur.close()

    except mariadb.Error as e:
        print(f"Error connecting to MariaDB Platform: {e}")
        sys.exit(1)


# afficher via buttle
@route('/todo')
def todo_list():
    conn = connect_db()
    c = conn.cursor()
    c.execute("SELECT id, task FROM todo WHERE status = 1")
    result = c.fetchall()
    return template('make_table', rows=result)


def main():
    con = connect_db()
    setup_database(con)
    insert_into_todo_table(con)
    debug(True)
    run(host='localhost', port=8080, reloader=True)


if __name__ == '__main__':
    main()
