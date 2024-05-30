import data
import sender_stand_request

def get_kit_body(name):
    current_body = data.kit_body.copy()
    current_body["name"] = name
    return current_body
def get_new_user_token():
    current_body = data.user_body.copy()
    user_response = sender_stand_request.post_new_user(current_body)
    return user_response.json()["authToken"]

def positive_assert_kit(kit_body):
    token = get_new_user_token()
    kit_response = sender_stand_request.post_products_kits(kit_body, token)
    kit_table_response = sender_stand_request.get_kits_table()
    str_kit = str(kit_response.json()["id"]) + ',' + kit_response.json()["name"]
    assert kit_table_response.text.count(str_kit) == 1

def negative_assert_code_400(kit_body_negative):
    token = get_new_user_token()
    kit_response = sender_stand_request.post_products_kits(kit_body_negative, token)
    assert kit_response.status_code == 400
    assert kit_response.json()["message"] == "No se han aprobado todos los parámetros requeridos"


def test_create_kit_1_letter():
    kit = get_kit_body("a")
    positive_assert_kit(kit)

    # Prueba 2
def test_create_kit_511_letters():
    kit = get_kit_body("AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabC")
    positive_assert_kit(kit)

    # Prueba 3
def test_create_kit_0_letters(x):
    kit = get_kit_body("")
    negative_assert_code_400(kit)

    # Prueba 4
def test_create_kit_512_letters():
    kit = get_kit_body("AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcD")
    negative_assert_code_400(kit)

    # Prueba 5
def test_create_kit_has_special_symbol_name():
    kit = get_kit_body("\"№%@\",")
    positive_assert_kit(kit)

    # Prueba 6
def test_create_kit(x):
    kit = get_kit_body(" A Aaa ")
    positive_assert_kit(kit)


    # Prueba 7
def test_create_kit_has_number():
    kit = get_kit_body("123")
    positive_assert_kit(kit)

    # Prueba 8
def test_create_kit_0_letters():
    kit = get_kit_body("")
    negative_assert_code_400(kit)

        # Prueba 9
def test_create_kit_has_number_get_error_response():
    kit = get_kit_body(123)
    negative_assert_code_400(kit)