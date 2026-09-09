import unittest

from CSE431.HW1.q2.main import loopback


class TestQ1(unittest.TestCase):
    def test_loopback(self):
        self.assertEqual(loopback(1_000_000),1_000_000)
        self.assertEqual(loopback(1_000_001), 1)
        self.assertEqual(loopback(1_100_000), 100_000)
        self.assertEqual(loopback(-5), 999_995)
        self.assertEqual(loopback(10), 10)
        self.assertEqual(loopback(0), 0)
    def test_odd(self):
        pass