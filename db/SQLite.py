import sqlite3
from models import movie

def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by db_file
    :param db_file: database file
    :return: Connection object or None
    """
    conn = sqlite3.connect(db_file)
    return conn

    return None

def create_table(conn, create_table_sql):
    """ create a table from the create_table_sql statement
    :param conn: Connection object
    :param create_table_sql: a CREATE TABLE statement
    :return:
    """
    c = conn.cursor()
    c.execute(create_table_sql)


def select_all_movies(conn):
    """
    Query all rows in the tasks table
    :param conn: the Connection object
    :return:
    """
    cur = conn.cursor()
    cur.execute("SELECT * FROM movies")

    rows = cur.fetchall()

    movies = []
    for row in rows:
        print(row)
        movie.append(movie(row))

    print(movies)

def select_all_schedules(conn):
    """
    Query all rows in the tasks table
    :param conn: the Connection object
    :return:
    """
    cur = conn.cursor()
    cur.execute("SELECT * FROM schedules")

    rows = cur.fetchall()

    movies = []
    for row in rows:
        print(row[1])
        movie.append(movie(row))

    print(movies)

def main():
    database = "../pythonsqlite.db"

    sql_create_movies_table = """ CREATE TABLE IF NOT EXISTS movies (
                                        id integer PRIMARY KEY,
                                        title text NOT NULL,
                                        description text,
                                        genre text
                                    ); """

    sql_create_schedule_table = """CREATE TABLE IF NOT EXISTS schedules (
                                    id integer PRIMARY KEY,
                                    date text NOT NULL,
                                    movie_id integer NOT NULL,
                                    total_amount integer,
                                    price real,
                                    FOREIGN KEY (movie_id) REFERENCES movies (id)
                                );"""

    sql_create_reservations_table = """CREATE TABLE IF NOT EXISTS reservations (
                                        id integer PRIMARY KEY,
                                        schedule_id integer NOT NULL,
                                        amount integer,
                                        FOREIGN KEY (schedule_id) REFERENCES schedules (id)
                                    );"""

    # create a database connection
    conn = create_connection(database)
    if conn is not None:
        # create movies table
        create_table(conn, sql_create_movies_table)
        # create schedules table
        create_table(conn, sql_create_schedule_table)
        # create reservations table
        create_table(conn, sql_create_reservations_table)
        select_all_schedules(conn)
    else:
        print("Error! cannot create the database connection.")

if __name__ == '__main__':
    main()
