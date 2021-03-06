'''
题目：请实现一个函数用来找出字符流中第一个只出现一次的字符。例如，当从字符流中只读出前两个字符"go"时，
第一个只出现一次的字符是"g"。当从该字符流中读出前六个字符“google"时，第一个只出现一次的字符是"l"。
'''

'''
思路：引入两个辅助存储空间。一个Dict存储当前出现的字符以及字符出现的次数，一个List存储当前出现字符。
然后每次比较List的第一个字符在Dict中对应的次数，如果为1则输出这个字符，如果不为1则弹出这个字符比较下一个字符。

伪代码:1. 创建字典，key为读取的字符串中的每一个字符，val为每个字符出现的个数的计数值 2. 输出函数:遍历字符串s中的字符，如果某个字符对应的计数为1，则返回该字符。
插入函数， 从字符流中读入字符到字符串s中，如果读入的字符在字符串中已存在，在字典中对应的字符计数 加一，如果读入的字符在字符串中不存在，则字典中对应的字符计数为一(即新增了一个新的字 符)
26ms
5760k
'''

# -*- coding:utf-8 -*-
class Solution:
    # 返回对应char
    def __init__(self):
        # 存储当前字符
        self.alist = []
        # 存储当前字符及其出现次数，出现大于1次，就设成2次
        self.adict = {}

    def FirstAppearingOnce(self):
        # write code here
        while len(self.alist) > 0 and self.adict[self.alist[0]] == 2:
            self.alist.pop(0)
        if len(self.alist) == 0:
            return '#'
        else:
            return self.alist[0]

    def Insert(self, char):
        # write code here
        if char not in self.adict.keys():
            self.adict[char] = 1
            self.alist.append(char)
        else:
            self.adict[char] = 2
