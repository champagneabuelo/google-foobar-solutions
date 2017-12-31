def create_list(version_list):
    # params: list of version number strings
    # return list of tuples, tuples will have strings or None, and number for length 
    tuple_list = []
    for string in version_list:
        string_array = map(int, string.split('.'))
        length = len(string_array)
        if length == 1:
            version_tuple = (string_array[0], None, None, 1)
            tuple_list.append(version_tuple)
        elif length == 2:
            version_tuple = (string_array[0], string_array[1], None, 2)
            tuple_list.append(version_tuple)
        elif length == 3:
            version_tuple = (string_array[0], string_array[1], string_array[2], 3)
            tuple_list.append(version_tuple)
    return tuple_list

def insertion_sort(l):
    # params: list of version tuples
    # return: list of sorted version tuples
    length = len(l)
    for i in reversed(range(3)):
        for j in range(1, length):
            current = l[j]
            position = j 
            while (position > 0) and (l[position-1][i] > current[i]):
                l[position] = l[position-1]
                position -= 1
            l[position] = current
    return l

def tuple_to_string(l):
    # params: list of version tuples 
    # return: list of version number strings
    string_list = []
    for tup in l:
        length = tup[3]
        if length == 1:
            version_string = str(tup[0])
            string_list.append(version_string)
        elif length == 2:
            version_string = str(tup[0])+"."+str(tup[1])
            string_list.append(version_string)
        elif length == 3:
            version_string = str(tup[0])+"."+str(tup[1])+"."+str(tup[2])
            string_list.append(version_string)
    return string_list

def answer(l):
    tuple_list = create_list(l)
    sorted_list = insertion_sort(tuple_list)
    final_list = tuple_to_string(sorted_list)
    return final_list

example_list1 = ["1.1.2", "1.0", "1.3.3", "1.0.12", "1.0.2"]
example_list2 = ["1.11", "2.0.0", "1.2", "2", "0.1", "1.2.1", "1.1.1", "2.0"]
example_list3 = ["1.0.0", "1.0", "1"]

answer(example_list1)
answer(example_list2)
answer(example_list3)
