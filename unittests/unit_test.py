import unittest
import sys
import os
sdmo = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, os.path.abspath(os.path.join(
    os.path.dirname(__file__), sdmo, 'src')))
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(
    __file__), sdmo, 'tools')))
import devs  # noqa: E402 (tells linter to not move this line to the top)


class TestDevs(unittest.TestCase):

    def test_import_repository(self):

        repo = ["name,email", "GitHub,noreply@github.com",
                "Jenni-Maria-Juurikka,jenni.juurikka@hotmail.com",
                "PetriPe,petri.pentinpuro@student.oulu.fi",
                "Sultan-Alshehry,192121920+Sultan-Alshehry@users.noreply.github.com",
                "elossa2000,163442413+elossa2000@users.noreply.github.com",
                "rtervo22,riina.tervo@student.oulu.fi",
                "ttorp22,144235906+ttorp22@users.noreply.github.com"]
        repository_name = \
            "https://github.com/Sultan-Alshehry/SDMO-2025-group-3-project"
        devs.import_repository(repository_name)
        i = 0
        with open(os.path.join("devs", "devs.csv"), 'r') as file:
            for line in file:
                self.assertEqual(repo[i], line.strip())
                i += 1


if __name__ == '__main__':
    unittest.main()
