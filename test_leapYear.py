import leapYear


def test_output():
    assert leapYear.LY(2020) == True
    assert leapYear.LY(2021) == False
