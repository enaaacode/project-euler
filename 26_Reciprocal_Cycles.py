# Problem 26: Reciprocal Cycles

numbers_lst = list(range(1,1000))
reciprocal_values_lst = []
longest_reciprocal_value = 0

for number in numbers_lst:
    reciprocal_value = 1 / number
    reciprocal_values_lst.append(reciprocal_value)
    if len(str(reciprocal_value)) > len(str(longest_reciprocal_value)):
        longest_reciprocal_value = reciprocal_value

# this is also is the max length of a recurring cycle
max_length = len(str(longest_reciprocal_value))

for line in reciprocal_values_lst:
    print(line)

# check recurring cycle
