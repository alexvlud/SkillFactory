from clients import Client

cl1 = Client("Иван", "Петров", "Москва", 50)
cl2 = Client("Иван", "Драго", "Саратов", 150)
cl3 = Client("Петя", "Васечкин", "Анапа", 1150)
cl4 = Client("Вася", "Петров", "Сочи", 360)

cls = [cl1, cl2, cl3, cl4]
for clients in cls:
    print(clients.get_party())


#print(cl1)
#print(cl1.get_party())