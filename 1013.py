def is_prime(x):
    if (x == 2) or (x == 3):
        return True
    if (x % 6 != 1) and (x % 6 != 5):
        return False
    for i in range(5, int(x ** 0.5) + 1, 6):
        if (x % i == 0) or (x % (i + 2) == 0):
            return False
    return True


# checking if the input is a prime number
# return True or False

def find_prime(lower_bound, upper_bound):
    prime_list = []
    for a in range(lower_bound, upper_bound):
        if is_prime(a):
            prime_list.append(a)
    return prime_list


# find all prime numbers in the region with lower_bound as lower bound and upper_bound as upper bound
# return the list made up by the appropriate prime numbers

def decimal_format(input_list, pack_num, index_1, index_2):
    import math
    input_list = input_list[index_1:index_2 + 1]
    line_num = math.floor((len(input_list) / pack_num))
    residual = len(input_list) % pack_num
    format_list = []

    if line_num == 0:
        print(" ".join(str(i) for i in input_list))
    else:
        for a in range(line_num):
            format_list.append(input_list[a * 10:(a + 1) * 10])
        if residual != 0:
            format_list.append(input_list[line_num * 10::])
            line_num += 1
        for a in range(line_num):
            if a != line_num - 1:
                print(" ".join(str(i) for i in format_list[a]))
            else:
                print(" ".join(str(i) for i in format_list[a]), end="")


m_n_list = input().split(" ")
m = int(m_n_list[0])
n = int(m_n_list[1])

found_list = find_prime(1, 10001)
decimal_format(found_list, 10, m, n)

#debug needed