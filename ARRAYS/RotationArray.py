#Rotation Array in Swapping Approach
# Time Complexity: O(n), as we need to iterate through all the elements.[n is the length of array]
# Auxiliary Space: O(1), as we are using constant space.


def ArrayRotation(arr,n):
    last_element = arr[n-1]

    for i in range(n-1,0,-1):
        arr[i] = arr[i-1]
    
    arr[0] = last_element


#Driver
Arr  = [1,2,3,4,5]
n = len(Arr)
print(Arr)
ArrayRotation(Arr,n)
print(Arr)

#for printing with for loop
for i in range(0,n):
    print(Arr[i],end =" ")