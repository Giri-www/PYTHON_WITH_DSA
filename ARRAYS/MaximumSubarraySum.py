""" *** Given an array of integers, find the contiguous subarray with the largest sum
        MaximumSubarraySum Problem / Kadane's Algorithm
                                                        *** """                                                      
 # Input: [-2, 1, -3, 4, -1, 2, 1, -5, 4]
# Output: 6 (The subarray [4, -1, 2, 1] has the largest sum which is 6) """    

def maxSumSubarraySum(nums):
    maxSum = float('-inf')  #  Initialize max_sum to negative infinity
    currentSum = 0
    for num in nums:
        currentSum = max(num,currentSum + num)
        maxSum = max(maxSum,currentSum)
    return maxSum

#Driver
nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
result = maxSumSubarraySum(nums)
print("Maximum Subarray Sum:", result)

