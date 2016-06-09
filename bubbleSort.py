
def populateRandomList(n):
    sample = []

    import random

    for count in range(0,n):
        sample.append(random.randint(1,n))

    return sample







toSort = populateRandomList(10)


print toSort






def bubbleSort(unsorted):

    # unsorted = []
    # i = 0
    # print unsorted
    for passnum in range(len(unsorted)-1,0,-1):
        for i in range(0,passnum):
            if unsorted[i] > unsorted[i+1]:
                temp  = unsorted[i+1]
                unsorted[i+1] = unsorted[i]
                unsorted[i] = temp
            


    print unsorted

bubbleSort(toSort)
