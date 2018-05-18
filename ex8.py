#Написать функцию ask_user() чтобы с помощью input() спрашивать пользователя “Как дела?”,
#пока он не ответит “Хорошо”
def ask_user():
	while True:
		ask_user=input('Как дела? ')
		if ask_user == 'Хорошо':
			break
result = ask_user()