elements = []
trace = 0
i_repeat = 0
j_repeat = 0
increment = 0
userInput = int(input()) # "How many test cases"
case = 1
for j in range(userInput):
    row = int(input()) #"How many rows"
    for i in range(row):
        x = input().split() #"Enter the values: "
        integer_map = map(int, x)
        integer_list = list(integer_map)
        elements.append(integer_list) # Creating a 2d array
        trace = trace + integer_list[increment] # calculating the diagonal values.
        increment = increment + 1
        if integer_list[0] in integer_list[1:]: # checking whether the row of the matrix has repeated values.
            i_repeat = i_repeat + 1
    for z in range(row):
        my_list = [k[z] for k in elements]  # Taking the first values of the list to create the column.
        # print(my_list)
        if elements[-1][z] in my_list[:-1]: # checking whether the column of the matrix has repeated values.
            j_repeat = j_repeat + 1
    print(f"Case #{case}:", trace, i_repeat, j_repeat)
    case = case + 1
    # Setting all of these values to 0 since there more than one case.
    trace = 0
    increment = 0
    i_repeat = 0
    j_repeat = 0
    elements.clear()
