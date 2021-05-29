import leapYear


def test_output():
    assert leapYear.LY(2020) == True
    assert leapYear.LY(2021) == False

def test_4and100():
    assert leapYear.LY(100) == False
