# Problem 1: Multiples of 3 or 5 

# create list with all the natural numbers below x

x = 100

numbers_lst = list(range(1, x))

# check which numbers in numbers_lst are multiples of 3 or 5

multiples_lst = []

for number in numbers_lst:
    if number % 3 == 0:
        multiples_lst.append(number)
    elif number % 5 == 0:
        multiples_lst.append(number)

# sum of all the multiples

sum_of_multiples = sum(multiples_lst)

print(f"This are our numbers below {x}: {numbers_lst}")
print(f"This are our multiples of 3 and 5: {numbers_lst}")
print(f"The sum of all the multiples is: {sum_of_multiples}")