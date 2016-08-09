#!/usr/bin/env python3
# HW05_ex00_logics.py


##############################################################################
def even_odd():
    """ Print even or odd:
        Takes one integer from user
            accepts only non-word numerals
            must validate
        Determines if even or odd
        Prints determination
        returns None
    """
    try:
        user_input = int(input("Enter an integer: "))
        if user_input % 2 == 0:
            print("Even!")
        else:
            print("Odd!")
    except:
        print("Oops! The number entered is not an integer")
    return

def ten_by_ten():
    """ Prints integers 1 through 100 sequentially in a ten by ten grid."""
    current_num = 1
    for col in range(10):
        for row in range(10):
            print(current_num, end = " ")
            current_num += 1
        print()

def find_average():
    """ Takes numeric input (non-word numerals) from the user, one number
    at a time. Once the user types 'done', returns the average.
    """
    user_input = ''
    sum_numbers = 0
    count = 0
    while True:
        user_input = input("Enter the number: ")
        try:
            if user_input != 'done':
                user_input = float(user_input)
                sum_numbers += user_input
                count += 1
            elif count >= 1:
                return sum_numbers/count
            else:
                return
        except:
            print("Please enter a numeral")

##############################################################################
def main():
    """ Calls the following functions:
        - even_odd()
        - ten_by_ten()
    Prints the following function:
        - find_average()
    """
    even_odd()
    ten_by_ten()
    print(find_average())

if __name__ == '__main__':
    main()
