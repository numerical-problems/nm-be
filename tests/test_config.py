import pytest
from manage import app
from src.config.config import config_by_name


@pytest.fixture
def client():
    app.config.from_object(config_by_name['dev'])
    with app.test_client() as client:
        yield client
