#Попросить пользователя ввести возраст.
#По возрасту определить, чем он должен заниматься: учиться в детском саду, школе, ВУЗе или работать.
#Вывести занятие на экран.
age = int(input("Введите свой возраст: "))
if age <= 6:
    print ("В детском саду ждет воспитатель!!")
elif age <= 18:
    print ("Вы должны учиться в школе")  
elif age <= 22:
    print ("Вы должны учиться в ВУЗе")
elif age > 22 :
    print ("Вы должны работать")
