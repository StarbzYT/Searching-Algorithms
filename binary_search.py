# binary search function (for arrays)
# Guidelines (pseudocode)
# this function accepts a sorted array and a value
# create a left pointer at the start of the array, and a right pointer at the end of the array
# while the left pointer comes before the right pointer:
    # create a pointer in the middle
    # if you find the value you want, return the index
    # if the value is too small, move the left pointer up
    # if the value is too large, move the right pointer down
# if you never find the value, return -1


def binary(arr, val):  # O(log n)
    start = 0  # first index
    end = len(arr) - 1  # at the last index
    middle = (start + end) // 2  # use // to floor result
    while start <= end and arr[middle] != val:  # start must be less than end and val should not be found (result infinite loop if value not found)
        if val < arr[middle]:  # if the value is less than the middle point
            # set end to be one less than the middle. (we know that the middle is not the value!)
            end = middle - 1
        else:
            #  else, val is greater than middle
            start  = middle + 1  # now move start pointer to one after middle!
        middle = (start + end) // 2  # update middle with the new start and end points after each cycle
    # check if middle is the val, otherwise return -1
    if arr[middle] == val:
        return middle
    return -1  # val index not found...

print(binary([2, 5, 7, 9, 11, 13, 15, 17], 15))  # 6
# [2, 5, 7, 9, 11, 13, 15, 17]
#  S        M               E      
# 15 is greater than middle so...
# [2, 5, 7, 9, 11, 13, 15, 17]
#               S   M        E              
print(binary([2, 5, 7, 9, 11, 13, 15, 17], 20))  # -1

