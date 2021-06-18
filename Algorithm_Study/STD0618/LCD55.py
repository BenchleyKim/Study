from typing import List

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        idx = 0 
        mx_range = nums[idx] + idx
        result = False
        if mx_range >= len(nums) - 1 :
            return True
        while nums[idx] > 0 :
            if mx_range >= len(nums) - 1 :
                return True
            for i in range(idx+1, min(mx_range+1,len(nums))) :
                if nums[i] + i >= mx_range :
                    idx = i
                    mx_range = nums[idx] + idx
                    break
        return result





solution = Solution()
nums = [2,3,1,1,4]
print(solution.canJump(nums))
nums = [3,2,1,0,4]
print(solution.canJump(nums))
nums = [2,0]

print(solution.canJump(nums))
nums = [0]

print(solution.canJump(nums))
