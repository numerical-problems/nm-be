from tests.test_config import client


def test_integrals_query(client):
    body = dict(expression="sin(x)*tan(x)", related_to="x", times=1)
    response = client.post("/integrals", json=body)
    data = response.json
    assert data == (dict(result="-log(sin(x) - 1)/2 + log(sin(x) + 1)/2 - sin(x)"))


def test_integrals_limit(client):
    body = dict(expression="2*x**2+1", related_to="x", limit_superior=2, limit_inferior=1)
    response = client.post("/integrals/limits", json=body)
    data = response.json
    assert data == (dict(result="17/3"))
