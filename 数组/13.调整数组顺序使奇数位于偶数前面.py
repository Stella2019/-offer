'''
题目：输入一个整数数组，实现一个函数来调整该数组中数字的顺序，使得所有的奇数位于数组的前半部分，
所有的偶数位于位于数组的后半部分，并保证奇数和奇数，偶数和偶数之间的相对位置不变。
'''

'''
伪代码:用插入排序的思想，时间复杂度最差O(n的平方):1. i++ 往前走碰到偶数停下来， j = i+1 ，2. 若 a[j] 为偶数， j++ 前进，直到碰到奇数。 
3. 然后奇数插到a[i]位置， j 经过的 j-i 个 偶数依次后移 
4. j==len-1 时还没碰到奇数，证明 i 和 j 之间都为偶数了，完成整个移动

方法一： 两个数组解
25ms
5504k
'''

# -*- coding:utf-8 -*-
class Solution:
    def reOrderArray(self, array):
        # write code here

        res1 = []
        res2 = []
        for i in array:
            if i % 2 == 0:
                res1.append(i)
            else:
                res2.append(i)
        return res2 + res1

'''
方法二：类似冒泡的思想，相互交换
'''
