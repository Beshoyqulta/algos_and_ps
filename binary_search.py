# binary search algorithm
# binary search is simply searching with log2 n for n is the worst possible count for finding the desired target 
# the algorithm is simply you begin with the middle element of the sorted list 
# if the number is higher than the middle we delete all the lower 50% 
# if the number is lower than the middle we delete all the higher 50% 
# the best case is that the desired target is the middle element 
# we keep reapting the process till we find the desired target 
def binary_search(list , item):
    low = 0
    high = len(list)-1
    while low <= high :
        mid = low + high
        guess = list[mid]
        if guess == item : 
            return mid
        if guess < item:
            low = mid + 1
        else:
            high = mid -1
    return None
list = [1,2,3,4,5,6,7]
print(binary_search(list , 5))
             



    