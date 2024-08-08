#Sorting a List custom Sort method
numbers = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
reverse_list = []

#! Custom Sort Function !# 
def custom_sort(numbers):
    length1 = len(numbers)
    for i in range(length1):
        for j in range(0 ,length1-i-1):
            if numbers[j] > numbers[j+1] :
                numbers[j], numbers[j+1] = numbers[j+1], numbers[j]

custom_sort(numbers)


#! Custom Reverse Function #!
def custom_reverse(numbers):
    length1 = len(numbers)
    # Iterate from the last index 
    for i in range(length1 - 1, -1, -1):
        reverse_list.append(numbers[i])
    
    return reverse_list

print(custom_reverse(numbers))