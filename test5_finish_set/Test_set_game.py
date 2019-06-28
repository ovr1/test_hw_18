import set_igra
import pytest

cards1 = [['3', 'OVAL', 'SOLID', 'RED'], ['3', 'OVAL', 'OPEN', 'GREEN'], ['3', 'SQUIGGLE', 'OPEN', 'RED']]
# set True
#cards2 = [['3', 'OVAL', 'STRIPPED', 'PURPLE'], ['1', 'OVAL', 'OPEN', 'PURPLE'], ['2', 'DIAMOND', 'STRIPPED', 'RED']
# set False


def test_check_set():
    assert set_igra.check_set(cards1) == True,bool

