def is_prime(x):
    if (x == 2) or (x == 3):
        return True
    if (x % 6 != 1) and (x % 6 != 5):
        return False
    for i in range(5, int(x ** 0.5) + 1, 6):
        if (x % i == 0) or (x % (i + 2) == 0):
            return False
    return True


def find_prime(lower_bound, upper_bound):
    prime_list = []
    for a in range(lower_bound, upper_bound):
        if is_prime(a):
            prime_list.append(a)
    return prime_list


def decimal_format(input_list, pack_num):
    import math
    line_num = math.floor((len(input_list) / pack_num))
    resiudal = len(input_list) % pack_num
    format_list = []

    if line_num == 0:
        print(input_list)
    else:
        for a in range(line_num):
            temp_list = []
            for b in range(pack_num):
                temp_list.append(input_list[a * pack_num + b])
            format_list.append(temp_list)
        if resiudal != 0:

        for a in range(line_num):
            print(format_list[a])


m_n_list = input().split(" ")
m = int(m_n_list[0])
n = int(m_n_list[1])

found_list = find_prime(m, n)
decimal_format(found_list, 10)
