import pytest
from twttr import shorten

def test_shorten():
    assert shorten('Wes') == 'Ws'
    assert shorten('supErCalifragiListicExpiAladocIous') == 'sprClfrgLstcxpldcs'
    assert shorten('834189352') == '834189352'
    assert shorten('aeiou') == ''
    assert shorten('AEIOU') == ''
    assert shorten('Leonard') == 'Lnrd'
