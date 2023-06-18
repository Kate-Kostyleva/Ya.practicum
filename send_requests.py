import configuration
import requests
import data


def post_new_order():
    return requests.post(configuration.URL_SERVICE + configuration.CREATING_AN_ORDER,
                         json=data.test_order)


def get_an_order(track_number):
    return requests.get(configuration.URL_SERVICE + configuration.GET_AN_ORDER_BY_NUMBER,
                         params={"t": track_number})