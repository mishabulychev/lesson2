#Написать функцию, которая принимает на вход две строки.
#Если строки одинаковые, возвращает 1.
#Если строки разные и первая длиннее, возвращает 2.
#Если строки разные и вторая строка 'learn', возвращает 3.
def line(one,two):
	if len(one) == len(two):
		return 1
	elif len(one) > len(two):
		return 2
	elif len(one) != len('learn'):
		return 3

one = input ('Введите первую строку: ')
two = input ('Введите вторую строку: ')
result = line(one,two)
print (result)
