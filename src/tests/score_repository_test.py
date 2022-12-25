import unittest
from repositories.scores_repository import score_repository
from entities.score import Score


class TestScoreRepository(unittest.TestCase):
    def setUp(self):
        score_repository.delete_all()
        self.score = 10

    def test_create(self):
        score_repository.create(self.score)
        scores = score_repository.find_all()

        self.assertEqual(len(scores), 1)
        self.assertEqual(scores[0].score, self.score)
