from tests.test_config import client


def test_drivate_query(client):
    response = client.get('/derivate/expression=x**3*y+y**3+z?related_to=x')
    data = response.json
    assert data == dict(total=5)