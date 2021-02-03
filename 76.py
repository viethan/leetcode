class Solution:
    def minWindow(self, s: str, t: str) -> str:
        t_letters, t_copy = {}, {}
        s_letters = {}
        
        for char in t:
            if char not in t_letters:
                t_letters[char] = t_copy[char] = 0
                s_letters[char] = 0
            t_letters[char] += 1
            t_copy[char] += 1
            
        
        # check if t is there in the first place !!!!!!!
        for char in s:
            if char in t_copy:
                t_copy[char] -= 1
                
        for val in list(t_copy.values()):
            if val > 0:
                return ""
            
        min_start, min_end = 0, len(s) - 1
        start = end = 0
        
        recorded, i = 0, 0
        while True:
            # if does not fulfill the condition
            if recorded != len(t) and i < len(s):
                # advance until it does
                end = i
                if s[i] in t_letters:
                    if s_letters[s[i]] < t_letters[s[i]]:
                        recorded += 1
                    s_letters[s[i]] += 1
                i += 1
                    
            else:
                while recorded == len(t):
                    #record to see if it's smaller than the current minimum window
                    if (end - start + 1) < (min_end - min_start + 1):
                        min_start, min_end = start, end
                        
                    #squezee as much as you can
                    if s[start] in t_letters:
                        if s_letters[s[start]] == t_letters[s[start]]:
                            recorded -= 1
                        
                        s_letters[s[start]] -= 1
                    
                    start += 1
                    
                if i == len(s):
                    break
                   
        return s[min_start:min_end + 1]
