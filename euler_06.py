# Problem 6: Sum Square Difference

# create list with x numbers

x = 100 

numbers_lst = [] # list(range(1, x + 1))

for i in range(1, x + 1):
    numbers_lst.append(i)

# a) sum of the squares of the first x natural numbers

squares_lst = []

for number in numbers_lst:
    square = number * number
    squares_lst.append(square)

sum_of_squares = sum(squares_lst)

# b) square of the sum of the first x natural numbers 

square_of_sum = sum(numbers_lst) * sum(numbers_lst)

# difference between b) and a)

difference = square_of_sum - sum_of_squares

print(f"This are our numbers: {numbers_lst}")
print(f"The sum of their squares is: {sum_of_squares}")
print(f"The square of their sum is: {square_of_sum}")
print(f"The difference between them is: {difference}")
