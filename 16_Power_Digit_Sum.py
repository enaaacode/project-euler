# Problem 16: Power Digit Sum

number = 2**1000
number_as_str = str(number)

digits_of_number = []
for i in range(len(number_as_str)):
    digit = int(number_as_str[i])
    digits_of_number.append(digit)

power_digit_sum = sum(digits_of_number)
print(power_digit_sum)
