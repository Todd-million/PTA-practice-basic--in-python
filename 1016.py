user_input = input().split(" ")
d_a_num = 0
d_b_num = 0
for a in user_input[0]:
    if a == user_input[1]:
        d_a_num += 1
for a in user_input[2]:
    if a == user_input[3]:
        d_b_num += 1

d_a = int(user_input[1])
d_b = int(user_input[3])

result_1 = 0
result_2 = 0
for a in range(d_a_num):
    result_1 += pow(10, a) * d_a
for a in range(d_b_num):
    result_2 += pow(10, a) * d_b

print(result_1 + result_2, end="")