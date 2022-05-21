from distutils.filelist import findall
import re
x = '192.168.0.12:13667 and 192.168.122.11:556'
i = re.compile(r'\d\d?\d?\.\d\d?\d?\.\d\d?\d?\.\d\d?\d?\:\d\d?\d?\d?\d?')
a = re.compile(r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})\:(\d{1,5})')
o = a.findall(x) 
e = a.search(x)
print(o)
print(e.group(0))
print(e.group(1))
print('Your Socket Number is ' + e.group(2))
