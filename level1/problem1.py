def answer(x,y):
    # convert lists to sets
    # subtract the sets
    # convert the difference to list
    # return the remaining int
    set1 = set(x)
    print set1
    set2 = set(y)
    print set2
    if len(set1) > len(set2):
        remainder = list(set1 - set2)
        return remainder[0] 
    else:
        remainder = list(set2 - set1)
        return remainder[0]

if __name__== "__main__":
    list1 = [13, 5, 6, 2, 5]
    list2 = [5, 2, 5, 13]
    list3 = [14, 27, 1, 4, 2, 50, 3, 1]
    list4 = [2, 4, -4, 3, 1, 1, 14, 27, 50]

    print answer(list1, list2)
    print answer(list3, list4)

