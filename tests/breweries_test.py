import pytest
from clients.rest.base_http import send_request
from storage.urls import BreweriesUrls


def test_get_breweries_list():
    response = send_request("GET", BreweriesUrls.BASE_URL)
    assert response.status_code == 200, "Код ответа равен 200"


@pytest.mark.parametrize("breweries_count", [1,3,5])
def test_get_breweries_by_per_page(breweries_count):
    print(BreweriesUrls.URL_PAGE.format(breweries_count))
    response = send_request("GET", BreweriesUrls.URL_PAGE.format(breweries_count))
    print(response.json())
    assert response.status_code == 200, "Код ответа равен 200"
    assert len(response.json()) == breweries_count, "Количество не равно ожидаемому"


@pytest.mark.parametrize("page, breweries_count", [(15, 1),(3, 2)])
def test_get_breweries_page_by_per_page(page, breweries_count):
    print(BreweriesUrls.URL_PAGE_BREWERIES.format(page, breweries_count))
    response = send_request("GET", BreweriesUrls.URL_PAGE_BREWERIES.format(page, breweries_count))
    print(response.json())
    assert response.status_code == 200, "Код ответа равен 200"
