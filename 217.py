class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        seto = set()
        
        for val in nums:
            if val in seto:
                return True
            seto.add(val)
        return False
