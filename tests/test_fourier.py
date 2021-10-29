from tests.test_config import client


def test_fourier_200(client):
    body = dict(first_interval=-3.14, second_interval=3.14, expression="x + 1", n=3)
    response = client.post("/fourier", json=body)
    data = response.json
    assert data == dict(
        result="6.28*sin(0.318471337579618*pi*x)/pi - 3.14*sin(0.636942675159236*pi*x)/pi + 1.0"
    )
    assert response.status_code == 200


def test_fourier_400_missing_x(client):
    body = dict(first_interval=-3.14, second_interval=3.14, expression="y + 1", n=3)
    response = client.post("/fourier", json=body)
    assert response.status_code == 400


def test_fourier_400_invalid_interval(client):
    body = dict(first_interval=3.14, second_interval=3.14, expression="x + y + 1", n=3)
    response = client.post("/fourier", json=body)
    assert response.status_code == 400
