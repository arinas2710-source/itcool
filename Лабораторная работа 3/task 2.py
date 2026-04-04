# TODO Напишите функцию find_common_participants
def find_common_participants(i,a,r=','):
    one=i.split(r)# создаем список из 1 команды
    two=a.split(r)# создаем список из 2 команды
    f=[h for h in one if h in two] # проверяем нахождение одиноковых участников
    f.sort() #сортируем по алфавиту
    return f


first = "Иванов|Петров|Сидоров"
second = "Петров|Сидоров|Смирнов"
print (find_common_participants(first,second,'|'))
# TODO Провеьте работу функции с разделителем отличным от запятой
