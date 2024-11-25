"""
Given an array of integers numbers that is sorted in non-decreasing order.

Return the indices (1-indexed) of two numbers, [index1, index2],
such that they add up to a given target number target and index1 < index2.
Note that index1 and index2 cannot be equal,
therefore you may not use the same element twice.

There will always be exactly one valid solution.

Your solution must use
O(1)
O(1) additional space.

Example 1:

Input: numbers = [1,2,3,4], target = 3

Output: [1,2]
"""
from  typing import List
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        start = 0
        end = len(numbers) - 1
        while start < end:
            if numbers[start] + numbers[end] == target:
                return [start+1, end+1]
            elif numbers[start] + numbers[end] > target:
                end -=1
            elif numbers[start] + numbers[end] < target:
                start+=1

        return [-1, -1]

sol = Solution()
arr1 = [1,2,3,4]
target = 3
print(sol.twoSum(arr1, target))

sol = Solution()
arr1 = [2,3,4]
target = 6
print(sol.twoSum(arr1, target))

sol = Solution()
arr1 = [1,2,3,4]
target = 5
print(sol.twoSum(arr1, target))
