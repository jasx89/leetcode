"""
1365. How Many Numbers Are Smaller Than the Current Number


Given the array nums, for each nums[i] find out how many numbers in the array are smaller than it. That is, for each nums[i] you have to count the number of valid j's such that j != i and nums[j] < nums[i].

Return the answer in an array.

Example 1:

Input: nums = [8,1,2,2,3]
Output: [4,0,1,1,3]
Explanation: 
For nums[0]=8 there exist four smaller numbers than it (1, 2, 2 and 3). 
For nums[1]=1 does not exist any smaller number than it.
For nums[2]=2 there exist one smaller number than it (1). 
For nums[3]=2 there exist one smaller number than it (1). 
For nums[4]=3 there exist three smaller numbers than it (1, 2 and 2).
Example 2:

Input: nums = [6,5,4,8]
Output: [2,1,0,3]
Example 3:

Input: nums = [7,7,7,7]
Output: [0,0,0,0]
 

Constraints:

2 <= nums.length <= 500
0 <= nums[i] <= 100


"""

#brute force

class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        res = [0]*len(nums)
        
        i = 0
        while i < len(nums):
            value = nums[i]
            count = 0;
            for j in range(len(nums)):
                if (i!=j and nums[j]<nums[i]):
                    count+=1
            res[i]=count;
            i+=1
        return res
		
		
# quicksort trick 1
class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        res = [0]*101
        
        for num in nums:
            res[num] += 1
        acc = 0
        
        for i in range(len(res)):
            prev = res[i]
            res[i]=acc
            acc += prev
        
        result = [0]*len(nums)
        for i in range(len(nums)):
            result[i]=res[nums[i]]
        
        return result

# quicksort trick 2
class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        res = [0]*101  #we know we have up to 100 buckets.
        
        for num in nums:
            res[num] += 1  #count the values in nums
        acc = 0  
        
        for i in range(len(res)):  
            prev = res[i]   
            res[i]=acc
            acc += prev
        
        return [res[num] for num in nums]


