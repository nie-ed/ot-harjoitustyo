import unittest
from logic.clock import Clock


class TestClock(unittest.TestCase):
    def setUp(self):
        self.test_clock = Clock()

    def test_tick(self):
        self.test_clock.tick(60)

    def test_get_ticks(self):
        self.assertEqual(self.test_clock.get_ticks(), 0)
