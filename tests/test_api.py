"""
Tests for API handlers

"""
import json

import pytest

from app import create_app


@pytest.fixture(scope='module', autouse=True)
def client():
    app = create_app()
    return app.test_client()


def test_not_found(client):
    response = client.get('/noexist')
    assert response.status_code == 404
    parsed_data = json.loads(response.data)
    assert parsed_data.get('error') == 'Not Found'


def test_hello_world(client):
    response = client.get('/api/v1/hello/world')
    parsed_data = json.loads(response.data)
    assert response.status_code == 200
    assert parsed_data.get('hello') == 'world'


def test_hello_foo(client):
    response = client.get('/api/v1/hello/foo')
    parsed_data = json.loads(response.data)
    assert response.status_code == 200
    assert parsed_data.get('hello') == 'foo'
