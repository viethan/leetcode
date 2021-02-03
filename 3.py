class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start = end = 0
        seen_positions = {}
        longest = 0
        
        for i in range(len(s)):
            if s[i] not in seen_positions or seen_positions[s[i]] < start:
                end = i
                longest = max(longest, end - start + 1)
            else:
                start = seen_positions[s[i]] + 1
            
            seen_positions[s[i]] = i
                    
        return longest
