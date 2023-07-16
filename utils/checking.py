"""Методы для проверки ответов запросов"""
import json


class Checking():

    """Метод для проверки статус кода"""
    @staticmethod
    def check_status_code(result,status_code):
        assert status_code == result.status_code, f"Провал!!! Статус код = {result.status_code}"
        print(f"Успешно!!! Статус код = {result.status_code}")

    """Метод для проверки наличия обязательных полей в ответе запроса"""
    @staticmethod
    def check_json_token(result, expected_value):
        token = json.loads(result.text)
        assert list(token) == expected_value, "Присутствуют не все поля!"
        print("Все поля присутствуют")

    """Метод для проверки значения обязательных полей в ответе запроса"""
    @staticmethod
    def check_json_value(result, field_name, expected_value):
        check = result.json()
        check_info = check.get(field_name)
        assert check_info == expected_value, f"Значение {field_name} не верно: {check_info}"
        print(f"Значение {field_name} верно")

    """Метод для проверки значения обязательных полей в ответе запроса по заданному слову"""
    @staticmethod
    def check_json_search_word_in_value(result, field_name,search_word):
        check = result.json()
        check_info = check.get(field_name)
        assert search_word in check_info, f"Слово {search_word} присутствует в {field_name}"
        print(f"Слово {search_word} присутствует в {field_name}")
