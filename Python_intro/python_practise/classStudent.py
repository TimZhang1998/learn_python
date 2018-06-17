# -*- coding: utf-8 -*-
	
class Student(object):
	count = 0
	def __init__(self, name = 'Bob', score = 0, gender = 'male'):
		self.__name = name
		self.__score = score
		self.__gender = gender
		Student.count += 1

	def get_gender(self):
		return self.__gender
	
	def set_gender(self, gender):
		if gender == 'male' or gender == 'female':
			self.__gender = gender
		else:
			raise ValueError('bad gender')
	
	def get_grade(self):
		if self.score >= 90:
			return 'A'
		elif self.score >= 60:
			return 'B'
		else:
			return 'C'

# 测试：			
bart = Student('Bart', 59, 'male')
if bart.get_gender() != 'male':
	print('测试失败!')
else:
	bart.set_gender('female')
	if bart.get_gender() != 'female':
		print('测试失败!')
	else:
		print('测试成功!')

if Student.count != 1:
    print('测试失败!')
else:
    bart = Student('Bart')
    if Student.count != 2:
        print('测试失败!')
    else:
        lisa = Student('Bart')
        if Student.count != 3:
            print('测试失败!')
        else:
            print('Students:', Student.count)
            print('测试通过!')
