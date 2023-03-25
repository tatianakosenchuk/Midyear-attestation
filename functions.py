import exception
from os import path
from logger import logging
from tabulate import tabulate
from datetime import date
import csv


def Add_record(file_path):
    if path.exists(file_path):
        f= open(file_path, 'r', encoding='utf-8') 
    else:
        f= open(file_path, 'w+', encoding='utf-8') 
    data = list(csv.reader(f))
    f.close()
    new_ID = 1
    new_note = [input(f"Введите текст заметки\n")]
    if len(data) > 0:
        new_ID = int(data[0][2])
        max_ID = 0
        for item in data:
            if int(item[2]) > max_ID:
                max_ID = int(item[2])
        new_ID = max_ID + 1
    with open(file_path, 'a+', encoding='utf-8') as fle:
        new_note.insert(0, date.today().strftime('%d.%m.%Y'))
        new_note.insert(2, str(new_ID))
        csv.writer(fle, delimiter=",").writerow(new_note)
        logging.info(f"New note created, ID {new_ID}")


def Change_record(file_path):
    with open(file_path, 'r', encoding='utf-8') as fle:
        change_ID = input(f'\nВведите ID для редактирования:\n')
        data = list(csv.reader(fle))
        fle.seek(0)
        if exception.ID_check(change_ID, data):
            data[data.index(exception.ID_check(change_ID, data))][1] = input(
                    f"\nВведите новый текст заметки:\n")
            logging.info(f"Note ID {change_ID} was modified")
            open(file_path, 'w').close()
            with open(file_path, 'w', encoding='utf-8')as new_f:
                for row in data:
                    csv.writer(new_f).writerow(row)
        else:
            logging.warning(f"Incorrect ID {change_ID} for change")
            print(f"\nID {change_ID} не существует.\n")


def Delete_record(file_path):
    with open(file_path, 'r+', encoding='utf-8') as fle:
        delete_ID = input(f'\nВведите ID для удаления:\n')
        data = list(csv.reader(fle))
        if exception.ID_check(delete_ID, data):
            for row in data:
                if row[2] == delete_ID:
                    confirm = input(f"\nВы действительно желаете удалить запись?\n"
                                    f"{row[1]}\n"
                                    "1 - Да\n"
                                    "0 - Нет\n")
                    if int(confirm) == 1:
                        logging.info(f"Note ID {delete_ID} {row[1]} deleted")
                        open(file_path, 'w').close()
                        with open(file_path, 'w', encoding='utf-8')as new_fle:
                            for row in data:
                                if row[2] != delete_ID:
                                    csv.writer(new_fle).writerow(row)
                    else:
                        break
        else:
            logging.warning(f"Incorrect ID {delete_ID} for deletion")
            print(f"\nID {change_ID} не существует.\n")


def Show_data(file_path):
    with open(file_path, 'r', encoding='utf-8') as fle:
        print(tabulate([a for a in [row.replace('\n', '').split(',')
                                    for row in fle.readlines()]]))


def Search_by_date(file_path):
    with open(file_path, 'r', encoding='utf-8') as fle:
        date = input("Введите дату в формате dd.mm.yyyy:\n")
        data = list(csv.reader(fle))
        fle.seek(0)
        if exception.Seach_date_check(date, data):
            print(
                tabulate([a for a in [row for row in data if row[0] == date]]))
        else:
            logging.warning(f"No records for {date} found")
            print(f"\nЗаметки за {date} не найдены.\n")


def Load_data(file_path):
    f_format = 0
    while True:
        load_format = input(f'\nВыберите формат выгружаемого файла:\n'
                            '1 - csv\n'
                            '2 - txt\n')
        try:
            l_f = int(load_format) in range(1, 3)
        except:
            logging.warning("Incorrect loading format")
            print("\nПожалуйста выберите корректный формат файла.\n")
        else:
            load_path = input('\nВведите путь для сохранения файла:\n')
            if path.exists(load_path):
                file_name = input('\nВведите имя файла:\n')
                if int(load_format) == 1:
                    f_format = '.csv'
                elif int(load_format) == 2:
                    f_format = '.txt'
                with open(file_path, 'r+', encoding='utf-8') as fle:
                    with open(load_path+str(file_name)+str(f_format), 'w+', encoding='utf-8') as new_f:
                        for row in csv.reader(fle):
                            csv.writer(new_f).writerow(row)
                        exit()
            else:
                logging.warning("Incorrect file path for loading")
                print("\nПожалуйста введите корректный путь для сохранения файла.\n")
