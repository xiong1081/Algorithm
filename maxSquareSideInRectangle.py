#!/usr/bin/python
# -*- coding: UTF-8 -*-

# 分治(divide and conquer，D&C)
# 递归

# 假设你是农场主，有一小块土地。
# 你要将这块地均匀地分成方块，且分出的方块要尽可能大。

def maxSquareSideInRectangle(length, width):
	remainder = length % width
	if remainder == 0:
		return width
	else:
		return maxSquareSideInRectangle(width, remainder)

print maxSquareSideInRectangle(1680, 640)
