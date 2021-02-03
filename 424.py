class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        if len(s) is 0:
            return 0
        
        start = end = 0
        max_count, max_char = 0, s[0]
        longest = 0
        count = {}
        
        for i in range(len(s)):
            if s[i] not in count:
                count[s[i]] = 0
            count[s[i]] += 1
            
            if count[s[i]] > max_count:
                max_count, max_char = count[s[i]], s[i]
            
            if (i - start + 1) - max_count <= k:
                end = i
                longest = max(longest, end - start + 1)
            else:
                count[s[start]] -= 1
                if s[start] is max_char:
                    max_count -= 1
                start += 1
            
        return longest
