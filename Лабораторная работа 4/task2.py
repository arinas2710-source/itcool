# TODO импортировать необходимые молули
import json #обращаемся к библиотеке
import csv#обращаемся к библиотеке

INPUT_FILENAME = "input.csv"#файлу присваиваем значение переменной
OUTPUT_FILENAME = "output.json"#файлу присваиваем значение переменной


def task():
    with open(INPUT_FILENAME, 'r') as f:# открыть файл
        reader=csv.DictReader(f, delimiter=',')#преобразовываем каждую строку в словарь
        data=list(reader)#список из словарей
        with open(OUTPUT_FILENAME,'w') as f:# открыть другой файл
            json.dump(data,f,indent=4)# сереалиазуем формат json и  + отступы в 4 пробела
    ...  # TODO считать содержимое csv файла

    ...  # TODO Сериализовать в файл с отступами равными 4


if __name__ == '__main__':#
    # Нужно для проверки
    task()

    with open(OUTPUT_FILENAME) as output_f:
        for line in output_f:
            print(line, end="")
