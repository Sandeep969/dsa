# https://leetcode.com/problems/3sum/
from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        n = len(nums)
        for i in range(n - 2):
            if nums[i] > 0:
                break  # sorted, so nothing after can sum to 0
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            lo, hi = i + 1, n - 1
            while lo < hi:
                total = nums[i] + nums[lo] + nums[hi]
                if total < 0:
                    lo += 1
                elif total > 0:
                    hi -= 1
                else:
                    res.append([nums[i], nums[lo], nums[hi]])
                    lo += 1
                    hi -= 1
                    # skip duplicate second values
                    while lo < hi and nums[lo] == nums[lo - 1]:
                        lo += 1
        return res


if __name__ == "__main__":
    s = Solution()
    assert s.threeSum([-1, 0, 1, 2, -1, -4]) == [[-1, -1, 2], [-1, 0, 1]]
    assert s.threeSum([0, 1, 1]) == []
    assert s.threeSum([0, 0, 0]) == [[0, 0, 0]]
    assert s.threeSum([0, 0, 0, 0]) == [[0, 0, 0]]
    assert s.threeSum([1, 2]) == []
    assert s.threeSum([-2, 0, 1, 1, 2]) == [[-2, 0, 2], [-2, 1, 1]]
    assert s.threeSum([-4, -2, -2, -2, 0, 1, 2, 2, 2, 3, 3, 4, 4, 6, 6]) == [
        [-4, -2, 6], [-4, 0, 4], [-4, 1, 3], [-4, 2, 2],
        [-2, -2, 4], [-2, 0, 2],
    ]
    print("ok")
