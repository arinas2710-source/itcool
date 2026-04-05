import json # обращаемся к библиотеке
s1='input.json' #переменная с файлом
def s(s1): #объявляем функцию
    with open('input.json', 'r') as f:# открываю файл
        data=json.load(s1)#рпреобразуем в список
    a=sum((i['score']*['weight']) for i in data)# находим сумму произвведений
    return round(a,3) #возвращаем найденное значение и округляем до 3х знаков после запятой
m=s(s1) #вызываем функцию
print(m)
