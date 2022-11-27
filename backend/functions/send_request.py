import requests


def send_post_request(url, data):
    response = requests.post(url, json=data)
    response.raise_for_status()
    return response.text
