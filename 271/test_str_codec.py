import unittest
from str_codec import encode, decode

def helper(strings: list[str]) -> bool:
    encoded = encode(strings)
    decoded = decode(encoded)
    return strings == decoded

class TestStrCodec(unittest.TestCase):

    def test_encode_return_type(self):
        val = encode(['one', 'two', 'three'])
        self.assertIsInstance(val, str)
    
    def test_case_empty(self):
        arg = []
        self.assertEqual(arg, decode(encode(arg)))
    
    def test_single_string(self):
        arg = ['single']
        self.assertEqual(arg, decode(encode(arg)))
    
    def test_multiple_strings(self):
        arg = ['one', 'two', 'three']
        self.assertEqual(arg, decode(encode(arg)))
    
    def test_contains_delimiter(self):
        arg = ['one', '#two', '23#three']
        self.assertEqual(arg, decode(encode(arg)))



if __name__ == '__main__':
    unittest.main()