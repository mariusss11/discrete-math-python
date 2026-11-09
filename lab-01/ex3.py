import math

num = input()

# https://pynative.com/python-count-digits-of-number/
count = len(str(abs(int(num)))) # Convert number to string and count its length
print("Number of digits:", count)

# digits = []

# for i in range(0,count):
#     digits.append(int(num[i]))

num_digits = list(num)

print(num_digits)

new_num = []


for i in range(0, count - 1):
    if (int(num[i]) > int(num[i+1])):
        temp = num[i]
        num[i] = num[i+1]
        num[i+1] = temp

print(num_digits)

# 110 -> 101
# 52 -> 25
# 654 -> 456
# 483 -> 348
# 213 -> 123