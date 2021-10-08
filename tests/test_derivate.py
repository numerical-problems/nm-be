from tests.test_config import client


def test_drivate_query(client):
    body = dict(expression="3*x**2", related_to="x")
    response = client.post('/derivate', json=body)
    data = response.json
    assert data == (dict(result="6*x"))


def test_successive_derivation(client):
    body = dict(expression="3*x**2", related_to="x", times=2)
    response = client.post('/derivate/successive', json=body)
    data = response.json
    assert data == (dict(result="6"))