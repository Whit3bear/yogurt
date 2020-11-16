""" Task

Given the birthdates of two people, find the date when the younger one is exactly half the age of the other.
Notes

    The dates are given in the format YYYY-MM-DD and are not sorted in any particular order
    Round down to the nearest day
    Return the result as a string, like the input dates

 """

import datetime
def half_life(person1, person2):
    y1, m1, d1 = list(map(int, min(person1, person2).split('-')))
    y2, m2, d2 = list(map(int, max(person1, person2).split('-')))
    delta = datetime.date(y2, m2, d2) - datetime.date(y1, m1, d1)
    return str(datetime.date(y2, m2, d2) + delta)