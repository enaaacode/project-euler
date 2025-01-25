# Problem 23: Non-Abundant Sums
n = 28123 

abundant = [] # if sum is >
deficient = [] # if sum is < 
perfect = [] # if sum is =

for i in range(1, n):
    divisors = []
    for j in range(1, n):
        if i > j:
            if i % j == 0:
                divisor = j
                divisors.append(divisor)

    divisors_sum = sum(divisors)

    if divisors_sum > i:
        abundant.append(i)

    if divisors_sum < i:
        deficient.append(i)

    if divisors_sum == i:
        perfect.append(i)

print(abundant)
print()
print(deficient)
print()
print(perfect)