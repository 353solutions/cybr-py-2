import re

# Exercise: Have tokenize return stemmed tokens
# Make sure all tests pass


def tokenize(text):
    """Return list of tokens (lower case) found in text.

    >>> tokenize("Who's on first?")
    ['who', 's', 'on', 'first']
    """
    tokens = []
    for word in re.findall(r'[a-zA-Z]+', text):
        token = word.lower()
        token = stem(token)
        if token:
            tokens.append(token)

    return tokens


def stem(word: str):
    """Stem returns stemmed form of word

    >>> stem('working')
    'work'
    >>> stem('works')
    'work'
    >>> stem('worked')
    'work'
    """
    for suffix in ('ed', 'ing', 's'):
        if word.endswith(suffix):
            return word[: -len(suffix)]

    return word


# import doctest
# doctest.testmod(verbose=True)
