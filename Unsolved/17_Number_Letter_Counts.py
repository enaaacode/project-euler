# Problem 17: Number Letter Counts
import copy

numbers_dict = {1: "one", 2: "two", 3: "three", 4: "four", 5: "five", 6: "six", 7: "seven", 8: "eight", 9: "nine", 10: "ten", 11: "eleven", 12: "twelve", 13: "thirteen", 14: "fourteen", 15: "fifteen", 16: "sixteen", 17: "seventeen", 18: "eighteen", 19: "nineteen", 20: "twenty", 30: "thirty", 40: "forty", 50: "fifty", 60: "sixty", 70: "seventy", 80: "eighty", 90: "ninety", 100: "hundred", 1000: "onethausend"}

number = 1000 + 1
letter_counts = []
count_later_two_digit = []
count_later_three_digit = []

# check if n is in dict and if not than fill count_later...
for i in range(1,number): 
    n = number - i
    if n in numbers_dict:
        written_n = numbers_dict[n]
        letter_counts.append(written_n)
    else:
        if n < 100:
            count_later_two_digit.append(str(n))
        else:
            count_later_three_digit.append(str(n))

# take care of the two digit numbers
for digit in count_later_two_digit:
    first_number = int(digit[0] + "0")
    written_first_number = numbers_dict[first_number]
    written_second_number = numbers_dict[int(digit[1])]
    written_number = written_first_number + written_second_number 
    numbers_dict[int(digit)] = written_number

# take care of the three digit numbers
for digit in count_later_three_digit:
    first_number = int(digit[0])
    written_first_number = numbers_dict[first_number] + numbers_dict[100]
    numbers_dict[int(digit[0]+"00")] = written_first_number

    if digit[2] != "0":
        second_number = int(digit[1] + digit[2])

        if second_number != 0:
            written_second_number = numbers_dict[second_number]
            written_number = written_first_number + "and" + written_second_number
            numbers_dict[int(digit)] = written_number

    else:
        second_number = int(digit[1] + "0")
        if second_number != 0:
            written_second_number = numbers_dict[second_number]
            written_number = written_first_number + "and" + written_second_number
            numbers_dict[int(digit)] = written_number

# count letters
letters = 0
for i in range(1,number):
    print(numbers_dict[i])
    letters += len(numbers_dict[i])

print(letters)