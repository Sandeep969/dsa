# https://leetcode.com/problems/valid-anagram/


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        count = {}
        for a, b in zip(s, t):
            count[a] = count.get(a, 0) + 1
            count[b] = count.get(b, 0) - 1
        return all(v == 0 for v in count.values())


if __name__ == "__main__":
    s = Solution()
    assert s.isAnagram("anagram", "nagaram") is True
    assert s.isAnagram("rat", "car") is False
    assert s.isAnagram("a", "a") is True
    assert s.isAnagram("ab", "a") is False
    assert s.isAnagram("aacc", "ccac") is False
    assert s.isAnagram("listen", "silent") is True
    assert s.isAnagram("", "") is True
    print("ok")
