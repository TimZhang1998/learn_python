# -*- coding: utf-8 -*-

def normalize(name):
	a = name[0:1]
	a = a.upper()
	b = name[1:]
	b = b.lower()
	return a + b
	
# 测试:
L1 = ['adam', 'LISA', 'barT']
L2 = list(map(normalize, L1))
print(L2)	
		