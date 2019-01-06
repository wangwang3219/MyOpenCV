number = [1,2,3,4,5]

number.append(6)							# append插入一个元素
print(number)

number.extend([7,8])						# extend插入一个列表
print(number)

number.insert(0,0)							# insert在A处插入B
print(number)

print(number[2])							# 输出指定位置元素

number.remove(3)							# remove删除指定元素
print(number)

del number[0] 								# del删除指定位置元素
print(number)

del number									# 删除number列表

number = [1,2,3,4,5]

print('\n\n*************************************\n')

number.pop()
print(number)     							# 弹出(删除)number列表中最后一位

str = 'I love you'							#后者替换前者，不改变原字符串
print(str.replace('you','her'))

list1 = [1,3,2]
list2 = list1[:]
list1.sort(reverse =True)
print(list1)
print(sorted(list2))
print(reversed(list1))

str = "Fish.com"
for i in str:
	print(i)
for i in enumerate(str):
	print(i)

for i in range(4):							#range(i)执行i次循环
	print('s')

def add(num1,num2):
	"""这是一个
	函数文档。
	"""
	print("343")
	return num1+num2
print(add(2,5))								#还可写为print(add(num2 = 5,num1 = 2))
print(add.__doc__)							#获取函数add的函数文档

def text( * p, extre = 8'):
	print(extre)
text()

											#python所有函数默认返回"None"
def test():
	return 1,"i love",3.2
print(test())

g = lambda x, y : x + y + 1					#lamjbda 匿名函数(函数只使用一次时用匿名函数比普通函数更快捷)  简化代码的可读性
print(g(5,3))

print(list(map(lambda x : x * 2, range(10))))