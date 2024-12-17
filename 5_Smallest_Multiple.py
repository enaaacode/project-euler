# Problem 5: Smallest Multiple
# searching for the smallest number that can be divided by each of the numbers from 1 to x without any remainder

x = 20
numbers_lst = list(range(1, x + 1))

n = x  

while True:
    devided_by_all = True

    for j in numbers_lst:
        if n % j != 0:
            devided_by_all = False
            break  

    if devided_by_all:
        print(f"The smallest multiple that is divisible by all numbers from 1 to {x}: {n}")
        break

    n += x # increase n by x to improve efficiency (the smallest multiple must be a multiple of x)


