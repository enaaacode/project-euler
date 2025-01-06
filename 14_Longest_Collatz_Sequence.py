# Problem 14: Longest Collatz Sequence

def n_is_even(number):
    res = number/2
    return int(res)

def n_is_odd(number):
    res = number * 3 + 1
    return int(res)

longest_collatz_sequenz = []
starting_number = 0

for number in range(1,1000000+1):
    collatz_sequenz = []
    if number % 2 == 0:
        collatz_sequenz.append(n_is_even(number))
    else:
        collatz_sequenz.append(n_is_odd(number))

    while collatz_sequenz[-1] != 1:
        
        if collatz_sequenz[-1] % 2 == 0:
            collatz_sequenz.append(n_is_even(collatz_sequenz[-1]))
        else:
            collatz_sequenz.append(n_is_odd(collatz_sequenz[-1]))

    if len(collatz_sequenz) > len(longest_collatz_sequenz):
        longest_collatz_sequenz = collatz_sequenz
        starting_number = number

print(starting_number)
print(longest_collatz_sequenz)
