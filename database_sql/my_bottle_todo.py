import mariadb
import sys
from bottle import route, run
import identify as identity


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


def setup_database(con):
    try:
        cur = con.cursor()
        cur.execute(
            "CREATE table if not exists todoPython.todo (id integer not null auto_increment, task varchar(100), status bool, primary key(id))engine=InnoDB")
        cur.close()

    except mariadb.Error as e:
        print(f"Error connecting to MariaDB Platform: {e}")
        sys.exit(1)


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


def main():
    con = connect_db()
    setup_database(con)
    insert_into_todo_table(con)
    run(host='localhost', port=8080, debug=True)


if __name__ == '__main__':
    main()



