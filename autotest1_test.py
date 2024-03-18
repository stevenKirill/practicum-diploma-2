import requests
import configuration


def create_order():
    return requests.post(configuration.BASE_URL + configuration.CREATE_ORDER,
                         json=configuration.body,
                         headers=configuration.headers,
                         )


def get_order(track_id):
    url = configuration.BASE_URL + configuration.GET_ORDER + '?t=' + track_id
    return requests.get(url)


def test_get_order():
    create_order_response = create_order().json()
    track_id = str(create_order_response['track'])
    get_order_response = get_order(track_id)
    order_data = get_order_response.json()
    print(order_data)
    assert get_order_response.status_code == 200


test_get_order()
