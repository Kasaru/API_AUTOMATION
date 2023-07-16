import json

from utils.checking import Checking
from utils.api import GoogleMapsApi

"""Создание, изменение, удаление новой локации"""
class TestCreatePlace:

    def test_create_new_place(self):

        print("Метод POST")
        result_post = GoogleMapsApi.create_new_place()
        check_post = result_post.json()
        place_id = check_post.get("place_id")
        Checking.check_status_code(result_post,200)
        Checking.check_json_token(result_post,['status', 'place_id', 'scope', 'reference', 'id'])
        token = json.loads(result_post.text)
        print(list(token))
        Checking.check_json_value(result_post,'status', 'OK')

        print("Метод GET_POST")
        result_get  = GoogleMapsApi.get_new_place(place_id)
        Checking.check_status_code(result_get, 200)
        Checking.check_json_token(result_get,['location', 'accuracy', 'name', 'phone_number', 'address', 'types', 'website', 'language'])
        token = json.loads(result_get.text)
        print(list(token))
        Checking.check_json_value(result_get, 'address', "29, side layout, cohen 09")

        print("Метод PUT")
        result_put = GoogleMapsApi.put_new_place(place_id)
        print(result_put)
        Checking.check_status_code(result_put, 200)
        Checking.check_json_token(result_put,["msg"])
        token = json.loads(result_put.text)
        print(list(token))
        Checking.check_json_value(result_put, 'msg', "Address successfully updated")

        print("Метод GET_PUT")
        result_get = GoogleMapsApi.get_new_place(place_id)
        Checking.check_status_code(result_get, 200)
        Checking.check_json_token(result_get,['location', 'accuracy', 'name', 'phone_number', 'address', 'types', 'website', 'language'])
        token = json.loads(result_get.text)
        print(list(token))
        Checking.check_json_value(result_get, 'address', "Kremlin")

        print("Метод DELETE")
        result_delete = GoogleMapsApi.delete_new_place(place_id)
        print(result_delete)
        Checking.check_status_code(result_delete, 200)
        Checking.check_json_token(result_delete, ['status'])
        token = json.loads(result_delete.text)
        print(list(token))
        Checking.check_json_value(result_delete, 'status', "OK")

        print("Метод GET_DELETE")
        result_get = GoogleMapsApi.get_new_place(place_id)
        Checking.check_status_code(result_get, 404)
        Checking.check_json_token(result_get, ['msg'])
        token = json.loads(result_get.text)
        print(list(token))
        Checking.check_json_value(result_get, 'msg', "Get operation failed, looks like place_id  doesn't exists")
        Checking.check_json_search_word_in_value(result_get, 'msg', "failed, looks like place_id  doesn't exists")
        print("Тестирование создания, изменения и удаления новой локации прошло успешно!!!")