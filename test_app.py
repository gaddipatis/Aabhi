import unittest

from app import app, sum_integers


class TestSumIntegers(unittest.TestCase):
    def test_positive_numbers(self):
        self.assertEqual(sum_integers(3, 5), 8)

    def test_negative_numbers(self):
        self.assertEqual(sum_integers(-4, -6), -10)

    def test_mixed_signs(self):
        self.assertEqual(sum_integers(10, -3), 7)

    def test_zero(self):
        self.assertEqual(sum_integers(0, 0), 0)


class TestIndexRoute(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()

    def test_get_returns_form(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Integer Sum Calculator", response.data)

    def test_post_valid_integers(self):
        response = self.client.post(
            "/",
            data={"num1": "12", "num2": "30"},
        )
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"12 + 30 = 42", response.data)

    def test_post_negative_integers(self):
        response = self.client.post(
            "/",
            data={"num1": "-5", "num2": "8"},
        )
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"-5 + 8 = 3", response.data)

    def test_post_invalid_input(self):
        response = self.client.post(
            "/",
            data={"num1": "abc", "num2": "10"},
        )
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Please enter valid integers in both fields.", response.data)

    def test_post_empty_fields(self):
        response = self.client.post(
            "/",
            data={"num1": "", "num2": "10"},
        )
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Please enter valid integers in both fields.", response.data)


if __name__ == "__main__":
    unittest.main()
