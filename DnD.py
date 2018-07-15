import random

def roll(roll_num,sides):
    total = 0 
    for roll in range(roll_num):
        total += random.randrange(1,sides+1)
    return total
