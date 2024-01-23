#Objective: To calculate average of all the  integers.
# Time Complexity: O(n)
# Space Complexity: O(1) for constant amount of space

def average(arr,n):
    sum = 0
    for i in range(n):
        sum += arr[i]
    return sum/n
#Driver
arr = [1,2,3,4,5,5]
n = len(arr)
print(n)
print(average(arr,n))

    