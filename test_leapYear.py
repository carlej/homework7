import leapYear


def test_output(capsys):
    leapYear.LY()
    assert leapYear.LY(2020) == True
    assert leapYear.LY(2021) == False
