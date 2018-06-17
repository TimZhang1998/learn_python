# -*- coding: utf-8 -*-
import re

p = re.compile(r'[a-zA-Z0-9\.]+@[a-zA-Z0-9]+.com')

def is_valid_email(addr):
	m = p.match(addr)
	return m
	
# 测试:
assert is_valid_email('someone@gmail.com')
assert is_valid_email('bill.gates@microsoft.com')
assert not is_valid_email('bob#example.com')
assert not is_valid_email('mr-bob@example.com')
print('ok')