import pytest
from challenges.challenge_encrypt_message import encrypt_message


def test_encrypt_message_reversed():
    message = "Hello, world!"
    key = 15
    expected = "!dlrow ,olleH"
    assert encrypt_message(message, key) == expected


def test_encrypt_message_two_parts():
    message = "Hello, world!"
    key = 6
    expected = "!dlrow _,olleH"
    assert encrypt_message(message, key) == expected


def test_encrypt_message_odd_key():
    message = "Hello, world!"
    key = 7
    expected = " ,olleH_!dlrow"
    assert encrypt_message(message, key) == expected


def test_encrypt_message_invalid_key_type():
    message = "Hello, world!"
    key = "invalid"
    with pytest.raises(TypeError):
        encrypt_message(message, key)


def test_encrypt_message_invalid_message_type():
    message = 12345
    key = 5
    with pytest.raises(TypeError):
        encrypt_message(message, key)
