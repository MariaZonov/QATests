import pytest
import allure
from clients.rest.cats_api.favorities import (
    get_images,
    get_image_id,
    add_image_to_favorities,
    check_image_in_favorities,
    delete_all_images_from_favorities)

@pytest.mark.favorities
@allure.feature("POST /v1/favourites")
class TestFavorities:
    @allure.title("Добавление картинки в favorities")
    def test_adding_image_to_favorities(self, cats_api_auth):
        with allure.step("Шаг: Удаление всех картинок в favotities"):
            delete_all_images_from_favorities(cats_api_auth)
        with allure.step("Шаг: Получение всех картинок, которые пока не добавлены в favorities"):
            images = get_images().json()
        with allure.step("Шаг: Присваивание image_id для конкретной картинки"):
            image_id = get_image_id(images=images)
        with allure.step("Шаг: Добавление этой картинки в favorities"):
            add_image_to_favorities(image_id, cats_api_auth)

        with allure.step("Шаг:  Проверка о существовании картинки в favorities"):
            check = check_image_in_favorities(image_id, cats_api_auth)
            assert check, f"Картинка {image_id} не добавлена в избранное"
            # assert response.status_code == 200, "Код ответа равен 200"
        with allure.step("Шаг: Удаление всех картинок в favotities"):
            delete_all_images_from_favorities(cats_api_auth)