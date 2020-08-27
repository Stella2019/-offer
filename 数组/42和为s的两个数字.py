'''
题目：输入一个递增排序的数组和一个数字S，在数组中查找两个数，是的他们的和正好是S，如果有多对数字的和等于S，
输出两个数的乘积最小的
'''

'''
伪代码:1. 数列满足递增，设两个头尾两个指针i和j，2. 若ai + aj == sum，就是答案(相差越远 乘积越小)
3. 若ai + aj > sum，aj肯定不是答案之一(前面已得出 i 前面的数已是不可能)，j -= 1 4. 
若ai + aj < sum，ai肯定不是答案之一(前面已得出 j 后面的数已是不可能)，i += 1 5. 循环1， 2，3，4步


思路：设定两个指针，一个指向数组的起点，一个指向数组的终点，然后对两个数字求和，如果和大于目标值，则把后一个指针前移，
如果和小于目标值，则把前一个指针后移。两个指针交汇的时候如果还没找到，就终止操作。

37ms
5628k
'''

# -*- coding:utf-8 -*-
class Solution:
    def FindNumbersWithSum(self, array, tsum):
        # write code here
        if array == None or len(array) <= 0 or array[-1] + array[-2] < tsum:
            return []
        start = 0
        end = len(array) - 1
        while start < end:
            if array[start] + array[end] < tsum:
                start += 1
            elif array[start] + array[end] > tsum:
                end -= 1
            else:
                return [array[start], array[end]]
        return []


