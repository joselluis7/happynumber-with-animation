"""
Module to verify if such given number is a happy number or not.

"""

#: Happy number are natural numbers which the sum of
#: His digits results in one.
#: Eg. 7 = 7*7 = 49 = 4*4 + 9*9 = 97 = 9*9 + 7*7 = 130 = 1*1 + 3*3 + 0*0 = 10 = 1*1 + 0*0 = 1
#:

def sum_squares(num):
    """get the sum of squares 

    args:
        num {int} -- num given by user to get sum of his digits
    retunt: 
        sum {int} -- sum of sqares of num digits

    """
    sum = rem = 0
    while num > 0:
        rest = num%10
        sum += rest**2
        num=num//10
    return sum


def is_happy_number(num):
    """Function that checks if the given number is happy
    args:
        num {int} -- num given to check if is happy
    retunt: 
         {boolean} -- True if number is happy, False if not
    """
    
    while( num != 1 and num != 4):
        num = sum_squares(num)

    if num == 1:
        print(num)
        return True
    else:
        return False


print(is_happy_number(7))