import unittest
import sys
import os

sdmo = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, os.path.abspath(os.path.join(
    os.path.dirname(__file__), sdmo, 'src')))
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(
    __file__), sdmo, 'tools')))

from devs import compute_similarity

class TestDevs(unittest.TestCase):


    def test_compute_similarity_c4(self):
        entries = [
            ["Korva Puusti", "korva.puusti@pulla.com"],
            ["Koira Musti", "kpuusti@pulla.com"],
        ]
        table = compute_similarity(entries)
        boolean = table["c4"].iloc[0]
        self.assertEqual(len(table), 1)
        self.assertTrue(boolean)

    def test_compute_similarity_c4_false(self):
        entries = [
            ["Korva Puusti", "korva.puusti@pulla.com"],
            ["Koira Musti", "koiramusti@pulla.com"],
        ]
        table = compute_similarity(entries)
        boolean = table["c4"].iloc[0]
        self.assertFalse(boolean)


    def test_compute_similarity_c5(self):
        entries = [
            ["Korva Puusti", "korva.puusti@pulla.com"],
            ["Koira Musti", "korvap@pulla.com"],
        ]
        table = compute_similarity(entries)
        boolean = table["c5"].iloc[0]
        self.assertEqual(len(table), 1)
        self.assertTrue(boolean)


    def test_compute_similarity_c6(self):
        entries = [
            ["Korva Puusti", "kmusti@pulla.com"],
            ["Koira Musti", "koira.musti@pulla.com"],
        ]
        table = compute_similarity(entries)
        boolean = table["c6"].iloc[0]
        self.assertEqual(len(table), 1)
        self.assertTrue(boolean)


    def test_compute_similarity_c7(self):
        entries = [
            ["Korva Puusti", "koiram@pulla.com"],
            ["Koira Musti", "koira.musti@pulla.com"],
        ]
        table = compute_similarity(entries)
        boolean = table["c7"].iloc[0]
        self.assertEqual(len(table), 1)
        self.assertTrue(boolean)


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

    def test_compute_similarity_email_case(self):
        entries = [
            ["Joni Lehto", "joni.lehto@pulla.com"],
            ["Joni Lehto", "JONI.LEHTO@pulla.com"],
        ]
        table = compute_similarity(entries)
        self.assertEqual(len(table), 1)


if __name__ == "__main__":
    unittest.main()
