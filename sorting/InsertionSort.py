### INSERTION SORT ###
"""
    Insertion Sort is a simple and intuitive sorting algorithm 
    that builds the final sorted array one item at a time. 
    It is much like sorting playing cards in your hands: 
    you pick up one card at a time and insert it into its correct position in 
    sthe already sorted section of your hand. """


def insertion_sort(arr):
    for i in range(1,len(arr)):
        key = arr[i]
        j = i-1

        while j>=0 and key < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key

    return arr

# Driver
arr = [64, 34, 25, 12, 22, 11, 90]
sorted_arr = insertion_sort(arr)
print(sorted_arr)  
# Output: [11, 12, 22, 25, 34, 64, 90