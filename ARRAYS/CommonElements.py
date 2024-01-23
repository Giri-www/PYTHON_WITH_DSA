'''**Finding common elements between two List**'''

# The space complexity :  O(k), where k is the number of common elements between arr1 and arr
#  The time complexity :
''' below  this function is O(m * n), where m is the length of arr1 and n
    The in operation in a list has a time complexity of O(n), and this operation is performed
     for each element in arr '''

def commonElemnts(arr,arr1):
    common_Elements = []
    for num in arr:
        if num in arr1 and num not in common_Elements:
            common_Elements.append(num)
    return common_Elements
#Driver 
arr1 = [1, 2, 3, 4, 5]
arr = [3, 4, 5, 6, 7]
result = commonElemnts(arr,arr1)
print("Common elements Normal Approach:", result)


#Set approach Approach 2
"""" 
     Time Complexity : O(m+n)   
     Space complexity : O(k)
     use optimized for fast lookups.
"""

def findCommon(arr2,arr3):
    set1=Set(arr2)
    set2=Set(arr3)
    commonElements =set1.intersection(set2)
    return commonElements
#Driver 
arr2 = [1, 2, 3, 4, 5]
arr3 = [3, 4, 5, 6, 7]
result = commonElemnts(arr2,arr3)
print("Common elements using Set approach:", result)
