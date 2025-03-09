import requests


def send_request(method, resource_url, **kwargs):
    """
    Базовая функция для работы с http-запросами:
    - Отправляет http-request
    - Возвращает объект http-response
    """
    return requests.request(method, resource_url, **kwargs)
