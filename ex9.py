#При помощи функции get_answer() отвечать на вопросы пользователя в ask_user(), 
#пока он не скажет “Пока!”
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

ask_user(answers)

