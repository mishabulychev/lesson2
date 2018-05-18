#Переписать функцию ask_user(), добавив обработку exception-ов
#Добавить перехват ctrl+C и прощание
answers = { 
'привет': "привет", 'как дела?':'Хорошо', 'пока':'пока'
}

def get_answer(questions,anwers):
    return answers.get(questions)

def ask_user(answers):
     while True:
        user=input('Скажи, не молчи: ')
        answer = get_answer(user, answers)
        print(answer)

        if user == 'Пока':
            print('Пока!')
            break

def stop_key_int(ask_user):
	try:
		print (ask_user(answers))
	except KeyboardInterrupt:
		print ('Еще увидимся!')

stop_key_int(ask_user)