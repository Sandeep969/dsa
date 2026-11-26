# https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/
from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers) - 1
        while l < r:
            s = numbers[l] + numbers[r]
            if s == target:
                return [l + 1, r + 1]  # 1-indexed
            if s < target:
                l += 1
            else:
                r -= 1
        return []


if __name__ == "__main__":
    s = Solution()
    assert s.twoSum([2, 7, 11, 15], 9) == [1, 2]
    assert s.twoSum([2, 3, 4], 6) == [1, 3]
    assert s.twoSum([-1, 0], -1) == [1, 2]
    assert s.twoSum([1, 1], 2) == [1, 2]
    assert s.twoSum([-5, -3, 0, 2, 8], 3) == [1, 5]
    assert s.twoSum([1, 2, 3, 4, 4, 9], 8) == [4, 5]
    assert s.twoSum([0, 0, 3, 4], 0) == [1, 2]
    print("ok")
