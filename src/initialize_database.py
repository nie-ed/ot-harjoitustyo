from database_connection import get_database_connection


def delete_tables(connection):
    """Delete Databases
    Args:
        connection: a connection object for the database
    """

    cursor = connection.cursor()

    cursor.execute("""
        drop table if exists scores;
    """)

    connection.commit()


def create_tables(connection):
    """Create a database.
    Args:
        connection: a connection object for the database
    """

    cursor = connection.cursor()

    cursor.execute("""
        create table scores (
            score integer
        );
    """)

    connection.commit()


def initialize_database():
    """Initializes database."""

    connection = get_database_connection()

    delete_tables(connection)
    create_tables(connection)


if __name__ == "__main__":
    initialize_database()
