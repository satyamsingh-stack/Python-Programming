# # Empty Dictionary
# dict={}
# print(dict)
# print(type(dict))
#
#
# # Adding Element
# d={}
# d[1]='Satyam Singh'
# d[2]='Kiran Singh'
# d[3]='Akhilesh Singh'
# d[4]='Ramanand Singh'
# d[5]='Kamla Singh'
# d[6]='Sarthak Singh'
# d[7]='Aayan Singh'
# print(d)
#
# # Accesing a Value
# d={1:'Monday',2:'Tuesday',3:'Wednesday',4:'Thursday',5:'Friday',6:'Saturady',7:'Sunday'}
# print(d[5])
#
#
# # Updating A Value
# d={1:'Jan',2:'Feb',3:'Mar',4:'Apr',5:'May'}
# print(d)
# d[2]='Jun'
# d[3]='July'
# d[4]='August'
# print(d)
#
#
# # Deleting Value
# d={1:'Jan',2:'Feb',3:'Mar',4:'Apr',5:'May'}
# del d[4]
# print(d)
#
#
# # Generic Function
# d={1:'Jan',2:'Feb',3:'Mar',4:'Apr'}
# d1=d.copy()
# print(len(d))
# print(max(d))
# print(min(d))
# print(sum(d))
# print(d.clear())
# print(d1)
# print(id(d),id(d1))
#
key=["Name","Age"]
value=[1,2,3]
d=dict.fromkeys(key,value)
print(d)
#
#
# d1={1:'Jan',2:'Feb'}
# d2={1:'Mar',2:'Apr'}
# d1.update(d2)
# print(d1)
# print(d1.keys())
# print(d1.values())
# print(d1.get('Feb','Sorry!'))
# print(d1.items())