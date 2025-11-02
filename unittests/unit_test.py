import unittest
import sys
import os
sdmo = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, os.path.abspath(os.path.join(
    os.path.dirname(__file__), sdmo, 'src')))
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(
    __file__), sdmo, 'tools')))
import devs  # noqa: E402 (tells linter to not move this line to the top)


developers = [
    "name,email",
    "GitHub,noreply@github.com",
    "Jenni-Maria-Juurikka,jenni.juurikka@hotmail.com",
    "PetriPe,petri.pentinpuro@student.oulu.fi",
    "Sultan-Alshehry,192121920+Sultan-Alshehry@users.noreply.github.com",
    "elossa2000,163442413+elossa2000@users.noreply.github.com",
    "rtervo22,riina.tervo@student.oulu.fi",
    "ttorp22,144235906+ttorp22@users.noreply.github.com"]


class TestDevs(unittest.TestCase):

    def test_import_repository(self):

        repository_name = \
            "https://github.com/Sultan-Alshehry/SDMO-2025-group-3-project"
        devs.import_repository(repository_name)
        i = 0
        with open(os.path.join("devs", "devs.csv"), 'r') as file:
            for line in file:
                self.assertEqual(developers[i], line.strip())
                i += 1

    def test_read_developers(self):

        dev_list = [
            ['GitHub', 'noreply@github.com'],
            ['Jenni-Maria-Juurikka', 'jenni.juurikka@hotmail.com'],
            ['PetriPe', 'petri.pentinpuro@student.oulu.fi'],
            ['Sultan-Alshehry', '192121920+Sultan-Alshehry@users.noreply.github.com'],
            ['elossa2000', '163442413+elossa2000@users.noreply.github.com'],
            ['rtervo22', 'riina.tervo@student.oulu.fi'],
            ['ttorp22', '144235906+ttorp22@users.noreply.github.com']
        ]
        self.assertEqual(devs.read_developers(), dev_list)

    def test_process(self):
        test_cases = [
            (("", ""), ("", "", "", "", "", "", ""), ("empty index error")),
            (("", "something@bloop.com"), ("", "", "", "", "",
             "something@bloop.com", "something"), ("no name error")),
            (("bob bleep", ""), ("bob bleep", "bob",
             "bleep", "b", "b", "", ""), ("no email error")),
            (("äöæø}", "hi@mailer.com"), ("aoæø", "aoæø",
             "", "a", "", "hi@mailer.com", "hi"), ("weird chars error")),
            (("john pork", "asdflj@mailing.com"), ("john pork", "john", "pork",
             "j", "p", "asdflj@mailing.com", "asdflj"), ("normal case error"))
        ]

        for idx, (input_data, expected_output, error_msg) in enumerate(test_cases):
            with self.subTest(msg=f"Test case {idx}: {error_msg}"):
                result = devs.process(input_data)
                self.assertEqual(result, expected_output, f"Test {
                                 idx} failed: {error_msg}")
                
    def test_compute_similarity_c1(self):
        entries = [
            ["Korva Puusti", "korva.puusti@pulla.com"],
            ["Kora Puusti", "korva.puusti@pulla.com"],
        ]
        table = devs.compute_similarity(entries)
        boolean = table["c1"].iloc[0]
        self.assertTrue(boolean)

    def test_compute_similarity_c2(self):
        entries = [
            ["Korva Puusti", "korva.puusti@pulla.com"],
            ["Korva Puusti", "koira.musti@pulla.com"],
        ]
        table = devs.compute_similarity(entries)
        boolean = table["c2"].iloc[0]
        self.assertTrue(boolean)

    def test_compute_similarity_c2_length_exact(self):
        short_entries = [
            ["Koor", "korva.puusti@pulla.com"],
            ["Koor", "koira.musti@pulla.com"],
        ]
        table = devs.compute_similarity(short_entries)
        boolean = table["c2"].iloc[0]
        self.assertFalse(boolean)

    def test_compute_similarity_c2_short(self):
        short_entries = [
            ["Kor", "korva.puusti@pulla.com"],
            ["Kor", "koira.musti@pulla.com"],
        ]
        table = devs.compute_similarity(short_entries)
        boolean = table["c2"].iloc[0]
        self.assertFalse(boolean)

    def test_compute_similarity_c2_longer(self):
        short_entries = [
            ["Korva", "korva.puusti@pulla.com"],
            ["Korva", "koira.musti@pulla.com"],
        ]
        table = devs.compute_similarity(short_entries)
        boolean = table["c2"].iloc[0]
        self.assertTrue(boolean)


    def test_compute_similarity_basic(self):
        entries = [
            ["Kala Keitto", "kalakeitto@mail.com"],
            ["Kala Keitto", "kalakeitto@mail.com"],
        ]
        table = devs.compute_similarity(entries)
        self.assertEqual(len(table), 1)
        row =  table.iloc[0]
        self.assertEqual(row["name_1"], "Kala Keitto")
        self.assertEqual(row["name_2"], "Kala Keitto")
        self.assertEqual(row["email_1"], "kalakeitto@mail.com")
        self.assertEqual(row["email_2"], "kalakeitto@mail.com")

if __name__ == '__main__':
    unittest.main()
