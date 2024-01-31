import pytest
from pass_generator import generate_password

def test_generate_password_valid_input():
    password = generate_password("capivara", "friends", "12062022", "outubro")
    assert len(password) == 8

def test_generate_password_empty_input():
    with pytest.raises(ValueError):
        generate_password("", "friends", "12062022", "outubro")
        generate_password("capivara", "", "12062022", "outubro")
        generate_password("capivara", "friends", "", "outubro")
        generate_password("capivara", "friends", "12062022", "")

def test_generate_password_invalid_input():
    with pytest.raises(ValueError):
        generate_password(None, "friends", "12062022", "outubro")
        generate_password("capivara", None, "12062022", "outubro")
        generate_password("capivara", "friends", None, "outubro")
        generate_password("capivara", "friends", "12062022", None)

