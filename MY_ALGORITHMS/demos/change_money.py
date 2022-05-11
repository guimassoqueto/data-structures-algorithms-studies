#! /usr/bin/python3

def change(money):
    num_coins = 0

    while money > 0:
        if money >= 10:
            money -= 10
        elif money >= 5:
            money -= 5
        else: money -= 1
        
        num_coins += 1
    return num_coins

print(change(28))

