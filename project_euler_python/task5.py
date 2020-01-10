"""
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

what is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
"""


def divide_range(number1: int, number2: int) ->int:
    number = number2 * number2
    non_stop = True
    while non_stop:
        number += 10
        for element in range(number1, number2):
            if number % element == 0:
                non_stop = False
            else:
                non_stop = True
                break
    return number  # 1-20 = 232792560 - long processing # 1-10 = 2520 works just fine;
#  quite quick if i+=10 not i+=1 - reasonable;
