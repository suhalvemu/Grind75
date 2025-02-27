class Solution:
    def isValid(self, s: str) -> bool:

        if len(s)<=1:
            return False

        stack = []

        for c in s:
            if c in ['(', '{' , '[']:
                stack.append(c)
            else:
                if len(stack)>0:
                    if c == ')' and stack.pop()!='(':
                        return False
                    elif c == '}' and stack.pop() != '{':
                        return False
                    elif c == ']' and stack.pop() != '[':
                        return False
                else:
                    return False
        if len(stack)>0:
            return False
        return True       