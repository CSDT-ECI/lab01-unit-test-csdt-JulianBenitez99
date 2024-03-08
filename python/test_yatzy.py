from yatzy import Yatzy

# These unit tests can be run using the py.test framework
# available from http://pytest.org/


def test_demo():
    expected = 15
    actual = 15
    assert expected == actual        

def test_chance_should_add_all():
    actual = Yatzy.chance(1,1,1,1,1)
    expected = 5
    assert expected == actual

def test_yatzy_all_equal():
    actual = Yatzy.yatzy([1,1,1,1,1])
    excepted = 50
    assert excepted == actual

def test_yatzy_different():
    actual = Yatzy.yatzy([1,1,3,1,1])
    excepted = 0
    assert excepted == actual

def test_ones():
    actual = Yatzy.ones(1,0,0,1,0)
    excepted = 2
    assert excepted == actual

def test_twos():
    actual = Yatzy.twos(2,0,2,0,0)
    excepted = 4
    assert excepted == actual

def test_threes():
    actual = Yatzy.threes(3,0,0,3,0)
    excepted = 6
    assert excepted == actual

def test_fours():
    yt = Yatzy(4,0,0,4,0)
    actual = yt.fours()
    excepted = 8
    assert excepted == actual

def test_fives():
    yt = Yatzy(5,0,5,0,0)
    actual = yt.fives()
    excepted = 10
    assert excepted == actual

def test_sixes():
    yt = Yatzy(6,6,6,0,0)
    actual = yt.sixes()
    excepted = 18
    assert excepted == actual

#def test_Pair():
#    actual = Yatzy.score_pair(3,3,3,4,4)
#    czzz = 8
#    assert excepted == actual

def test_crazy_even():
    actual = Yatzy.crazy(2,2,2,2,2)
