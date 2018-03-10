# -*- coding: utf-8 -*-
from functools import reduce

def str2float(s):
	def _10int(a, b):
		return 10 * a + b 
	def _str2int(s):
		s = [x for x in s if x != '.']
		s = list(map(int, s))
		s = reduce(_10int, s)
		return s 
	def _adddot(s, a):
		i = 0
		while s[-i] != '.':
			i = i + 1
		while (i - 1) != 0:
			a = a / 10
			i = i - 1
		return a 
	a = _str2int(s)
	s = _adddot(s, a)
	return s 
	
# 测试：
print('str2float(\'123.456\') =', str2float('123.456'))
if abs(str2float('123.456') - 123.456) < 0.00001:
    print('测试成功!')
else:
    print('测试失败!')
	