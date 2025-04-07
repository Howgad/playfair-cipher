import unittest
from playfair import playfair_cipher

class TestPlayfairCipher(unittest.TestCase):
    def test_encrypt(self):
        self.assertEqual(playfair_cipher("HELLO", "KEY", "encrypt"), "KCLTZV")

    def test_decrypt(self):
        encrypted = playfair_cipher("HELLO", "KEY", "encrypt")
        decrypted = playfair_cipher(encrypted, "KEY", "decrypt")
        self.assertEqual(decrypted[:5], "HELLO")

if __name__ == '__main__':
    unittest.main()