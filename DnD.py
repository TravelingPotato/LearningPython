import random

def roll(roll_num,sides):
    total = 0 
    while roll_num:
        total += random.randrange(1,sides+1)
        roll_num -= 1
    return total
