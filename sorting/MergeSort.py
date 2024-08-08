#### == Merge Sort == ####

def merge_sort(arr):
    
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2

    left_half = arr[:mid]
    righ_half = arr[mid:]

    left_sort = merge_sort(left_half)
    right_sort = merge_sort(righ_half)

    return merge(left_sort,right_sort)

def merge(left,right):
    array = []
    left_index,right_index = 0,0

    while left_index < len(left) and right_index < len(right):
        if left[left_index] < right[right_index]:
            array.append(left[left_index])
            left_index += 1
        else:
            array.append(right[right_index])
            right_index += 1    
    #!  Rather the elements added        
    array.extend(left[left_index:])
    array.extend(right[right_index:])
    
    return array

# Example usage
numbers = [64, 34, 25, 12, 22, 11, 90]
sorted_numbers = merge_sort(numbers)
print("Sorted array:", sorted_numbers)