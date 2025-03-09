import pytest
import allure
from clients.rest.cats_api.favorities import (
    get_images,
    get_image_id,
    add_image_to_favorites,
    get_favorite_image_by_id
)


@pytest.mark.cats_favorities
@allure.feature("GET /v1/favourites/favourite_id")
class TestFavorites:
    @allure.title("Запрос данных картинки из списка favorites по ID")
    def test_get_image_from_favorites_by_id(self, cats_api_auth):
        with allure.step("Шаг: Получение всех картинок, которые пока не добавлены в favorites"):
            images = get_images().json()
        with allure.step("Шаг: Присваивание image_id для конкретной картинки"):
            image_id = get_image_id(images=images)
        with allure.step(f"Шаг: Добавление картинки c image_id = {image_id} в favorites"):
            add_image_to_favorites(image_id, cats_api_auth)
        with allure.step(f"Шаг: Запрос данных картинки c image_id = {image_id}"):
            response = get_favorite_image_by_id(image_id, cats_api_auth)
        with allure.step("Проверка: Код ответа равен 200"):
            assert response.status_code == 200, "Код ответа не равен 200"
