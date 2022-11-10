from rest_framework import status
import pytest
# from model_bakery import baker


@pytest.fixture
def create_cart(api_client):
    def do_create_cart():
        return api_client.post('/store/carts/')
    return do_create_cart


@pytest.mark.django_db
class TestCreateCart:
    def test_if_user_is_authenticated(self, authenticate, create_cart):
        authenticate(is_staff=True)

        response = create_cart()

        assert response.status_code == status.HTTP_201_CREATED
