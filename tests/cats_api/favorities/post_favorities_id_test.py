import pytest
import allure
from clients.rest.cats_api.favorities import (
    get_images,
    get_image_id,
    add_image_to_favorites,
    check_image_in_favorites,
    delete_all_images_from_favorites
)


@pytest.mark.cats_favorities
@allure.feature("POST /v1/favourites")
class TestFavorites:
    @allure.title("Добавление картинки в список favorites")
    def test_add_image_to_favorites(self, cats_api_auth):
        with allure.step("Pre Condition: Удаление всех картинок из списка favorites"):
            delete_all_images_from_favorites(cats_api_auth)
        with allure.step("Шаг: Получение всех картинок, которые пока не добавлены в favorites"):
            images = get_images().json()
        with allure.step("Шаг: Присваивание image_id для конкретной картинки"):
            image_id = get_image_id(images=images)
        with allure.step(f"Шаг: Добавление картинки c image_id = {image_id} в favorites"):
            add_image_to_favorites(image_id, cats_api_auth)
        with allure.step("Шаг:  Проверка о существовании картинки в favorites"):
            check = check_image_in_favorites(image_id, cats_api_auth)
            assert check, f"Картинка {image_id} не добавлена в избранное"
        with allure.step("Post Condition: Удаление всех картинок из списка favorites"):
            delete_all_images_from_favorites(cats_api_auth)
