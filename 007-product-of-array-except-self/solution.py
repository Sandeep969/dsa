# https://leetcode.com/problems/product-of-array-except-self/
from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [1] * n
        # res[i] = product of everything left of i
        for i in range(1, n):
            res[i] = res[i - 1] * nums[i - 1]
        # then multiply in the product of everything right of i
        right = 1
        for i in range(n - 1, -1, -1):
            res[i] *= right
            right *= nums[i]
        return res


if __name__ == "__main__":
    s = Solution()
    assert s.productExceptSelf([1, 2, 3, 4]) == [24, 12, 8, 6]
    assert s.productExceptSelf([-1, 1, 0, -3, 3]) == [0, 0, 9, 0, 0]
    assert s.productExceptSelf([2, 3]) == [3, 2]
    assert s.productExceptSelf([0, 0]) == [0, 0]
    assert s.productExceptSelf([0, 4, 5]) == [20, 0, 0]
    assert s.productExceptSelf([-2, -3, 4]) == [-12, -8, 6]
    assert s.productExceptSelf([1, 1, 1, 1]) == [1, 1, 1, 1]
    print("ok")
