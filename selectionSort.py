def populateRandomList(n):
    sample = []

    import random

    for count in range(0,n):
        sample.append(random.randint(1,n))

    print sample
    return sample








toSort = populateRandomList(10)


def selectionSort(unsorted):

    for i in range(0, len(unsorted)):
        min = i
        max = i
        for j in range(i+1, len(unsorted)):
            if unsorted[j] < unsorted[min]:
                min = j
            if unsorted[j] > unsorted[max]:
                max = j

        # temp  = unsorted[i]
        # unsorted[i] = unsorted[min]
        # unsorted[min] = temp

        temp  = unsorted[i]
        unsorted[i] = unsorted[max]
        unsorted[max] = temp
            


    print unsorted

selectionSort(toSort)
    