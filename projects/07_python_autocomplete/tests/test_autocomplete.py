import pytest
from dictionary import Dictionary

@pytest.fixture
def dictionary_from_file():
    dictionary = Dictionary()
    dictionary.load_words_from_file('./words_alpha.txt')
    return dictionary

@pytest.fixture
def dictionary_simple():
    dictionary = Dictionary()
    dictionary.load_words(['hello', 'world'])
    return dictionary

@pytest.fixture
def dictionary_complete():
    dictionary = Dictionary()
    dictionary.load_words(['harehearted', 'harehound','hello', 'world'])
    return dictionary

def test_load_words(dictionary_from_file):
    assert dictionary_from_file.words == 370103

def test_check_word(dictionary_simple):
    assert dictionary_simple.check_word('hello')
    assert dictionary_simple.check_word('world')
    assert not dictionary_simple.check_word('hell')
    assert not dictionary_simple.check_word('worldy')
    assert not dictionary_simple.check_word('worldly')
    assert not dictionary_simple.check_word('w')

def test_get_words(dictionary_simple):
    assert dictionary_simple.get_words() == ['hello', 'world']

def test_complete_word(dictionary_complete):
    assert dictionary_complete.complete_word('hareh') == ['harehearted', 'harehound']
    assert dictionary_complete.complete_word('zq') == []

def test_complete_word_large_dictionary(dictionary_from_file):
    words = dictionary_from_file.complete_word('hes')
    assert len(set(words)) == len(words) 

