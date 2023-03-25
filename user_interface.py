import functions
from logger import logging


file_path = '/home/tatkosen/Рабочий стол/Учёба/Python/Notes/notes.csv'


def Notes_main_menu():
    while True:
        main_choice = input("\nВас приветствует приложение Заметки!\n"
                            "\nВыберите действие:\n"
                            "\n1 - создание заметки\n"
                            "2 - редактирование заметки\n"
                            "3 - удаление заметки\n"
                            "4 - вывод списка заметок\n"
                            "5 - выборка по дате\n"
                            "6 - выгрузить данные\n"
                            "0 - выход\n")
        if int(main_choice) in range(1,7):
            Actions(main_choice)
        elif int(main_choice) == 0:
            logging.info("Exit programm")
            exit()
        else:
            logging.warning("Incorrect main menu input")
            print(f"\nПожалуйста выберите корректное действие.\n")


def Actions(main_choice):
    global file_path
    logging.info(f"Start actions menu")
    if int(main_choice) == 1:
        functions.Add_record(file_path)
        Return_menu()
    elif int(main_choice) == 2:
        functions.Change_record(file_path)
        Return_menu()
    elif int(main_choice) == 3:
        functions.Delete_record(file_path)
        Return_menu()
    elif int(main_choice) == 4:
        functions.Show_data(file_path)
        Return_menu()
    elif int(main_choice) == 5:
        functions.Search_by_date(file_path)
        Return_menu()
    elif int(main_choice) == 6:
        functions.Load_data(file_path)
        Return_menu()
        
def Return_menu():
    rep_or_fin=input("\nВы желаете продолжить работу?\n"
                     "1 - Да\n"
                     "2 - Нет (выход из программы)\n")
    if int(rep_or_fin)==1:
        Notes_main_menu()
    else:
        exit()