a = [1,2,3,4,5]

def multiply(nums, m):
    newnums = []
    for element in nums:
        element *= m
        newnums.append(element)
    return newnums


b = multiply(a,5)
print b

