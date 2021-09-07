user_input = input().split(" ")
a = int(user_input[0])
b = int(user_input[1])

q = a // b
r = a % b
print(q, " ", r, sep="")

# A,B = map(int,input().split())
# review the map function