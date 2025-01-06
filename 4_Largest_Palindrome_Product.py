# Problem 4: Largest Palindrome Product
# A palindromic number reads the same both ways.

# create a list with numbers from y to X

y = 100
x = 999
digit = len(str(x))

numbers_lst = list(range(y, x + 1)) # +1 because off by one
#print(numbers_lst)

# multiply each number with each number

multiply_lst = []

for i in range(len(numbers_lst)):
    for j in range(len(numbers_lst)):
        multiply_lst_entry = []
        multiply_lst_entry.append(numbers_lst[i])
        multiply_lst_entry.append(numbers_lst[j])
        multiply = numbers_lst[i] * numbers_lst[j]
        multiply_lst_entry.append(multiply)
        multiply_lst.append(multiply_lst_entry)

'''for i in range(len(multiply_lst)):
    print(multiply_lst[i])'''

# find palindromes 

palindrome_lst = []

for i in range(len(multiply_lst)):
    number = list(str(multiply_lst[i][2])) 
    reversed_number = list(reversed(str(multiply_lst[i][2]))) # the reversed method only works with strings and it returns a crazy format -> this is why i make a list 
    if number == reversed_number:
        palindrome_lst.append(multiply_lst[i][2])

'''for i in range(len(palindrome_lst)):
    print(palindrome_lst[i])'''

# find largest palindrome

largest = max(palindrome_lst)
print()
print(f"This is the largest palindrome made from the product of {digit}-digit numbers: {largest}")
print()