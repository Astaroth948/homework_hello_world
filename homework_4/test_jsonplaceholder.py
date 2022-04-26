import requests
import pytest


@pytest.mark.parametrize(
    'resource, resources_len',
    [
        ('posts', 100),
        ('comments', 500),
        ('albums', 100),
        ('photos', 5000),
        ('todos', 200),
        ('users', 10)
    ]
)
def test_len_resources(resource: str, resources_len: int) -> None:
    response = requests.get(f'https://jsonplaceholder.typicode.com/{resource}')
    assert len(response.json()) == resources_len


@pytest.mark.parametrize('resource', ['posts', 'comments', 'albums', 'photos', 'todos', 'users'])
def test_open_resources_get(resource: str) -> None:
    response = requests.get(f'https://jsonplaceholder.typicode.com/{resource}')
    assert response.status_code == 200


@pytest.mark.parametrize('resource', ['posts', 'comments', 'albums', 'photos', 'todos', 'users'])
def test_open_resources_post(resource: str) -> None:
    response = requests.post(
        f'https://jsonplaceholder.typicode.com/{resource}')
    assert response.status_code == 201


def test_delete_post() -> None:
    response = requests.delete('https://jsonplaceholder.typicode.com/posts/1')
    assert response.status_code == 200


def test_photo_in_album() -> None:
    response = requests.get('https://jsonplaceholder.typicode.com/photos/1')
    assert response.json()['albumId'] == 1
