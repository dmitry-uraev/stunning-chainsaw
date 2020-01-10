"""
the sum of the squares of the first ten natural numbers is 385
the square of the sum of the first ten natural numbers is 3025

hence the difference between the sum of the squares of the first ten natural numbers
    and the square of the sum is 3025−385=2640.

find the difference between the sum of the squares
    of the first one hundred natural numbers and the square of the sum.
"""


def sum_square_difference(number1: int, number2: int) ->int:
    sum_sqrt, sqrt_sum = 0, 0
    for number in range(number1, number2+1):
        sum_sqrt += number * number
        sqrt_sum += number
    return sqrt_sum*sqrt_sum-sum_sqrt  # 1-100 = 25164150 - quite quick; 1-10 = 2640 - fine;
