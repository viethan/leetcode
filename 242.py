class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dic = {}
        
        for char in s:
            if char not in dic:
                dic[char] = 0
            dic[char] += 1
            
        for char in t:
            if char not in dic:
                return False
            else:
                dic[char] -= 1
        
        for val in list(dic.values()):
            if val != 0:
                return False
            
        return True
