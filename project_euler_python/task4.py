"""
a palindromic number reads the same both ways.
the largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

find the largest palindrome made from the product of two 3-digit numbers.
"""


def _check_palindrome(number: int) ->bool:
    if str(number) == str(number)[::-1]:
        return True


def palindrome(num=3) ->int:
    start, end, boarders, all_ = '1', '10', [], []
    for n in range(num-1):
        start, end = start + '0', end + '0'
    boarders.append(int(start)), boarders.append(int(end))
    for n in range(boarders[-1], boarders[0], -1):
        for n_ in range(boarders[-1], boarders[0], -1):
            if _check_palindrome(n * n_):
                all_.append(n * n_)
    return max(all_)

