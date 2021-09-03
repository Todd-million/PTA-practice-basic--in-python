'''
def is_prime(x):
    if (x == 2) or (x == 3):
        return True
    if (x % 6 != 1) and (x % 6 != 5):
        return False
    for i in range(5, int(x ** 0.5) + 1, 6):
        if (x % i == 0) or (x % (i + 2) == 0):
            return False
    return True
'''


# determine whether a number x is prime or not

def is_prime(x):
    if x == 2:
        return True
    elif x % 2 == 0:
        return False
    for i in range(3, int(x ** 0.5) + 1, 2):
        if x % i == 0:
            return False
    return True


upper_bound = int(input())
count = 0
prime_list = []
for b in range(2, upper_bound + 1):
    if is_prime(b):
        prime_list.append(b)
prime_list.sort(reverse=False)
for a in prime_list:
    if (a + 2) in prime_list:
        count += 1

print(count, end="")

#debug needed: time overflow