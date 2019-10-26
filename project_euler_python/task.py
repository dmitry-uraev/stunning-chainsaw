"""
find the sum of all the multiples of 3 or 5 below 100
"""

def multiples(n: int) ->int:
    res = 0
    for number in range(1, n):
        if (number/5 == number//5) or (number/3 == number//3):
            res += number
    return res


"""
by considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms
"""

def Fibonacci() ->int:
    fibonacci = [1, 2]
    res = 0
    flag = True
    while flag:
        if fibonacci[-1] >= 4000000:
            fibonacci = fibonacci[:-1]
            flag = False 
            continue 
        fibonacci.append(fibonacci[-1] + fibonacci[-2])
    for element in fibonacci:
        if element/2 == element//2:
            res += element 
    return res
