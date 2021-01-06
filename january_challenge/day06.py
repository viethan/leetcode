class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        missing, expected = 0, 1
        
        i = 0
        while missing != k:
            if i < len(arr) and (arr[i] != expected):
                while expected != arr[i] and missing != k:
                    missing += 1
                    expected += 1
            else:
                if i < len(arr) and (arr[i] == expected):
                    i += 1
                else:
                    missing += 1
                expected += 1
                
        return expected - 1
