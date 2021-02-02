iclass Solution:
    def isPalindrome(self, s: str) -> bool:
        if s is None:
            return True
        
        i, j = 0, len(s) - 1
        while i < j:
            if s[i].isalnum() and s[j].isalnum():
                if s[i].lower() != s[j].lower():
                    return False
                i, j = i + 1, j - 1
            else:
                if not s[i].isalnum():
                    i += 1
                if not s[j].isalnum():
                    j -= 1
        return True
