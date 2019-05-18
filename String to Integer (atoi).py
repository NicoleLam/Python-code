'''
Implement atoi which converts a string to an integer.

The function first discards as many whitespace characters as necessary until the first non-whitespace character is found. Then, starting from this character, takes an optional initial plus or minus sign followed by as many numerical digits as possible, and interprets them as a numerical value.

The string can contain additional characters after those that form the integral number, which are ignored and have no effect on the behavior of this function.

If the first sequence of non-whitespace characters in str is not a valid integral number, or if no such sequence exists because either str is empty or it contains only whitespace characters, no conversion is performed.

If no valid conversion could be performed, a zero value is returned.

Note:

Only the space character ' ' is considered as whitespace character.
Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−2^31,  2^31 − 1]. If the numerical value is out of the range of representable values, INT_MAX (2^31 − 1) or INT_MIN (−2^31) is returned.
'''
class Solution:
    def myAtoi(self, str: str) -> int:
        import re
        s = str.strip()
        sign = '+'
        try:            
            if s[0] in '+-':
                sign = s[0]
                s = s[1:]
            for i in range(len(s)):
                if s[i].isdigit():
                    continue
                elif i>0:
                    s = s[:i]
                    # print(s)
                else:
                    return 0        
            if sign == '-':
                s = -1*int(s)
                return max(-2**31,s)
            else:
                print(s)
                return min(int(s), 2**31-1)
        except:
            return 0
        