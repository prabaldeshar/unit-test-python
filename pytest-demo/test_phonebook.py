import pytest

from phonebook import Phonebook
# from .phonebook import Phonebook

@pytest.fixture
def phonebook_typo(tmpdir):
    return Phonebook(tmpdir)
    

def test_lookup_by_name(phonebook_typo):
    phonebook_typo.add("Bob", "1234")
    assert "1234" == phonebook_typo.lookup("Bob")

def test_phonebook_contains_all_names(phonebook_typo):
    phonebook_typo.add("Bob", "12345")
    assert "Bob" in phonebook_typo.names()

def test_missing_name_raises_error(phonebook_typo):
    phonebook_typo.add("Bob", "12345")
    with pytest.raises(KeyError):
        phonebook_typo.lookup("ABC")