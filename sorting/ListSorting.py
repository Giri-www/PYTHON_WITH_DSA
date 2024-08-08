##### List Sorting With Numbers ####
numbers = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
#using sort function
numbers.sort()

# Output After sorted
print(numbers)  # [1, 1, 2, 3, 3, 4, 5, 5, 5, 6, 9]


#### Sorted With Key Function To Sort Complex DS Like Tuple,List And Dict ####
students = [("Giri", "A", 15), ("Das", "C", 12), ("Paul", "B", 10)]

 
sorted_by_age = sorted(students, key=lambda student: student[2])
print(sorted_by_age)  

# Output: [('Paul', 'B', 10), ('Das', 'B', 12), ('Giri', 'A', 15)]
