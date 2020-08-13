"""
1395. Count Number of Teams

There are n soldiers standing in a line. Each soldier is assigned a unique rating value.

You have to form a team of 3 soldiers amongst them under the following rules:

Choose 3 soldiers with index (i, j, k) with rating (rating[i], rating[j], rating[k]).
A team is valid if:  (rating[i] < rating[j] < rating[k]) or (rating[i] > rating[j] > rating[k]) where (0 <= i < j < k < n).
Return the number of teams you can form given the conditions. (soldiers can be part of multiple teams).

 

Example 1:

Input: rating = [2,5,3,4,1]
Output: 3
Explanation: We can form three teams given the conditions. (2,3,4), (5,4,1), (5,3,1). 
Example 2:

Input: rating = [2,1,3]
Output: 0
Explanation: We can't form any team given the conditions.
Example 3:

Input: rating = [1,2,3,4]
Output: 4
 

Constraints:

n == rating.length
1 <= n <= 200
1 <= rating[i] <= 10^5
"""


class Solution:
	# Brute force
    def numTeams(self, rating: List[int]) -> int:
        count = 0
        for i in range(0,len(rating)-2):
            for j in range(i+1,len(rating)-1):
                for k in range(j+1,len(rating)):
                    count +=1 if (( rating[i] < rating[j] and rating[j] < rating[k] ) or (rating[i] > rating[j] and rating[j] > rating[k])) else 0
        return count
	
	
	#Mathematical solution
	def numTeams_Math(self, rating: List[int]) -> int:
	    ans = 0
        n = len(rating)
        for j in range(n):
            leftsmaller ,leftlarger, rightsmaller, rightlarger = 0,0,0,0
			
            for i in range (0,j):
                if rating[i] < rating[j]:
                    leftsmaller +=1
                if rating[i] > rating[j]:
                    leftlarger +=1
            
            for k in range (j+1,n):
                if rating[k] < rating[j]:
                    rightsmaller +=1
                if rating[k] > rating[j]:
                    rightlarger +=1
            
			#just sum
            ans += leftsmaller*rightlarger + leftlarger*rightsmaller
        return ans