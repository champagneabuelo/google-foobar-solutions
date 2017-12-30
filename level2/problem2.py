# current approach:
# implement subtraction with differnt base numbers
# utilize that function to continuously iterate new keys
# once a value is reached that already exists in the list, stop and return the length of list
import sys
sys.setrecursionlimit(5000)

def convert_base(number, base):
    while number > 0:
        number, digit = divmod(number, base)
        yield digit

def sort_string(string):
    # params: string of id
    # return: tuple with sorted strings ascending and descending
    to_array = map(int, string)
    to_array.sort()
    ascending = ''.join(map(str, to_array))
    to_array.sort(reverse=True)
    descending = ''.join(map(str, to_array))
    return (ascending, descending)

def substraction(values, base):
    # params: tuples with numbers to be substracted, and base of number
    # return: difference in base that was originally given 
    ascending = int(values[0], base)
    descending = int(values[1], base)
    difference = descending - ascending
    converted = list(convert_base(difference, base))
    converted.reverse()
    return ''.join(map(str, converted))

def answer(n, b):
    ids = []
    # params: takes initial string of k length, and base of number
    # return: number of values before cycle
    no_cycle = True
    while no_cycle:
        length = len(n)
        string_tuple = sort_string(n)
        new_value = substraction(string_tuple, b)
        new_id = new_value.zfill(length)
        for index, item in enumerate(ids):
            if item == new_id:
                return index+1
                break
        ids = [new_id] + ids
        n = new_id

if __name__== "__main__":
    answer("210022", 3) 
    answer("1211", 10)
