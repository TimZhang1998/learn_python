# -*- coding: utf-8 -*-
import re

p = re.compile(r'(<(\w+?[\w\s]+)>\s+)?(\w+|\w+.\w+|\d+)@(\w+|\d+).\w+')
def name_of_email(addr):
    g = p.match(addr).groups()
    return g[1] if g[1] else g[2]
	
assert name_of_email('<Tom Paris> tom@voyager.org') == 'Tom Paris'
assert name_of_email('tom@voyager.org') == 'tom'
print('ok')

