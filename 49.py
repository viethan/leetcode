class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = {}
        
        for string in strs:
            sorted_string = ''.join(sorted(string))
            if sorted_string not in dic:
                dic[sorted_string] = []
            dic[sorted_string].append(string)
            
        return list(dic.values())
