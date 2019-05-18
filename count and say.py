'''
The count-and-say sequence is the sequence of integers with the first five terms as following:

1.     1
2.     11
3.     21
4.     1211
5.     111221
1 is read off as "one 1" or 11.
11 is read off as "two 1s" or 21.
21 is read off as "one 2, then one 1" or 1211.

Given an integer n where 1 ≤ n ≤ 30, generate the nth term of the count-and-say sequence.

Note: Each term of the sequence of integers will be represented as a string.
'''
class Solution:
    def countAndSay(self, n: int) -> str:
        def sub_count(n):
            if n ==1:
                return '1'
            else:
                s = sub_count(n-1)
            i = 0
            j = 1
            rst = ''
            while i < len(s):
                while j < len(s) and s[i] == s[j]:
                    j +=1
                rst += str(j-i) + s[i]
                i = j
                j += 1
            return rst
        return sub_count(n)