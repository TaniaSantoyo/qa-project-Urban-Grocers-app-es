import configuration
import requests
import data


def post_new_user(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH,
                         json=body,
                         headers=data.headers_user)  # Crear un usuario
response = post_new_user(data.user_body)
print(response.status_code)
print(response.json())   # Muestra del resultado en la consola


def post_products_kits(kit_body, token):
    # Realiza una solicitud POST para buscar kits por productos.
    current_body = data.headers_kit.copy()
    current_body["Authorization"] = "Bearer " + token
    return requests.post(configuration.URL_SERVICE + configuration.KITS_PATH,
                         # Concatenación de URL base y ruta.
                         json=kit_body,  # Datos a enviar en la solicitud.
                         headers=current_body)  # Encabezados de solicitud.


response = post_products_kits(data.kit_body, response.json()["authToken"])
print(response.status_code)
print(response.json())  # Muestra del resultado en la consola

def get_kits_table():
    return requests.get(configuration.URL_SERVICE + configuration.KITS_TABLE_PATH)

response = get_kits_table()
print(response.status_code)



