# Problem 18: Maximum Path Sum I

data = '''75
95 64
17 47 82
18 35 87 10
20 04 82 47 65
19 01 23 75 03 34
88 02 77 73 07 63 67
99 65 04 28 06 16 70 92
41 41 26 56 83 40 80 70 33
41 48 72 33 47 32 37 16 94 29
53 71 44 65 25 43 91 52 97 51 14
70 11 33 28 77 73 17 78 39 68 17 57
91 71 52 38 17 14 91 43 58 50 27 29 48
63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23'''

data = data.splitlines()

numbers_lst = []
for i in range(len(data)):
    numbers_line = data[i].split(" ")
    numbers_lst.append(numbers_line)

int_numbers_lst = []
for i in range(len(numbers_lst)):
    int_numbers_line = []
    for j in range(len(numbers_lst[i])):
        int_number = int(numbers_lst[i][j])
        int_numbers_line.append(int_number)
    int_numbers_lst.append(int_numbers_line)    

for line in int_numbers_lst:
    print(line)

max_path_sum = int_numbers_lst[0][0]
starting_point = 0

for i in range(1, len(int_numbers_lst)):
    for j in range(len(int_numbers_lst[i])-1):
        if j == starting_point:
            left_adjacent = int_numbers_lst[i][j]
            right_adjacent = int_numbers_lst[i][j+1]
            if left_adjacent > right_adjacent:
                highest_adjacent_number = left_adjacent
                starting_point = j
                break
            if left_adjacent < right_adjacent:
                highest_adjacent_number = right_adjacent
                starting_point = j+1
                break
    '''print()
    input()
    print(int_numbers_lst[i])
    print(highest_adjacent_number)'''

    max_path_sum += highest_adjacent_number

print(max_path_sum) # oh no! This is just one path. But I need every possible path T.T

