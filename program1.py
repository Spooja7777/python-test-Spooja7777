class Solution(object):
    def isValid(self,s):
        stack = []
        for c in s:
            if c in ( '(', '{' , '{'):
                stack.append(c)
            else:
                if stack and ((stack[-1] == '(' and c == ')') or 
                        (stack[-1] == '' and c == '}') or 
                        (stack[-1] == '[' and c == ']')) :
                    stack.pop()
                else:
                    return False
        return not stack

exp = input()
solution = Solution()
result = solution.isValid(exp)
print(result)
        


  

