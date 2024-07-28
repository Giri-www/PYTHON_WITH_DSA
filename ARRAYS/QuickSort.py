class Quicksort:
    def __init__(self):
        #pass funcion 
        pass
    #Quick Sort Code Below
    def quick_sort(self,array,low,high):
        if low < high:
            partition = self.partition_func(array,low,high)
            self.quick_sort(array,low,partition-1)  # Recursively call quick_sort
            self.quick_sort(array,partition+1,high) # Recursively call quick_sort
            # print("quick")
    #! Partition Code Below 
    def partition_func(self,array,low,high):
        pivot = array[high]
        i = low -1
        for j in range(low,high):
            if array[j] <= pivot:
                i += 1 
                temp = array[i]
                array[i] = array[j]
                array[j] = temp
         #After Close the Loop       
        temp = array[i + 1]
        array[i + 1] = array[high]
        array[high] = temp
        return i + 1

#!Driver Code Below #!   
quick_object = Quicksort()
array = [24,10, 7, 18, 29, 1, 5,27]
print(len(array)-1)
quick_object.quick_sort(array,0,len(array)-1)
print("Sorted Array Is >>>  ",array)
    

#### ANALYSIS ALGO ####
  #!Time!
    # partition_func takes O(n) time as it involves a single pass through the array segment.
    # In the best and average cases, the array is divided into two nearly equal halves, leading to O(n log n) time complexity.
    #In Wrost scenario it's o(n^2)

  #!Space!
    # Here algorithm uses constant extra space for variables, but the recursion stack space depends on the depth of the recursive calls.
    # In the best and average cases, the depth of the recursion tree is log n, resulting in O(log n) auxiliary space.
    # In the worst case, the recursion depth can go up to n, resulting in O(n) auxiliary space.