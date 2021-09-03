#string reverse marked by space
input_string = input()
input_list = input_string.split(" ")
list_length = len(input_list)
input_list.reverse()

print(" ".join(input_list))