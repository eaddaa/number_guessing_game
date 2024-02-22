# test_main.py

from unittest import TestCase
from unittest.mock import patch
from main import guess_the_number

class TestGuessTheNumber(TestCase):
    @patch("builtins.input", side_effect=["50", "75", "80", "85", "90", "95", "97", "98", "99", "100"])
    def test_guess_the_number(self, mock_input):
        with patch("main.generate_random_number", return_value=97):
            with patch("main.print") as mock_print:
                guess_the_number()
                self.assertEqual(
                    mock_print.call_args_list,
                    [
                        ("Too low. Try again.",),
                        ("Too low. Try again.",),
                        ("Too low. Try again.",),
                        ("Too low. Try again.",),
                        ("Too low. Try again.",),
                        ("Too low. Try again.",),
                        ("Too low. Try again.",),
                        ("Too low. Try again.",),
                        ("Too low. Try again.",),
                        ("Congratulations! You guessed the number in 10 attempts.",),
                    ]
                )
