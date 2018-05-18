#Перепишите предыдущий пример в виде функции find_person(name), которая ищет имя в списке.
def find_person(name):
	name_list = ["Вася", "Маша", "Петя", "Валера", "Саша", "Даша", "Оля", "Миша", "Катя", "Гоша", "Витя", "Коля"]
	while name_list:
#		print(name_list[-1])
#		print(name_list)
		if name_list.pop() == name:
			result = str(name) + " " + str("нашелся(лась)")
			break
		else:
			result = ("Такого имени не найдено")	
	return result

name = input ("Введите нужное имя: ")
result = find_person(name)
print (result)