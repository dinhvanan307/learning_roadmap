# Example from python/08-debug-test-environment.md; keep in sync with the lesson.
import unittest

def normalize_title(value):
    if not isinstance(value, str):
        raise TypeError("title must be text")
    result = value.strip()
    if not result:
        raise ValueError("title must not be empty")
    return result

class TitleTests(unittest.TestCase):
    def test_trims_whitespace(self):
        self.assertEqual(normalize_title("  Python  "), "Python")

    def test_rejects_blank(self):
        for value in ("", "   ", "\n"):
            with self.subTest(value=value):
                with self.assertRaises(ValueError):
                    normalize_title(value)

    def test_rejects_wrong_type(self):
        for value in (None, 123, True):
            with self.subTest(value=value):
                with self.assertRaises(TypeError):
                    normalize_title(value)

if __name__ == "__main__":
    unittest.main(verbosity=2)
