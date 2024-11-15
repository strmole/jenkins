# test_email_validator.py

from email_validator import is_valid_email

def test_valid_emails():
    assert is_valid_email("test@example.com") == True
    assert is_valid_email("user.name+tag+sorting@example.com") == True
    assert is_valid_email("user@sub.domain.com") == True

def test_invalid_emails():
    assert is_valid_email("plainaddress") == False
    assert is_valid_email("missing_at_sign.com") == False
    assert is_valid_email("missing@domain") == False
