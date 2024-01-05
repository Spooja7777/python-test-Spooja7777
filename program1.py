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

exp = input("Enter the expression : ")
# creating an instance of the Solution class
solution = Solution()
# call the isValid method with a string argument that will be taken as input from user
result = solution.isValid(exp)
print(result)
        


  

