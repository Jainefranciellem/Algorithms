import pytest
from challenges.challenge_encrypt_message import encrypt_message


def test_encrypt_message():
    assert encrypt_message("Hello, world!", 15) == "!dlrow ,olleH"

    assert encrypt_message("Hello, world!", 6) == "!dlrow _,olleH"

    assert encrypt_message("Hello, world!", -3) == '!dlrow ,olleH'

    with pytest.raises(TypeError):
        encrypt_message("Hello, world!", "invalid")

    with pytest.raises(TypeError):
        encrypt_message(12345, 5)
