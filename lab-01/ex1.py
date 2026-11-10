# 1 2 3 -> [[],[1],[2],[3],[1,2],[1,3],[2,3],[1,2,3]]

def generate_subsets(s, index, curr, res):
    # if it is the end case (we've for to the end list) we stop and add the element itself (the list itself)
    if index == len(s):
        res.append(curr[:])
        return

    curr.append(s[index])                         # include
    generate_subsets(s, index + 1, curr, res)
    curr.pop()                                    # backtrack: fără argument
    generate_subsets(s, index + 1, curr, res)     # exclude

def power_set(s):
    res = []
    generate_subsets(s, 0, [], res)
    return res

user_input = input().split()
res = power_set(user_input)

print("The results in res list: ")
print(res)
# or

print("[" + ",".join("[" + ",".join(x) + "]" for x in res) + "]")
