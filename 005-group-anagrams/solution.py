# https://leetcode.com/problems/group-anagrams/
from collections import defaultdict
from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)
        for s in strs:
            # anagrams have the same sorted letters, so use that as the key
            groups["".join(sorted(s))].append(s)
        return list(groups.values())


if __name__ == "__main__":
    s = Solution()
    assert sorted(map(sorted, s.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))) == sorted(map(sorted, [["bat"], ["nat", "tan"], ["ate", "eat", "tea"]]))
    assert s.groupAnagrams([""]) == [[""]]
    assert s.groupAnagrams(["a"]) == [["a"]]
    assert s.groupAnagrams(["abc", "bca", "xyz"]) == [["abc", "bca"], ["xyz"]]
    assert s.groupAnagrams(["ab", "ba", "ab"]) == [["ab", "ba", "ab"]]
    assert s.groupAnagrams(["a", "b", "a"]) == [["a", "a"], ["b"]]
    assert s.groupAnagrams(["aab", "aba", "baa", "abb"]) == [["aab", "aba", "baa"], ["abb"]]
    print("ok")
