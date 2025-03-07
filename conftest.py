import pytest
from storage.credentials import CatApiUser

@pytest.fixture(scope="session")
def cats_api_auth():
    return {"X-API-KEY" : CatApiUser.X_API_KEY}