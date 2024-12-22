# Problem 9: Special Pythagorean Triplet
# a**2 + b**2 = c**2

def pythagorean_triplet_product(number):
    for a in range(1,number):
        for b in range(1,number):
            for c in range(1,number):
                if a+b+c == number:
                    if a**2 + b**2 == c**2:
                        result = a*b*c
                        return result

print(pythagorean_triplet_product(1000))