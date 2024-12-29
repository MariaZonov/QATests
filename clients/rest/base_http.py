import requests


def send_request(method, resource_url, **kwargs):
    """функция для отправки http-запросов"""
    return requests.request(method, resource_url, **kwargs)

