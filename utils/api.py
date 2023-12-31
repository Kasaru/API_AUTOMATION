from utils.http_methods import HttpMethods

"""Методы для тестирования Google Maps API"""

base_url = "https://rahulshettyacademy.com/"  # Базовая ссылка
key = "?key=qaclick123"  # Параметр для всех запросов


class GoogleMapsApi():
    """Метод для создания новой локации"""

    @staticmethod
    def create_new_place():
        json_for_create_new_location = {  # Тело post запроса
            "location": {
                "lat": -38.383494,
                "lng": 33.427362
            }, "accuracy": 50,
            "name": "Frontline house",
            "phone_number": "(+91) 983 893 3937",
            "address": "29, side layout, cohen 09",
            "types": [
                "shoe park",
                "shop"
            ],
            "website": "http://google.com",
            "language": "French-IN"
        }

        post_resource = "/maps/api/place/add/json"  # Ресурс метода post
        post_url = f"{base_url}{post_resource}{key}"  # составная ссылка метода post
        print(post_url)
        result_post = HttpMethods.post(post_url, json_for_create_new_location)
        print(result_post.text)
        return result_post

    """Метод для проверки новой локации"""
    @staticmethod
    def get_new_place(place_id):
        get_resource = "/maps/api/place/get/json"  # Ресурс метода get
        get_url = f"{base_url}{get_resource}{key}&place_id={place_id}"  # составная ссылка метода get
        print(get_url)
        result_get = HttpMethods.get(get_url)
        print(result_get.text)
        return result_get

    """Метод для изменения новой локации"""
    @staticmethod
    def put_new_place(place_id):
        json_for_update_new_location = {

            "place_id": f"{place_id}",

            "address": "Kremlin",

            "key": "qaclick123"

        }
        put_resource = "/maps/api/place/update/json"
        put_url = f"{base_url}{put_resource}{key}"
        print(put_url)
        result_put = HttpMethods.put(put_url, json_for_update_new_location)
        print(result_put.text)
        return result_put

        """Метод для удаления новой локации"""

    @staticmethod
    def delete_new_place(place_id):
        delete_resource = "/maps/api/place/delete/json"
        delete_url = f"{base_url}{delete_resource}{key}"
        print(delete_url)
        json_for_delete_new_location = {
            "place_id": f"{place_id}"
        }
        result_delete = HttpMethods.delete(delete_url, json_for_delete_new_location)
        print(result_delete.text)
        return result_delete