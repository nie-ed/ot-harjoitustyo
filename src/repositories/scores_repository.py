from pathlib import Path
from entities.score import Score
from database_connection import get_database_connection

def get_score_by_row(row):
    return Score(row["username"], row["score"]) if row else None


class ScoreRepository:
    def __init__(self, connection):
        """Luokan konstruktori.
        Args:
            connection: Tietokantayhteyden Connection-olio
        """

        self._connection = connection

    def find_all(self):
        """Palauttaa kaikki käyttäjät.
        Returns:
            Palauttaa listan User-olioita.
        """

        cursor = self._connection.cursor()

        cursor.execute("select * from score")

        rows = cursor.fetchall()

        return list(map(get_score_by_row, rows))




    def create(self, score, username):
        """Saves score and username to database
        Args:
            username: player username
            score: score player got from game
        Returns:
            Tallennettu käyttjä User-oliona.
        """

        cursor = self._connection.cursor()

        cursor.execute(
            "insert into score (score, username) values (?, ?)",
            (score, username)
        )

        self._connection.commit()


    def delete_all(self):
        """Deletes all.
        """

        cursor = self._connection.cursor()

        cursor.execute("delete from score")

        self._connection.commit()


score_repository = ScoreRepository(get_database_connection())

