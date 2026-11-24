# https://leetcode.com/problems/longest-consecutive-sequence/
from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        best = 0
        for x in num_set:
            # only start counting from the beginning of a run
            if x - 1 in num_set:
                continue
            length = 1
            while x + length in num_set:
                length += 1
            best = max(best, length)
        return best


if __name__ == "__main__":
    s = Solution()
    assert s.longestConsecutive([100, 4, 200, 1, 3, 2]) == 4
    assert s.longestConsecutive([0, 3, 7, 2, 5, 8, 4, 6, 0, 1]) == 9
    assert s.longestConsecutive([1, 0, 1, 2]) == 3
    assert s.longestConsecutive([]) == 0
    assert s.longestConsecutive([7]) == 1
    assert s.longestConsecutive([-1, -2, -3, 5, 6]) == 3
    assert s.longestConsecutive([10, 30, 20]) == 1
    print("ok")
