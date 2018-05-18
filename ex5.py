#Создать список с оценками учеников разных классов школы
#Посчитать и вывести средний балл по всей школе.
#Посчитать и вывести средний балл по каждому классу.
school_journal = [
{'school_class': '4a', 'scores': [3,4,4,5,2]} , 
{'school_class': '9b', 'scores': [5,2,3,5,4]} ,
{'school_class': '11d', 'scores': [4,3,2,3,3]}
]
all_school = []
for each in school_journal:
    summ_for_class = 0
    for score in each['scores']:
        summ_for_class += score
        score_in_klass = int(score)
        all_school.append(score_in_klass)
    print('Средний балл в', each['school_class'], summ_for_class/len(each['scores']))
average_all_school = 0
average_all_school = round(sum(all_school)/len(all_school), 2)
print ('Средний балл по школе:', average_all_school)
