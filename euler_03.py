# Problem 3: Largest Prime Factor
# we are looking for the biggest prime factor in 600851475143

n = 1346
#600851

# create a list with prime numbers
# there is a algorithm to determine the prime numbers called "Sieve of the Eratosthenes" (Sieb des Eratosthenes)

numbers = list(range(2,n+1)) # start at 2 because 1 is not a prime number
prime_numbers_lst = numbers 

list_counter = 0
for i in range(1, len(numbers)):
    if i < len(numbers):
        if numbers[i] % numbers[list_counter] == 0:
            prime_numbers_lst.remove(numbers[i])
            list_counter += 1

# print(prime_numbers_lst)

# find the prime factors of n

prime_factors_of_n = []
still_calculating = True

counter = 0
divided_n = n

while still_calculating:

    if counter < len(prime_numbers_lst):

        if divided_n % prime_numbers_lst[counter] == 0:
            divided_n = divided_n / prime_numbers_lst[counter] 
            prime_factors_of_n.append(prime_numbers_lst[counter]) 

        else:
            counter += 1
        
    if divided_n == 1:
        still_calculating = False

print(f"This are the prime factors of {n}: {prime_factors_of_n}")
print(f"This is the biggest one: {prime_factors_of_n[-1]}")
