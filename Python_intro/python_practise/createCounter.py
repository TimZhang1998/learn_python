# -*- coding: utf-8 -*-

def createCounter():
	j = 0
	def counter():
		nonlocal j
		j += 1
		return j 
	return counter

# 测试:
counterA = createCounter()
print(counterA(), counterA(), counterA(), counterA(), counterA()) # 1 2 3 4 5
counterB = createCounter()
if [counterB(), counterB(), counterB(), counterB()] == [1, 2, 3, 4]:
    print('测试通过!')
else:
    print('测试失败!')

	
    