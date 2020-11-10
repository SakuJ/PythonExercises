from student import Student

list = []

list.append(Student('Matti', 'Meikalainen', 'tvt18spo'))
list.append(Student('Antti', 'Ahola', 'tvt13spo'))
list.append(Student('Heikki', 'Hela', 'tvt19spo'))

print(list[0].Info())

for obj in list:
    obj.Info()