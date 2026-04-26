def test_get_products(client):
    response = client.get("/products")
    assert response.status_code == 200
    assert isinstance(response.json(), list)


def test_get_product_by_id(client):
    response = client.get("/products/1")
    assert response.status_code in [200, 404]