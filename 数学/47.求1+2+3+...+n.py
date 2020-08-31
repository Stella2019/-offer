'''
题目：求1+2+3+...+n，要求不能使用乘除法、for、while、if、else、switch、case等关键字及条件判断语句（A?B:C）。
'''

'''
伪代码:1. 需利用逻辑与的短路特性实现递归终止 
2. 当n== 0 时，(n> 0 )&& ((sum+=Sum_Solution(n- 1 ))> 0 )只执行前面的判断，为 false ，然后直接返回 0 ;
3. 当n> 0 时，执行sum+=Sum_Solution(n- 1 )，实现递归计算Sum_Solution(n)。

思路一：利用了python的特性吧，好想法。

29ms
5632k
'''

# -*- coding:utf-8 -*-
class Solution:
    def Sum_Solution(self, n):
        # write code here
        return sum(list(range(1, n + 1)))

'''
思路二：利用两个函数，一个函数充当递归函数的角色，另一个函数处理终止递归的情况。如果对n连续进行两次反运算，
那么非零的n转换为True，0转换为False。利用这一特性终止递归。注意考虑测试用例为0的情况。

34ms
6140k
'''

# -*- coding:utf-8 -*-
class Solution:
    def Sum_Solution(self, n):
        # write code here
        return self.sum(n)

    def sum0(self, n):
        return 0

    def sum(self, n):
        fun = {False: self.sum0, True: self.sum}
        return n + fun[not not n](n - 1)