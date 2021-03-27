import re
str1 = "sadw96aeafae4awdw2wd100awd"
a=re.findall('\d+', str1)
print(a)
print(len(a))