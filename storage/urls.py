class BreweriesURLS:
    BASE_URL = "https://api.openbrewerydb.org/v1/breweries"
    URL_PAGE = BASE_URL + "?per_page={0}"
    URL_PAGE_BREWERIES = BASE_URL + "?page ={0}&per_page={1}"
    URL_TYPE = BASE_URL + "?by_type=micro&per_page={0}"

class CatsApi:
    BASE_URL = "https://api.thecatapi.com"
    IMAGES_URL = BASE_URL + "/v1/images/search"
    FAVORITIES_URL = BASE_URL + "/v1/favourites"