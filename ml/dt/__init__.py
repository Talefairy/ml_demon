# -*- coding: utf-8 -*-
# @Time    : 2018/3/12 
# @Author  : fc.w
# @File    : __init__.py.py


"""
	3. 计算房源图片相似度:
		1). 相同小区下，自有房源图片与其它平台的房源图片做笛卡尔积。
		2). 先将图片做灰度处理，通过SIFT算法获取两张图片的相同的局部特征；统计每套自有房源笛卡尔积后和其他平台房源相同的总特征数，判定特征数最大的外部房源为


"""