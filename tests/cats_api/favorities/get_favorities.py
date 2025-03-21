import pytest
import allure
from clients.rest.cats_api.favorities import (
    get_favorite_images
)


@pytest.mark.cats_favorities
@allure.feature("GET /v1/favourites")
class TestFavorites:
    @allure.title("Запрос списка favorites")
    def test_get_favorite_images(self, cats_api_auth):
        with allure.step("Шаг: Получение всех картинок,добавленных в favorites"):
            response = get_favorite_images(cats_api_auth)
        with allure.step("Проверка: Код ответа равен 200"):
            assert response.status_code == 200, "Код ответа не равен 200"
