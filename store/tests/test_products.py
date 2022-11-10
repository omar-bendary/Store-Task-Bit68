from rest_framework import status
import pytest


@pytest.mark.django_db
class TestProductList:
    def test_if_get_product_list_returns_200(self, api_client):

        response = api_client.get('/store/products/')

        assert response.status_code == status.HTTP_200_OK
