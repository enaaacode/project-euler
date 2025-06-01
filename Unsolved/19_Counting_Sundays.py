# Problem 19: Counting Sundays

months = ["Jan", "Feb", "Mar", "Apr", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dez"]
regular_year = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
leap_year = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31] # A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400
years_lst = list(range(1900,2001))
week = 7 #days
days = ["Mon", "Tue", "Wed", "Thu", "Fry", "Sat", "Sun"]

years_dict = {}
for i in range(1900,2001):
    if i % 4 == 0:
        years_dict[i] = sum(leap_year)
    else:
        years_dict[i] = sum(regular_year)

year = 1900
date = 7, "Jan"
day_counter = 7
day = "Sun"
sundays = []

while year < 2001:
    for i in range(1900,2001):
        days = years_dict[i]
        while days > 0:
            pass

