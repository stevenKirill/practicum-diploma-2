body = {
    "firstName": "Naruto 24",
    "lastName": "Uchiha",
    "address": "Konoha, 142 apt.",
    "metroStation": 23,
    "phone": "+7 800 355 35 35",
    "rentTime": 5,
    "deliveryDate": "2020-06-06",
    "comment": "Saske, come back to Konoha",
    "color": [
        "BLACK"
    ]
}

headers = {
    "Content-Type": "application/json"
}

BASE_URL = "https://35b096d9-dab3-43b8-85a8-9dcd86424cb9.serverhub.praktikum-services.ru"
CREATE_ORDER = "/api/v1/orders"
GET_ORDER = "/api/v1/orders/track"
