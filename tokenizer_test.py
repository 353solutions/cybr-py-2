"""
pytest search for files starting with test_*.py or *_test.py

I prefer *_test.py since then on the explorer you see the file being tested and
the test next to each other.

Inside each file, pytest looks for functions starting with test_ and will run them.

$ python -m pytest -v

To start a debugger on failing test
$ python -m pytest -v --pdb

TDD: Test Driven Development: First write a failing test, then write code to pass the test.
"""

import tokenizer

import pytest


# Empty test, still useful for catching syntax error, missing modules ...
def test_smoke():
    pass


def test_tokenize():
    text = "Who's on first?"
    tokens = tokenizer.tokenize(text)

    assert tokens == ['who', 'on', 'first']


def test_stem():
    word = 'working'
    stem = tokenizer.stem(word)
    assert stem == 'work'


stem_cases = [
    # word, step
    ('worked', 'work'),
    ('working', 'work'),
    ('works', 'work'),
    ('work', 'work'),
    ('', ''),
    ('s', ''),
]


# function parameter names must match names in parametrize decorator
@pytest.mark.parametrize('word, stem', stem_cases)
def test_stem_many(word, stem):
    out = tokenizer.stem(word)
    assert out == stem
