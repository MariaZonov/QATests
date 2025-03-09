from clients.rest.base_http import send_request
from storage.urls import CatsApiUrls


def get_favorite_images(auth):
    """Отправляет GET-запрос на получение избранных картинок"""
    return send_request("GET", CatsApiUrls.FAVORITIES_URL, headers=auth)


def get_favorite_image_by_id(image_id, auth):
    """Отправляет GET-запрос на получение избранной картинки по ID"""
    return send_request("GET",f"{CatsApiUrls.FAVORITIES_URL}/{image_id}", headers=auth)


def delete_image_from_favorites(image_id,auth):
    """Отправляет DELETE-запрос на удаление картинки по ID из списка избранных"""
    return send_request("DELETE", f"{CatsApiUrls.FAVORITIES_URL}/{image_id}", headers=auth)


def delete_all_images_from_favorites(auth):
    """Удаляет все картинки из списка избранных"""
    favorite_images = get_favorite_images(auth).json()

    for image in favorite_images:
        image_id = image["id"]
        delete_image_from_favorites(image_id, auth)


def get_images(**kwargs):
    """Отправляет GET-запрос на получение картинок"""
    return send_request("GET", CatsApiUrls.IMAGES_URL, **kwargs)


def get_image_id(images):
    """Возвращает ID картинки"""
    return images[0]["id"]


def add_image_to_favorites(image_id, auth):
    """Отправляет POST-запрос на добавление картинки в список избранных"""
    body = {"image_id":image_id, "sub_id": "my-user-02345"}
    return send_request("POST", CatsApiUrls.FAVORITIES_URL, json=body, headers=auth)


def check_image_in_favorites(image_id, auth):
    """
    Проверяет, находится ли картинка с указанным image_id в списке избранных:
    - Возвращает True, когда находится
    - Возвращает False, когда нет
    """
    check = False
    favorite_images = get_favorite_images(auth).json()
    for image in favorite_images:
        if image["image_id"] == image_id:
            check = True
    return check



