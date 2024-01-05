class Solution():
   
    def romanToInt(self, s):
        roman = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000,'IV':4,'IX':9,'XL':40,'XC':90,'CD':400,'CM':900}
        i = 0
        result = 0
 
        while i < len(s):
            if i+1 < len(s) and s[i:i+2] in roman:
                result += roman[s[i:i+2]]
                i += 2
            else:
                result += roman[s[i]]
                i += 1
        return result

inputv = input("Enter the roman : ")
solution = Solution()

result = solution.romanToInt(inputv)
print(result)
