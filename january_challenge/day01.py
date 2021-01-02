class Solution:
    def canFormArray(self, arr: List[int], pieces: List[List[int]]) -> bool:
        dic, arr_length = {}, len(arr)
        
        for iPiece in pieces:
            dic[iPiece[0]] = iPiece

        i = 0
        while i < arr_length:
            if arr[i] in dic:
                copy_i = i
                for j in range(len(dic[arr[copy_i]])):
                    if i < arr_length and arr[i] == dic[arr[copy_i]][j]:
                        i += 1
                    else:
                        return False
            else:
                return False
            
        return True
