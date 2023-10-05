import json
from unittest.mock import MagicMock, patch

import pytest
from conftest import raise_exception, test_client
from Product import Product


def test_ping(test_client):
    # Define the first step as fixture
    resp = test_client.get("/")
    assert resp.data.decode("ascii") == "ok"
    assert resp.status_code == 200


def test_get_products_success(test_client):
    """
    We test that we get successfully the available products in the database
    We mock the available products returned by the system
    """
    products_mock = [Product(1, "product name"), Product(2, "product name 2")]
    Product.find_all = MagicMock(return_value=products_mock)
    resp = test_client.get("/products")
    assert resp.status_code == 200
    assert json.loads(resp.data) == [p.json for p in products_mock]


def test_get_products_error(test_client):
    """
    We assert that we get an error when we could not connect to the given database
    We mock the returned value from the db query, and we define it as an exception
    """
    exception_message = "An exception occurred while retrieving all products"
    Product.find_all = MagicMock(side_effect=raise_exception)

    resp = test_client.get("/products")
    assert resp.status_code == 500
    assert resp.data.decode("ascii") == exception_message
