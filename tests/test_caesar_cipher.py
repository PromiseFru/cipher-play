"""Test Module"""

import pytest
from ciphers.caesar_cipher import caesar_encrypt, caesar_decrypt

@pytest.mark.parametrize("plaintext, shift, expected", [
    ("HELLO", 3, "KHOOR"),
    ("hello", 3, "khoor"),
    ("abc", -3, "xyz"),
    ("xyz", 3, "abc"),
    ("HELLO, WORLD!", 3, "KHOOR, ZRUOG!"),
    ("HELLO", 26, "HELLO"),
    ("hello", 0, "hello"),
    ("HELLO", 29, "KHOOR")
])
def test_encrypt(plaintext, shift, expected):
    assert caesar_encrypt(plaintext, shift) == expected

@pytest.mark.parametrize("ciphertext, shift, expected", [
    ("KHOOR", 3, "HELLO"),
    ("khoor", 3, "hello"),
    ("xyz", -3, "abc"),
    ("abc", 3, "xyz"),
    ("KHOOR, ZRUOG!", 3, "HELLO, WORLD!"),
    ("HELLO", 26, "HELLO"),
    ("hello", 0, "hello"),
    ("KHOOR", 29, "HELLO")
])
def test_decrypt(ciphertext, shift, expected):
    assert caesar_decrypt(ciphertext, shift) == expected
