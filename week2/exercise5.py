# Find the 2nd smallest number in the list


def second_smallest_number(lst):
    min_2 = []
    while lst:
        min = lst[0]
        for i in lst:
            if i < min:
                min = i
        min_2.append(min)
        lst.remove(min)
    if len(min_2) >= 2:
        return min_2[1]
    else:
        return "List does not have a second smallest number."

lst = [6, 9, 7, 8, 4, 90]

print("SECOND SMALLEST NUMBER IS", second_smallest_number(lst))


