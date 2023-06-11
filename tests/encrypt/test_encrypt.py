import pytest
from challenges.challenge_encrypt_message import encrypt_message


def test_encrypt_message():
    with pytest.raises(TypeError):
        encrypt_message(0, "string")
    assert encrypt_message("teste", -1) == "etset"
    assert encrypt_message("teste", 1) == "t_etse"
