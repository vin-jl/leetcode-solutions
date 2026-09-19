class Solution:
    def isPalindrome(self, s: str) -> bool:
        st = "".join(filter(str.isalnum, s)).lower()
        start = 0
        end = len(st)-1
        while start <= end:
            if st[start] != st[end]:
                return False
            else:
                start += 1
                end -= 1
        return True
