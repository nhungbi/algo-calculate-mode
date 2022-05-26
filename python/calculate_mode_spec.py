# Write your own unit tests here!
from calculate_mode import calculate_mode
import unittest

class ModeTest(unittest.TestCase):

    def test_num_list(self):
        self.assertEqual(calculate_mode([1,2,3,3]), [3])
        self.assertEqual(calculate_mode([4.5, 0, 0]), [0])
        self.assertEqual(calculate_mode([1.5, -1, 1, 1.5]), [1.5])
        self.assertEqual(calculate_mode([1,1,2,2]), [1,2])
        self.assertEqual(calculate_mode([1,2,3]), [1,2,3])

    def test_string_list(self):
        self.assertEqual(calculate_mode(["who", "what", "where", "who"]), ['who'])
        self.assertEqual(calculate_mode(["hi", "world", "hi", "morning"]), ['hi'])

if __name__ == '__main__':
    unittest.main()