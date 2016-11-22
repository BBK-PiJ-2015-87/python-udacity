import re

str1 = '2016_01_01_HelloWorld'
str2 =  '2016_01_01_'

print(str1.replace(str2,''))

line = '2016_01_01_001_2016-11-11_HelloRegex_80000076'


line2 = re.sub(r"\d{4}_\d{2}_\d{2}_\d{3}_", "", line)

print(line2)