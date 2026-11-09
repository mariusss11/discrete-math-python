# (!x + y) * z + (!z * y * k)
#  x + y

# 0 1
# 0 0
# 1 1
# 1 0


def is_variable(char):
    if (char == "(" or char == ")" or char == "*" or char == "+" or char == "!" or char == " "):
        return False
    return True


input_string = input()

variable_set = set()

# get all the variables from the string
for char_index in range(0, len(input_string)):
    # print("Variable: " + expr[i])
    # print("isVariable = " + str(is_variable(expr[i])))
    if (is_variable(input_string[char_index])):
        variable_set.add(input_string[char_index])


# sort the set
variable_set = sorted(variable_set)

variable_count = len(variable_set)
total_rows = 2 ** variable_count
total_columns = variable_count + 1
result_column = variable_count


# create the table
# https://www.geeksforgeeks.org/python/python-using-2d-arrays-lists-the-right-way/
rows, cols = (total_rows, total_columns)
arr = [[0] * total_columns for _ in range(total_rows)]

# // returns integer
# / returns float

# add the 0 and 1 in the table, move firstly through the columns then through the row
# loop for columns
for char_index in range(variable_count):
    column_counter = total_rows // (2 ** (char_index + 1))

    # loop for rows
    for row_index in range(total_rows):
        arr[row_index][char_index] = (row_index // column_counter) % 2


# prepare the expresion for evaluation
expr = input_string.replace("!", " not ").replace("*", " and ").replace("+", " or ")


# https://www.geeksforgeeks.org/python/how-to-create-a-dictionary-in-python/
def get_dict_for_row(arr):
    keys = variable_set
    values = arr
    return {k: v for k, v in zip(keys, values)}


for row_index in range(total_rows):
    # without the final column
    dict = get_dict_for_row(arr[row_index][:variable_count])

    arr[row_index][result_column] = bool(eval(expr, {}, dict))



print("The final matrix: ")
for row in arr:
    print(row)





