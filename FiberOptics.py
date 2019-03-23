# File: FiberOptics.py
# Name: Taylor Anderson
# Date: 3/22/2019
# Course: DSC 510
# Assignment: Week 2
# Purpose: Retrieves company name and length of fiber optic, calculates cost, prints receipt

print('Welcome to Fiber Tech! The leading supplier of fiber optics.')
company = input('What is the name of your company?\n')

while True:  # Retrieves length in feet and checks for ValueError
    try:
        length = int(input('How many feet of fiber optic cable would {} like to purchase?\n'.format(company)))
        break
    except ValueError:
        print('Oops! That is not a number.')

cable_cost = 0.87  # Cost of cable in $US
total_cost = length*cable_cost  # Total cost in $US

print('Thank you for your purchase {}!'.format(company))  # Print receipt
print('Length of cable: {} feet'.format(length))
print('Total cost of installation: ${}'.format(total_cost))
