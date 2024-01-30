from job_API import GetApiHeadHunter, GetApiSuperJob


class Vacancies:
    """
    Класс для обработки и сортировки вакансий.

    Attributes:
        vacancies_sorting (list): Список для сортировки вакансий.
        vacancies_sorted (list): Список отсортированных вакансий.
        vacancies_list (list): Конечный список вакансий.

    Methods:
        __init__(): Инициализация объекта Vacancies.
        __repr__(): Возвращает строковое представление объекта.
        salary_comparison_hh(): Сравнивает зарплаты и возвращает отсортированный список вакансий (HeadHunter).
        salary_comparison_sj(): Сравнивает зарплаты и возвращает отсортированный список вакансий (SuperJob).
        vacancies_list_hh(): Формирует список вакансий с информацией о зарплате (HeadHunter).
        vacancies_list_sj(): Формирует список вакансий с информацией о зарплате (SuperJob).
    """

    def __init__(self):
        self.vacancies_sorting = []
        self.vacancies_sorted = []
        self.vacancies_list = []

    def __repr__(self):
        """
        Возвращает строковое представление объекта.

        :return: Строковое представление объекта.
        """
        return f"""Конечный список вакансий: {self.vacancies_list}
Сортируемые вакансии: {self.vacancies_sorting}
Отсортированные вакансии: {self.vacancies_sorted}"""

    def salary_comparison_hh(self):
        """
        Сравнивает зарплаты и возвращает отсортированный список вакансий (HeadHunter).

        :return: Отсортированный список вакансий.
        """
        vacancies = GetApiHeadHunter.get_api_data()
        salary_sorting = sorted(list(vacancies.values()), reverse=True)
        for salary in salary_sorting:
            for key, value in vacancies.items():
                if salary == value:
                    self.vacancies_sorting.append(key)
        for i in self.vacancies_sorting:
            if i not in self.vacancies_sorted:
                self.vacancies_sorted.append(i)
        return self.vacancies_sorted

    def salary_comparison_sj(self):
        """
        Сравнивает зарплаты и возвращает отсортированный список вакансий (SuperJob).

        :return: Отсортированный список вакансий.
        """
        vacancies = GetApiSuperJob.get_api_data()
        salary_sorting = sorted(list(vacancies.values()), reverse=True)
        for salary in salary_sorting:
            for key, value in vacancies.items():
                if salary == value:
                    self.vacancies_sorting.append(key)
        for i in self.vacancies_sorting:
            if i not in self.vacancies_sorted:
                self.vacancies_sorted.append(i)
        return self.vacancies_sorted

    def vacancies_list_hh(self):
        """
        Формирует список вакансий с информацией о зарплате (HeadHunter).

        :return: Список вакансий с информацией о зарплате.
        """
        for vacancies in self.salary_comparison_hh():
            vacancies_dict = {"id вакансии": vacancies.split(",  ")[0], "название": vacancies.split(",  ")[1],
                              "начальная зарплата": vacancies.split(",  ")[2],
                              "конечная зарплата": vacancies.split(",  ")[3],
                              "валюта": vacancies.split(",  ")[4],
                              "город": vacancies.split(",  ")[5], "работодатель": vacancies.split(",  ")[6],
                              "ссылка на вакансию": vacancies.split(",  ")[7]}
            self.vacancies_list.append(vacancies_dict)
        return self.vacancies_list

    def vacancies_list_sj(self):
        """
        Формирует список вакансий с информацией о зарплате (SuperJob).

        :return: Список вакансий с информацией о зарплате.
        """
        for vacancies in self.salary_comparison_sj():
            vacancies_dict = {"id вакансии": vacancies.split(",  ")[0], "название": vacancies.split(",  ")[1],
                              "начальная зарплата": vacancies.split(",  ")[2],
                              "конечная зарплата": vacancies.split(",  ")[3],
                              "валюта": vacancies.split(",  ")[4], "город": vacancies.split(",  ")[5],
                              "ссылка на вакансию": vacancies.split(",  ")[6]}
            self.vacancies_list.append(vacancies_dict)
        return self.vacancies_list
