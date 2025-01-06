# Problem 12: Highly Divisible Triangular Number
import copy

n = 12500
natural_numbers = list(range(1,n+1))

triangle_numbers = []

# put 1 and 1+2 in new list
one = natural_numbers[0]
triangle_numbers.append(one)
three = natural_numbers[0] + natural_numbers[1]
triangle_numbers.append(three)

for i in range(2, len(natural_numbers)): # start at 2 because of previous step
    result = natural_numbers[i] + triangle_numbers[-1]
    triangle_numbers.append(result)

print(triangle_numbers)

# - - - - - - - to slow with high numbers :-(
possible_divisors = list(range(1, triangle_numbers[-1]))

divisors_lst = []

for number in triangle_numbers:
    divisors = []
    for divisor in possible_divisors:
        if number >= divisor:
            if number % divisor == 0:
                divisors.append(divisor)
        else:
            break
    
    if len(divisors) > 500:
        divisors_lst.append(divisors)
        break


print(divisors_lst)