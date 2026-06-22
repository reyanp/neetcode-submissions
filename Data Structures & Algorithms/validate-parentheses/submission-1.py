class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        CTO = { ")" : "(", 
                        "]" : "[", 
                        "}" : "{" }
        
        for c in s:
            if c in CTO:
                if stack and stack[-1] == CTO[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        
        return True if not stack else False

'''
- Python we can use a [] as a stack
- pop() and append()


6/22
valid = []
        for c in s:
            if c == "(" or c == "[" or c == '{':
                valid.append(c)
            if c == ")" or c == "]" or c == '}':
                valid.append(c)
        print(valid)
        while len(valid) != 0:
            if valid [0] == '[' and valid[-1] == ']':
                valid.pop(0)
                valid.pop(-1)
            elif valid [0] == '{' and valid[-1] == '}': 
                valid.pop(0)
                valid.pop(-1)
            elif valid [0] == '(' and valid[-1] == ')':
                valid.pop(0)
                valid.pop(-1)
            else:
                return False
        return True
'''