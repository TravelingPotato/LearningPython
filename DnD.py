import random

def roll(roll_num,sides):
    total = 0 
<<<<<<< HEAD
    while roll_num:
        total += random.randrange(1,sides+1)
        roll_num -= 1
=======
    for roll in range(roll_num):
        total += random.randrange(1,sides+1)
>>>>>>> 81e893a6af6f7828cb62d08037c8341f022a21c0
    return total
