#!/usr/bin/python
# -*- coding: UTF-8 -*-

'''
题目描述
现在你面对一个n*m的矩阵，矩阵中的每一个元素都是一个整数，
现在你需要计算从矩阵的左上角走到右下角所走过的所有元素的最大和。
注意：只能向右或者向下走，不能走出边界。

解答要求
时间限制：1000ms，内存限制：64MB

输入
输入第一行包含两个用空格分开的整数n(1 <= n <= 100)和m(1 <= m <= 100)，
表示n行m列的矩阵，矩阵中每个点的数值范围为0~100。

输出
输出从矩阵的左上角所走过的所有元素相加的最大和

样例
n=3，m=4
1 2 0 7
1 8 2 3
9 0 1 5
输出
21
'''

import random


# 贪婪算法
def largest_sum_of_path_in_rectangle0(arr, n, m):
	n, m = 0, 0
	result = arr[n][m]
	while len(arr) > n+1 or len(arr[0]) > m+1:
		right = 0
		if len(arr[0]) > m+1:
			right = arr[n][m+1]
		down = 0
		if len(arr) > n+1:
			down = arr[n+1][m]
		if right > down:
			m += 1
			result += right
		else:
			n += 1
			result += down
	return result


# 递归穷举 剪枝
dict = {}
def largest_sum_of_path_in_rectangle1(arr, n, m):
	if len(arr) == n+1 and len(arr[0]) == m+1:
		print("last  n:" + str(n) + ", m:" + str(m) + ", r:" + str(arr[n][m]))
		return arr[n][m]

	right = 0
	if len(arr[0]) > m+1:
		key = str(n) + '-' + str(m+1)
		if key not in dict:
			dict[key] = largest_sum_of_path_in_rectangle1(arr, n, m+1)
		right = arr[n][m] + dict[key]

	down = 0
	if len(arr) > n+1:
		key = str(n+1) + '-' + str(m)
		if key not in dict:
			dict[key] = largest_sum_of_path_in_rectangle1(arr, n+1, m)
		down = arr[n][m] + dict[key]
	
	if right > down:
		print("right n:" + str(n) + ", m:" + str(m) + ", r:" + str(right))
		return right
	else:
		print("down  n:" + str(n) + ", m:" + str(m) + ", r:" + str(down))
		return down

# arr = [[1,2,0,7], [1,8,2,3], [9,0,1,5]]
arr = []
for i in range(1, 100):
	ta = []
	for j in range(1, 100):
		ta.append(random.randint(0, 100))
	arr.append(ta)
print("arr:" + str(arr))

result = largest_sum_of_path_in_rectangle1(arr, 0, 0)
print("result:" + str(result))

