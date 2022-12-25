from pathlib import Path
from entities.score import Score
from database_connection import get_database_connection


def get_score_by_row(row):
    return Score(row["score"]) if row else None


class ScoreRepository:
    def __init__(self, connection):
        """Class constructor.
        Args:
            connection: Databases connection object.
        """

        self._connection = connection

    def find_all(self):
        """Returns all scores.
        Returns:
            Returns a list of scores, ordered descendingly.
        """

        cursor = self._connection.cursor()

        cursor.execute("select * from scores order by score desc")

        rows = cursor.fetchall()

        return list(map(get_score_by_row, rows))

    def create(self, score):
        """Saves score to database
        Args:
            score: score player got from game
        """

        cursor = self._connection.cursor()

        cursor.execute(
            "insert into scores (score) values (?)",
            (score,)
        )

        self._connection.commit()

    def delete_all(self):
        """Deletes all.
        """

        cursor = self._connection.cursor()

        cursor.execute("delete from scores")

        self._connection.commit()


score_repository = ScoreRepository(get_database_connection())
