#Reverse an array without in Builed function

#The space complexity is O(1), indicating constant space usage. 
# The function doesn't use additional space that scales with the input size. 

# The time complexity of the custom reverse function is O(n), where n is the length of the input ARRAY. 
# increases, the number of iterations grows linearly.

def My_Reverse(array):

    start ,end = 0,len(array) - 1   

    while(start<end):
        array[start] ,array[end] = array[end],array[start]
        start += 1
        end -= 1
    return array

array = [1,2,3,4,5]
print(array)
ReverseArray=My_Reverse(array)
print(ReverseArray)


