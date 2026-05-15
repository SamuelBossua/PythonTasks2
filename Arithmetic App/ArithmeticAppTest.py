import unittest
from subtraction_quiz import generate_problem, calculate_answer, check_answer


class TestSubtractionQuiz(unittest.TestCase):

    def test_generate_problem_has_no_negative_result(self):
        for count in range(100):
            first, second = generate_problem()
            self.assertGreaterEqual(first - second, 0)

    def test_calculate_answer(self):
        self.assertEqual(calculate_answer(10, 4), 6)

    def test_check_answer_correct(self):
        self.assertTrue(check_answer(6, 6))

    def test_check_answer_wrong(self):
        self.assertFalse(check_answer(5, 6))


if __name__ == "__main__":
    unittest.main()