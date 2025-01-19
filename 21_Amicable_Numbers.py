# Problem 21: Amicable Numbers
import copy

def sum_of_divisors(num):
    divisors = []
    for i in range(1, num):
        if num % i == 0:
            divisors.append(i)
    return sum(divisors)

n = 10000
number_lst = list(range(1, n))
checked_numbers = copy.deepcopy(number_lst)

amicable_numbers = []

while len(checked_numbers) > 0:

    for number in number_lst:
        divisors_sum_a = sum_of_divisors(number)  
        b = divisors_sum_a
        divisors_sum_b = sum_of_divisors(b)

        if number != b and number == divisors_sum_b:

            amicable_numbers.append(number)
            #amicable_numbers.append(divisors_sum_b)
            checked_numbers.remove(number)
            if divisors_sum_b in checked_numbers:
                checked_numbers.remove(divisors_sum_b)
        
        else:
            checked_numbers.remove(number)

print(sum(amicable_numbers))
print(amicable_numbers)

