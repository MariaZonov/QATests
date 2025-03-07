import pytest
import allure
from clients.rest.cats_api.favorities import (
    get_images,
    get_image_id,
    add_image_to_favorities,
    check_image_in_favorities,
    delete_all_images_from_favorities,
    delete_image_from_favorities)

@pytest.mark.favorities
@allure.feature("DELETE /v1/favourites/:favourite_id")
class TestFavorities:
    @allure.title("Удаление картинки в favorities")
    def test_deleting_image_from_favorities(cats_api_auth):
        with allure.step("Шаг: Получение всех картинок, которые пока не добавлены в favorities"):
            images = get_images().json()
        with allure.step("Шаг: Присваивание image_id для конкретной картинки"):
            image_id = get_image_id(images=images)
        with allure.step("Шаг: Добавление этой картинки в favorities"):
            add_image_to_favorities(image_id, cats_api_auth)
        with allure.step("Шаг: Удаление этой картинки в favorities"):
            delete_image_from_favorities(image_id, cats_api_auth)

        with allure.step("Шаг:  Проверка об удалении этой картинки в favorities"):
            check = check_image_in_favorities(image_id, cats_api_auth)
            assert not check, f"Картинка {image_id} не удалена из избранного"

