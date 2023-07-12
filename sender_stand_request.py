import configuration
import requests
import data


def post_new_order(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDER_PATH,
                         json=body,
                         headers=data.headers)


def get_new_order_by_track(track):
    url = "{}/v1/orders/track?t={}".format(configuration.URL_SERVICE, track)
    return requests.get(url)


if __name__ == "__main__":
    created_order = post_new_order(data.order_body)
    print("Response:", created_order.json())
