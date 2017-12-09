#good swap function
#def swap(a,b):
#   return([b,a])


def bubble_sort(lst):
    is_sorted = False
    while is_sorted == False:
        nswaps = 0
        for i in range(len(lst)-1):
            a = lst[i]
            b = lst[i+1]
            if a>b:
                lst[i] = b
                lst[i+1] = a
                nswaps = nswaps+1
        if nswaps == 0:
            is_sorted = True
    return lst

print(bubble_sort([1,2,3,4,5]))

print(bubble_sort([5,4,3,2,1]))

print(bubble_sort([4,5,3,1,2]))
    
