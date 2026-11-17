# https://leetcode.com/problems/contains-duplicate/
from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        for x in nums:
            if x in seen:
                return True
            seen.add(x)
        return False


if __name__ == "__main__":
    s = Solution()
    assert s.containsDuplicate([1, 2, 3, 1]) is True
    assert s.containsDuplicate([1, 2, 3, 4]) is False
    assert s.containsDuplicate([1, 1, 1, 3, 3, 4, 3, 2, 4, 2]) is True
    assert s.containsDuplicate([7]) is False
    assert s.containsDuplicate([0, 0]) is True
    assert s.containsDuplicate([-1, 1, -1]) is True
    assert s.containsDuplicate([-5, 5, 0]) is False
    print("ok")
