# Problem 3: Largest Prime Factor
# we are looking for the biggest prime factor in 600851475143

number = 600851475143

# - - - create a list with prime numbers - - -
n = 10000 
all_n = list(range(2,int(n+1)))
prime_numbers = []

while len(prime_numbers) < 1000:

    l = [] # put the first entry from all_n in l 
    l.append(all_n[0]) # this is the prime number we want to create multiples of
    prime_numbers.append(all_n[0])
    del all_n[0] # delete it from all_n
    
    for multiplicator in range(2, int(n/2)):
        result = multiplicator * l[0]
        if result > n:
            break
        else:
            l.append(result)

    # remove the entries in l from all_n
    for entry in l:
        if entry in all_n:
            all_n.remove(entry)

    l.clear() # clear l to start over again with the next all_n[0]

print(prime_numbers)

# - - - find the prime factors of number - - -

prime_factors = []
still_calculating = True

counter = 0

while still_calculating:

    if counter < len(prime_numbers):

        if number % prime_numbers[counter] == 0:
            number = number / prime_numbers[counter]
            if number not in prime_factors: 
                prime_factors.append(prime_numbers[counter]) 

        else:
            counter += 1
        
    if number == 1:
        still_calculating = False

print(f"This are the prime factors of {number}: {prime_factors}")
print(f"This is the biggest one: {prime_factors}")
