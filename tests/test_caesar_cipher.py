import pytest
from caesar_cipher import __version__
from caesar_cipher.caesar_cipher import Caesar


def test_version():
    assert __version__ == '0.1.0'
