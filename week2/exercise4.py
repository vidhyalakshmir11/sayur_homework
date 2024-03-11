# Find the smallest number in the list

def smallestNumber(list):
    min = list[0]
    for i in list :
        if min > i:
            min = i
    return min
list = [1,2,3,4,5,6]

print(smallestNumber(list) )
