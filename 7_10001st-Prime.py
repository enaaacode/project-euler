# Problem 7: 10.001st Prime
x = 150000
all_numbers = list(range(2,x+1)) # create a list with numbers from 2 to x

prime_numbers = [2] # this is the list with the prime numbers -> it will grow as we progress
p_counter = 0

n_lst = [] 

div_lst = [] # this list goes into n_lst

for i in range(len(all_numbers)):
    if all_numbers[i] % prime_numbers[p_counter] != 0:
        div_lst.append(all_numbers[i])

p_counter += 1
prime_numbers.append(div_lst[0])
n_lst.append(div_lst)

for j in range(int(x/2)):

    div_lst = []
    for i in range(len(n_lst[-1])):
        my_list = n_lst[-1]
        if my_list[i] % prime_numbers[p_counter] != 0:
            div_lst.append(my_list[i])

    p_counter += 1
    n_lst.append(div_lst)
    if len(div_lst) > 0:
        prime_numbers.append(div_lst[0])
    else:
        break


'''for i in n_lst:
    print(i)'''

#print(prime_numbers)
#print(len(prime_numbers))
print(prime_numbers[10001-1])