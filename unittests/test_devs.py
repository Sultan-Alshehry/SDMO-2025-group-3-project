import unittest
import sys
import os

sdmo = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, os.path.abspath(os.path.join(
    os.path.dirname(__file__), sdmo, 'src')))
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(
    __file__), sdmo, 'tools')))
import devs  # noqa: E402 (tells linter to not move this line to the top)

from devs import compute_similarity, save_csv

class TestDevs(unittest.TestCase):


    def test_compute_similarity_similar(self):
        entries = [
            ["Joni Lehto", "joni.lehto@pulla.com"],
            ["Jouni Lehti", "jouni.lehti@pulla.com"],
        ]
        table = compute_similarity(entries)
        self.assertEqual(len(table), 0)


    def test_compute_similarity_email_case(self):
        entries = [
            ["Joni Lehto", "joni.lehto@pulla.com"],
            ["Joni Lehto", "JONI.LEHTO@pulla.com"],
        ]
        table = compute_similarity(entries)
        self.assertEqual(len(table), 1)


    def test_compute_similarity_basic(self):
        entries = [
            ["Korva Puusti", "korva.puusti@gpulla.com"],
            ["Kala Keitto", "kalakeitto@mail.com"],
        ]
        table = compute_similarity(entries)
        self.assertEqual(len(table), 0)
        entries = [
            ["Kala Keitto", "kalakeitto@mail.com"],
            ["Kala Keitto", "kalakeitto@mail.com"],
        ]
        table = compute_similarity(entries)
        self.assertEqual(len(table), 1)


    def test_compute_similarity_accents(self):
        entries = [
            ["Korva Puusti", "korva.puusti@gpulla.com"],
            ["Körva Puusti", "korva.puusti@gpulla.com"],
            ["Köŕvä Ṕuusti", "korva.puusti@gpulla.com"],
        ]
        table = compute_similarity(entries)
        self.assertEqual(len(table), 0)


if __name__ == "__main__":
    unittest.main()
