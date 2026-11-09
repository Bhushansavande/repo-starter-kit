import unittest

from your_project import greet
from your_project.cli import main


class GreetTests(unittest.TestCase):
    def test_greets(self):
        self.assertEqual(greet(" Asha "), "Hello, Asha!")

    def test_rejects_empty(self):
        with self.assertRaises(ValueError):
            greet("  ")

    def test_cli_error_code(self):
        self.assertEqual(main(["   "]), 2)


if __name__ == "__main__":
    unittest.main()
