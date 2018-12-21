import unittest
import ask_lib


class TestAnswerReturn(unittest.TestCase):
    def test_return_name(self):
        original_raw_input = __builtins__.raw_input
        __builtins__.raw_input = lambda _: 'Marc'
        self.assertEqual(ask_lib.ask_name(), 'Thank you, Marc.')
        __builtins__.raw_input = original_raw_input

    def test_multiply_nums(self):
        self.assertEqual(ask_lib.multiply_nums(2,3), 6, "Should be 6")

if __name__ == "__main__":
    unittest.main()
    print("Everything passed")