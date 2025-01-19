# Problem 20: Factorial Digit Sum

n = 100
n_lst = list(range(1, n + 1))

print(n_lst)

factorial_digit = n_lst[0]
for i in range(1, len(n_lst)):
    factorial_digit *= n_lst[i]

factorial_digit_str = str(factorial_digit)

factorial_digit_lst = []
for i in range(len(factorial_digit_str)):
    digit = int(factorial_digit_str[i])
    factorial_digit_lst.append(digit)

factorial_digit_sum = sum(factorial_digit_lst)

print(factorial_digit_sum)