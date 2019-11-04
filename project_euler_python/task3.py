import math

"""
what is the largest prime factor of the number 600851475143?
"""


def prime_factor(num=600851475143):
    items = [math.ceil(math.sqrt(num)), []]
    for number in range(3, items[0]):
        if num % number == 0:
            if not prime_factor(number):
                items[1].append(number)
    try:
        return max(items[1])
    except ValueError:
        return items[1]
