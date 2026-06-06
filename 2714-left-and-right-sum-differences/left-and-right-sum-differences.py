class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        n = len(nums)
        if n == 1:
            return [0]
        l, r = 0, sum(nums[1:])
        ret = [r]
        for i in range(1, n):
            l += nums[i - 1]
            r -= nums[i]
            ret.append(abs(l - r))
        return ret