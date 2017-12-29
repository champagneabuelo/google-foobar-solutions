def answer(area):
    val_list = []
    while area > 0:
        largest_size = int(area ** 0.5)
        largest_square = largest_size ** 2
        area -= largest_square
        val_list.append(largest_square)
    return val_list

if __name__== "__main__":
    test1 = answer(15324)
    print test1
    print 15324, sum(test1)
    test2 = answer(339)
    print test2
    print 339, sum(test2)
    test3 = answer(1)
    print test3
    print 1, sum(test3)
    test4 = answer(12)
    print test4
    print 12, sum(test4)
    test5 = answer(100000)
    print test5
    print 100000, sum(test5)
