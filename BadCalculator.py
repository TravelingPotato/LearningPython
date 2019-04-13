# File: BadCalculator.py
# Name: Taylor Anderson
# Date: 4/13/2019
# Course: DSC 510
# Assignment: Week 5
# Summary: Allows a user to add, subtract, multiply, divide, or average numbers


# Request an operation and two numbers. Then performs the operation on this two numbers.
def performCalculation(operation):

    ops = ['+', '-', '*', '/']  # list acceptable operations

    if operation in ops:  # check for valid operation

        while True:
            try:
                num1 = float(input('What is the first number?\n'))   # Request the first number
                num2 = float(input('What is the second number?\n'))  # Request the second number

                if operation == '/' and num2 == 0:  # Check that we are not dividing by zero
                    print('Error: You cannot divide by zero')
                else:
                    break

            except ValueError:
                print('That is not a number. Try again.')     # Loop if the user does not give a number

        if operation == '+':
            return num1 + num2               # Add the numbers
        elif operation == '-':
            return num1 - num2               # Subtract the numbers
        elif operation == '*':
            return num1 * num2               # Multiply the numbers
        elif operation == '/':
            return num1 / num2               # Divide if num2 is not 0

    else:
        print('That is not a valid operation.')


# Calculates the average of user entered numbers
def calculateAverage():

    total = 0

    while True:
        try:
            # Determine how many numbers to average
            count = int(input('How many numbers would you like to average?\n'))

            # Check that the number is greater than zero
            if count > 0:
                break
            else:
                print('Number must be greater than zero.')

        except ValueError:  # Check that the input is a number
            print('That is not a number. Try again.')

    # Request numbers and add them together
    for i in range(count):
        while True:
            try:
                num = float(input(f'Enter number {i+1}\n'))  # Request each number
                break
            except ValueError:  # Check that input is a number
                print('That is not a number. Try again.')

        total += num

    return total/count  # Calculate are return the average


def main():
    print('Welcome to Bad Calculator')
    while True:

        # Ask for which function the user wants to use or quit
        request = input(
            "***********************************************************\n"
            "Enter 'c' to add, subtract, multiply, or divide two numbers\n"
            "Enter 'a' to average numbers\n"
            "Enter any other value to quit\n"
            "***********************************************************\n")

        if request == 'c':  # Use performCalculation function
            calc = performCalculation(input('What operation do you want to use?\n'))
            if calc is not None:  # Checks if an error occurred. If not, print the result.
                print(f'The result of your operation is: {calc}')
        elif request == 'a':  # Use calculateAverage function
            print(f'The average of your numbers is: {calculateAverage()}')
        else:
            print('Thank you for using Bad Calculator')  # Exits
            break


main()
