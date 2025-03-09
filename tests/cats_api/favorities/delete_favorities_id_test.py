import pytest
import allure
from clients.rest.cats_api.favorities import (
    get_images,
    get_image_id,
    add_image_to_favorites,
    check_image_in_favorites,
    delete_image_from_favorites
)


@pytest.mark.cats_favorities
@allure.feature("DELETE /v1/favourites/favourite_id")
class TestFavorites:
    @allure.title("Удаление картинки из списка favorites")
    def test_delete_image_from_favorites(self, cats_api_auth):
        with allure.step("Шаг: Получение всех картинок, которые пока не добавлены в favorites"):
            images = get_images().json()
        with allure.step("Шаг: Присваивание image_id для конкретной картинки"):
            image_id = get_image_id(images=images)
        with allure.step(f"Шаг: Добавление картинки c image_id = {image_id} в favorites"):
            add_image_to_favorites(image_id, cats_api_auth)
        with allure.step("Шаг: Удаление картинки из списка favourites"):
            delete_image_from_favorites(image_id, cats_api_auth)
        with allure.step(f"Проверка: Картинка c image_id = {image_id} удалена из favorites"):
            check = check_image_in_favorites(image_id, cats_api_auth)
            assert not check, f"Картинка {image_id} не удалена из избранного"
