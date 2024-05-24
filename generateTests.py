import requests
import pytest

baseUrl = "https://jsonplaceholder.typicode.com/posts"

def test_product_list_returns_200():
    response = requests.get("https://jsonplaceholder.typicode.com/posts/1")
    assert response.status_code == 200

def test_product_list_response_is_not_empty():
    response = requests.get(baseUrl)
    assert len(response.json()) > 1

def test_product_list_response_item_has_id():
    response = requests.get(baseUrl)
    assert response.json()[0]["id"] is not None

def test_product_list_response_item_has_userId():
    response = requests.get(baseUrl)
    assert response.json()[0]["userId"] is not None

def test_product_list_response_item_has_title():
    response = requests.get(baseUrl)
    assert response.json()[0]["title"] is not None

def test_product_list_response_item_has_body():
    response = requests.get(baseUrl)
    assert response.json()[0]["body"] is not None

def test_delete_product():
    response = requests.delete("https://jsonplaceholder.typicode.com/posts/1")
    assert response.status_code == 200
    response = requests.get("https://jsonplaceholder.typicode.com/posts/1")
    assert response.status_code == 404
