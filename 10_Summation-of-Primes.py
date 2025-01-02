# Problem 10: Summation of Primes
mio = 1000000
n = 2*mio

def sieve_of_eratosthenes(n):
    primes = [True] * (n + 1)
    primes[0] = primes[1] = False  # 0 and 1 are no prime numbers
    
    for i in range(2, int(n ** 0.5) + 1):  # root of n for the biggest possible prime number
        if primes[i]:  
            for j in range(i * i, n + 1, i):  
                primes[j] = False

    prime_numbers = []
    for i in range(2, n + 1):
        if primes[i] == True:
            prime_numbers.append(i)
    
    return prime_numbers

print(sum(sieve_of_eratosthenes(n)))
