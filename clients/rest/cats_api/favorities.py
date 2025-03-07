import pytest
from clients.rest.base_http import send_request
from storage.urls import CatsApi
from storage.credentials import CatApiUser


def get_favorities_images(auth):
    return send_request("GET",CatsApi.FAVORITIES_URL,headers=auth)
def get_favorities_image_by_id(image_id, auth):
    return send_request("GET",f"{CatsApi.FAVORITIES_URL}/{image_id}",headers=auth)

def delete_image_from_favorities(image_id,auth):
    return send_request("DELETE", f"{CatsApi.FAVORITIES_URL}/{image_id}",headers=auth)

def delete_all_images_from_favorities(auth):
    favorite_images = get_favorities_images(auth).json()

    for image in favorite_images:
        image_id = image["id"]
        delete_image_from_favorities(image_id, auth)

def get_images(**kwargs):
    return send_request("GET",CatsApi.IMAGES_URL,**kwargs)

def get_image_id(images):
    return images[0]["id"]

def add_image_to_favorities(image_id, auth):
    body = {"image_id":image_id, "sub_id": "my-user-02345"}
    return send_request("POST",CatsApi.FAVORITIES_URL, json=body, headers=auth)


def check_image_in_favorities(image_id, auth):
    check = False
    favorities = send_request("GET", CatsApi.FAVORITIES_URL, headers=auth).json()
    for image in favorities:
        if image["image_id"]==image_id:
            check = True
        # check = True if image["id"]==image_id
    return check



