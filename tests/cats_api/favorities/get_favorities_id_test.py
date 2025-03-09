import pytest
import allure
from clients.rest.cats_api.favorities import (
    get_images,
    get_image_id,
    add_image_to_favorities,
    check_image_in_favorities,
    get_favorities_image_by_id)

@pytest.mark.favorities
@allure.feature("GET /v1/favourites/:favourite_id")
class TestFavorities:
    @allure.title("Получает картинку в favorities")
    def test_get_image_from_favorities_by_id(self, cats_api_auth):
        with allure.step("Шаг: Получение всех картинок, которые пока не добавлены в favorities"):
            images = get_images().json()
        with allure.step("Шаг: Присваивание image_id для конкретной картинки"):
            image_id = get_image_id(images=images)
        with allure.step("Шаг: Добавление этой картинки в favorities"):
            add_image_to_favorities(image_id, cats_api_auth)
        with allure.step("Шаг: Получение этой картинки в favorities"):
            response = get_favorities_image_by_id(image_id, cats_api_auth)

        with allure.step("Шаг:  Проверка код ответа равен 200"):
            assert response.status_code == 200, "Код ответа не равен 200"
