from tests.test_config import client


def test_sum_query(client):
    response = client.get('/sums/query?value1=2&value2=3')
    data = response.json
    assert data == dict(total=5)


def test_sum_param(client):
    response = client.get('/sums/johndoe')
    data = response.json
    assert data == dict(your_name='johndoe')


def test_sum_body(client):
    body = dict(sum1=1, sum2=2)
    response = client.post('/sums', json=body)
    data = response.json
    assert data == dict(total=3)
