#! /bin/python3

from math import floor

def change_money(money: int) -> int:
    return floor(money / 10) + floor((money % 10)/5) + (money % 5)

