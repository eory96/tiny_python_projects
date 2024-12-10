#!/usr/bin/env python3
"""tests for crowsnest.py"""

import os
from subprocess import getstatusoutput, getoutput

prg = './crowsnest.py'
consonant_words = [
    'brigantine', 'clipper', 'dreadnought', 'frigate', 'galleon', 'haddock',
    'Junk', 'ketch', 'longboat', 'Mullet', 'narwhal', 'porpoise', 'quay',
    'regatta', 'Submarine', 'tanker', 'vessel', 'whale', 'xebec', 'yatch',
    'zebrafish', '12322'
]
vowel_words = ['aviso', 'Eel', 'Iceberg', 'octopus', 'upbound']
template = 'Ahoy, Captain, {} {} off the larboard bow!'


# --------------------------------------------------
def test_exists():
    """exists"""

    assert os.path.isfile(prg)


# --------------------------------------------------
def test_usage():
    """usage"""

    for flag in ['-h', '--help']:
        rv, out = getstatusoutput(f'{prg} {flag}')
        assert rv == 0
        assert out.lower().startswith('usage')


# --------------------------------------------------
def test_consonant():
    """brigantine -> a brigantine"""

    for word in consonant_words:
        out = getoutput(f'{prg} {word.lower()}')
        assert out.strip() == template.format('a', word.lower())


# --------------------------------------------------
def test_consonant_upper():
    """brigantine -> A Brigatine"""

    for word in consonant_words:
        out = getoutput(f'{prg} {word.title()}')
        if word[0] >='a' and word[0]<='Z':
            assert out.strip() == template.format('A', word.title())


# --------------------------------------------------
def test_vowel():
    """octopus -> an octopus"""

    for word in vowel_words:
        out = getoutput(f'{prg} {word.lower()}')
        assert out.strip() == template.format('an', word.lower())


# --------------------------------------------------
def test_vowel_upper():
    """octopus -> an Octopus"""

    for word in vowel_words:
        out = getoutput(f'{prg} {word.upper()}')
        assert out.strip() == template.format('An', word.upper())
