"""
find the sum of all the multiples of 3 or 5 below 1000
"""


def multiples(n=1000) ->int:
    res = 0
    for number in range(1, n):
        if (number/5 == number//5) or (number/3 == number//3):
            res += number
    return res


"""
by considering the terms in the Fibonacci sequence 
whose values do not exceed four million, find the sum of the even-valued terms
"""


def fibonacci(number=4000000) ->int:
    items = [[1, 2], 0, True]
    while items[2]:
        if items[0][-1] >= number:
            items[0], items[2] = items[0][:-1], False
            continue 
        items[0].append(items[0][-1] + items[0][-2])
    for element in items[0]:
        if element/2 == element//2:
            items[1] += element 
    return items[1]



