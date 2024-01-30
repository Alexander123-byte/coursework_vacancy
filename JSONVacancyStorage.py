from abc import ABC, abstractmethod
import json
import os


class AbstractVacancyStorage(ABC):
    """
    Абстрактный класс для хранения вакансий.
    """

    @abstractmethod
    def __repr__(self):
        """
        Абстрактный метод для представления объекта в виде строки.

        :return: Строковое представление объекта.
        """
        pass

    @abstractmethod
    def add(self, *args):
        """
        Абстрактный метод для добавления вакансий.

        :param args: Дополнительные аргументы, необходимые для добавления вакансии.
        """
        pass

    @abstractmethod
    def read(self):
        """
        Абстрактный метод для чтения вакансий из хранилища.
        """
        pass

    @abstractmethod
    def delete(self):
        """
        Абстрактный метод для удаления хранилища вакансий.
        """
        pass


class JsonData(AbstractVacancyStorage):
    """
    Класс для хранения вакансий в формате JSON.
    """

    def __init__(self):
        self.vacancies_save = f'{input("Введите название файла, куда сохранить вакансии: ")}.json'

    def __repr__(self):
        """
        Возвращает строковое представление объекта.

        :return: Строковое представление объекта.
        """
        return f"Файл {self.vacancies_save}"

    def add(self, vac_data):
        """
        Добавляет вакансии в файл в формате JSON.

        :param vac_data: Словарь с информацией о вакансиях.
        """
        with open(self.vacancies_save, 'w', encoding='utf-8') as json_file:
            json.dump(vac_data, json_file, ensure_ascii=False, indent=4)
        print(f"Результат успешно сохранен в {self.vacancies_save}")

    def read(self):
        """
        Читает вакансии из файла и предоставляет пользователю возможность выбора критериев.
        """
        with open(self.vacancies_save, 'r', encoding='utf-8') as json_file:
            data = json.load(json_file)
            count = True
            while count:
                user_input = input("""Введите цифру для выбора критериев отображения:
1: id вакансии, конечная зарплата, валюта, ссылка на вакансию;
2: название вакансии, конечная зарплата, город, ссылка на вакансию;
3: полный список. """)
                if len(data) == 0:
                    count = False
                    print(f"В файле {self.vacancies_save} вакансий не нашлось.")
                else:
                    if user_input != "1" and user_input != "2" and user_input != "3":
                        print("Введите 1, 2 или 3!")
                    else:
                        for dat in data:
                            print("")
                            if user_input == "1":
                                count = False
                                print(f'''"id вакансии": {dat["id вакансии"]}
"конечная зарплата": {dat["конечная зарплата"]}
"город": {dat["город"]}
"ссылка на вакансию": {dat["ссылка на вакансию"]}''')
                            elif user_input == "2":
                                count = False
                                print(f'''"название": {dat["название"]}
"конечная зарплата": {dat["конечная зарплата"]}
"валюта": {dat["валюта"]}
"ссылка на вакансию": {dat["ссылка на вакансию"]}''')
                            elif user_input == "3":
                                count = False
                                for k, v in dat.items():
                                    print(f"{k}: {v}")
                            print("")

    def delete(self):
        """
        Удаляет файл с вакансиями.
        """
        os.remove(os.path.join(self.vacancies_save))
        print(f"Файл {self.vacancies_save} успешно удален.")
