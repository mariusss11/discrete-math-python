
a = input()
b = input()
# a, b = input().split()

# print(a)
# print(b)

a_boolean = bool(a.lower() == "true" or a == "1")
b_boolean = bool(b.lower() == "true" or b == "1")

# print(a_boolean)
# print(b_boolean)

result = (a_boolean and b_boolean) or (not a_boolean and not b_boolean)

print("XNOR:", "1" if result else "0")