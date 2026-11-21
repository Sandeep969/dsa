# https://leetcode.com/problems/top-k-frequent-elements/
from collections import Counter
from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # bucket sort by frequency: index i holds values that appear i times
        count = Counter(nums)
        buckets = [[] for _ in range(len(nums) + 1)]
        for x, c in count.items():
            buckets[c].append(x)
        res = []
        for c in range(len(buckets) - 1, 0, -1):
            res.extend(buckets[c])
            if len(res) >= k:
                return res[:k]
        return res


if __name__ == "__main__":
    s = Solution()
    assert sorted(s.topKFrequent([1, 1, 1, 2, 2, 3], 2)) == [1, 2]
    assert s.topKFrequent([1], 1) == [1]
    assert sorted(s.topKFrequent([4, 4, 4, 5, 5, 6], 2)) == [4, 5]
    assert sorted(s.topKFrequent([-1, -1, 0, 0, 0, 2], 2)) == [-1, 0]
    assert s.topKFrequent([7, 7, 7, 7], 1) == [7]
    assert sorted(s.topKFrequent([1, 2, 3, 4], 4)) == [1, 2, 3, 4]
    assert sorted(s.topKFrequent([0, 0, 1, 1, 2, 2, 2], 3)) == [0, 1, 2]
    print("ok")
