# Link - https://leetcode.com/problems/two-sum/
# Question ID - 1
# Question Name - Two Sum
class Solution(object):
    def twoSum(self, nums, target):
        checkList = {}
        for i in range(len(nums)):
            if (target - nums[i]) in checkList:
                return [checkList[target-nums[i]], i] 
            checkList[nums[i]] = i
        return []