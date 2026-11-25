# https://leetcode.com/problems/valid-palindrome/


class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1
        while l < r:
            # skip anything that isn't a letter or digit
            if not s[l].isalnum():
                l += 1
            elif not s[r].isalnum():
                r -= 1
            elif s[l].lower() != s[r].lower():
                return False
            else:
                l += 1
                r -= 1
        return True


if __name__ == "__main__":
    s = Solution()
    assert s.isPalindrome("A man, a plan, a canal: Panama") is True
    assert s.isPalindrome("race a car") is False
    assert s.isPalindrome(" ") is True
    assert s.isPalindrome("") is True
    assert s.isPalindrome("0P") is False
    assert s.isPalindrome("a.") is True
    assert s.isPalindrome("No 'x' in Nixon") is True
    print("ok")
