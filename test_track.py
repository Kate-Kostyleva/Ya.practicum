#Екатерина Костылева, 5-я когорта — Финальный проект. Инженер по тестированию плюс.

import send_requests


def get_track_number_of_orders():
    track_number = send_requests.post_new_order()
    return track_number.json()["track"]


def test_successful_receipt_of_the_order_by_track():
    track_number = get_track_number_of_orders()
    get_response = send_requests.get_an_order(track_number)
    assert get_response.status_code == 200
