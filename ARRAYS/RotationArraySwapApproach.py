# # Swapping Approach Rotation Array
# Time Complexity: O(n), as we need to iterate through all the elements.(n is length of array) 
# Auxiliary Space: O(1), as we are using constant space.

def Rotation(arr,n):
    i = 0
    j = n-1
    while i != j:
        arr[i] ,arr[j] = arr[j],arr[i]
        i = i+1
    pass
#Driver 
arr = [1,2,3,4,5]
n = len(arr)
print(f"""Before Array Rotation is {arr}""")
Rotation(arr,n)  #call Rotation
print(f"""After Rotation the Array is {arr}""")