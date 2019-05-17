'''
Given a non-empty array of digits representing a non-negative integer, plus one to the integer.

The digits are stored such that the most significant digit is at the head of the list, and each element in the array contain a single digit.

You may assume the integer does not contain any leading zero, except the number 0 itself.
'''
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        num = int(''.join(str(i) for i in digits)) +1
        return [int(x) for x in str(num)]