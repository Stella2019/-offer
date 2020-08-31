'''
题目：
大家都知道斐波那契数列，现在要求输入一个整数n，请你输出斐波那契数列的第n项。
n<=39
'''

'''
伪代码:1. 用sum存储第N项，one储存第N-1项，two储存第N-2项 2. 循环，并交替储存第N，N- 1,N-2项的数，sum=one+two得到结果。 注意的点:递归时间复杂度是[O(N的平方)]，上面的伪代码是O(N)。
第三位是前两位之和，一直迭代的
25ms
5632k
'''

# -*- coding:utf-8 -*-
class Solution:
    def Fibonacci(self, n):
        # write code here
        res = [0,1]
        while len(res) <= n:
            res.append(res[-1]+res[-2])
        return res[n]