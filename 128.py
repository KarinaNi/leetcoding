class Solution:
    def longestConsecutive(self, nums):
        if not nums:
            return 0

        dp = {}
        max_length = 0
        for num in nums:
            if num not in dp:
                prev = dp.get(num-1, 0)
                next = dep.get(num+1, 0)
                curr_len = prev+next+1
                dp[num] = curr_len
                dp[num-prev] = curr_len
                dp[num+next] = curr_len
                max_length = max(max_length, curr_len)
        return max_length

sol = Solution()
nums1 = []
print(sol.longestConsecutive(nums1))  # Expected output: 0 Actual output: 0

nums2 = [100, 4, 200, 1, 3, 2]
print(sol.longestConsecutive(nums2))  # Expected output: 4 Actual output: 2

nums3 = [9, 1, 4, 7, 3, 6, 2, 8]
print(sol.longestConsecutive(nums3))  # Expected output: 4 Actual output: 3

nums4 = [1, 2, 3, 4]
print(sol.longestConsecutive(nums4))  # Expected output: 4 Actual output: 4

#works only for increasing sequence
