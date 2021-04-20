from NB import NoteBook
import time
notebook = NoteBook()

running = True

while running:
    actions_txt = """
Выберите действие:

    1. Создать заметку
    2. Поиск по слову
    3. Выдать по номеру
    4. Закрыть программу

Напишите номер действия и нажмите [Enter]: """
    choose_action = int(input(actions_txt))

    if choose_action == 4:
        running = False
    elif choose_action == 1:
        num = notebook.create_note(input('Пишите:\n'))
        print('Заметка записана под номером ' + str(num))
    elif choose_action == 2:
        note = notebook.find_note(input('Введите поисковое слово: '))
        print('Найдена заметка :\n' + note)
    elif choose_action == 3:
        note = notebook.get_note(int(input('Введите номер заметки: ')))
        print('Найдена заметка :\n' + note)
    
    time.sleep(4)
