user_input = input()
user_input_1 = list(user_input)
user_input_1.reverse()
input_length = len(user_input_1)

if input_length == 3:
    print(int(user_input_1[2]) * 'B', end='')
if input_length > 1:
    print(int(user_input_1[1]) * "S",end="")
for a in range(1, int(user_input_1[0]) + 1):
    print(a,end='')
