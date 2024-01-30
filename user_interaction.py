from Vacancies import Vacancies
from JSONVacancyStorage import JsonData


def user_interaction():
    """
    Функция взаимодействия с пользователем для поиска вакансий, сохранения в файл и управления результатами.

    Процесс включает выбор платформы (HeadHunter или SuperJob), поиск вакансий, сохранение в файл,
    вывод результатов в консоль, удаление результатов и возможность повторного поиска.
    """
    print("Предлагаю поискать работу.")

    while True:
        user_input = input("Какой сайт Вас интересует?\n 1) HeadHunter;\n2) Superjob;\n0) выход: ")
        if user_input == "1":
            vacancies = Vacancies()
            vac_list = vacancies.vacancies_list_hh()
            json_data = JsonData()
            json_data.add(vac_list)
            second_user_input = input("Вывести результаты в консоль?\n1) да;\n2) нет;\n0) выход: ")
            while True:
                if second_user_input == "1":
                    json_data.read()
                    break
                elif second_user_input == "2":
                    break
                elif second_user_input == "0":
                    print("Завершение программы.")
                    quit()
                else:
                    print("Введите 1, 2 или 0!")
                    continue
            third_user_input = input("Удалить результаты поиска?\n1) да;\n2) нет;\n0) выход: ")
            while True:
                if third_user_input == "1":
                    json_data.delete()
                    break
                elif third_user_input == "2":
                    break
                elif third_user_input == "0":
                    print("Завершение программы.")
                    quit()
                else:
                    print("Введите 1, 2 или 0!")
                    continue
            fourth_user_input = input("Посмотреть еще вакансии?\n1) да;\n 2) нет: ")
            while True:
                if fourth_user_input == "1":
                    break
                elif fourth_user_input == "2":
                    print("Завершение программы.")
                    quit()
                else:
                    print("Введите 1, 2 или 0!")
                    continue
        elif user_input == "2":
            vacancies = Vacancies()
            vac_list = vacancies.vacancies_list_sj()
            json_data = JsonData()
            json_data.add(vac_list)
            second_user_input = input("Вывести данные о вакансиях в консоль?\n1) да;\n2) нет;\n0) выход: ")
            while True:
                if second_user_input == "1":
                    json_data.read()
                    break
                elif second_user_input == "2":
                    break
                elif second_user_input == "0":
                    print("Завершение программы.")
                    quit()
                else:
                    print("Введите 1, 2 или 0!")
                    continue
            third_user_input = input("Удалить список вакансий?\n1) да;\n2) нет;\n0) выход: ")
            while True:
                if third_user_input == "1":
                    json_data.delete()
                    break
                elif third_user_input == "2":
                    break
                elif third_user_input == "0":
                    print("Завершение программы.")
                    quit()
                else:
                    print("Введите 1, 2 или 0!")
                    continue
            fourth_user_input = input("Посмотреть еще вакансии?\n1) да;\n2) нет: ")
            while True:
                if fourth_user_input == "1":
                    break
                elif fourth_user_input == "2":
                    print("Завершение программы.")
                    quit()
                else:
                    print("Введите 1, 2 или 0!")
                    continue
        elif user_input == "0":
            print("Завершение программы.")
            quit()
        else:
            print("Введите 1, 2 или 0!")
            continue
