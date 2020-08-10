# linear search function; time complexity: O(n)
# return the index at which the val lies

def linear(arr, val):
    i = 0  # track of indices
    while i < len(arr):
        for item in arr:  # go through each index in arr
            if item == val:
                return i
            i += 1
        return -1  # if val not found...


print(linear([10, 15, 20, 25], 15))  # 1
print(linear([200], 100))  # -1




