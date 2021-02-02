class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        
        for char in s:
            if char in ['(', '[', '{']:
                stack.append(char)
            elif char in [')', ']', '}']:
                if stack:
                    open_bracket = stack.pop()
                    if not ((open_bracket is '(' and char is ')') or \
                    (open_bracket is '[' and char is ']') or \
                    (open_bracket is '{' and char is '}')):
                        return False
                else:
                    return False
                
        if stack:
            return False
        return True
