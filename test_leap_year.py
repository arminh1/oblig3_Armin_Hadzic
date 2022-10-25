from leap_year import isLeapYear

def test_if_number_is_leap_year():
    assert isLeapYear(2000)

def test_if_number_is_not_leap_year():
    assert not isLeapYear(1700)

def test_if_divisible_by_four():
    assert isLeapYear(4)

def test_if_divisible_by_four_hundred():
    assert isLeapYear(400)

def test_if_not_divisible_by_4():
    assert not isLeapYear(3)

def test_if_divisible_by_hundred_not_four_hundred():
    assert not isLeapYear(100)





























