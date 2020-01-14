"""
by listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

what is the 10 001st prime number?
"""


def prime_number_by_position(position: int) ->int:
    pos, number = 0, 1
    while pos != position:
        number += 1
        if check_prime(number):
            pos += 1
    return number  # quite slow, but acceptable and working right 10001st is 104743
# might be quicker if skip some numbers while iterating 


def check_prime(number: int) ->bool:
    for num in range(1, number):
        if num != 1 and num != number:
            if number/num == number//num:
                return False
    return True
