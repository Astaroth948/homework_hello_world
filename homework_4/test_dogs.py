import requests
import pytest


def get_breeds() -> None:
    response = requests.get('https://dog.ceo/api/breeds/list/all')
    breeds = response.json()['message']
    for breed in breeds.keys():
        if len(breeds[breed]) == 0:
            yield breed
        for sub_breed in breeds[breed]:
            yield breed + '/' + sub_breed


def test_open_random_dog() -> None:
    response = requests.get('https://dog.ceo/api/breeds/image/random')
    assert response.status_code == 200


def test_jpg_random_dog() -> None:
    response = requests.get('https://dog.ceo/api/breeds/image/random')
    assert response.json()['message'][-4:] in ['.jpg', 'jpeg']


@pytest.mark.parametrize(
    'breed, quantity',
    [
        ('hound', 3),
        ('hound/afghan', 5),
        ('spaniel/welsh', 45),
    ]
)
def test_quantity_collections_by_breed(breed: str, quantity: int) -> None:
    response = requests.get(
        f'https://dog.ceo/api/breed/{breed}/images/random/{quantity}')
    assert len(response.json()['message']) == quantity


@pytest.mark.parametrize('breed', get_breeds())
def test_open_dogs_by_breed(breed: str) -> None:
    print(breed)
    response = requests.get(
        f'https://dog.ceo/api/breed/{breed}/images/random/1')
    assert response.status_code == 200


def test_quantity_sub_breeds_hound() -> None:
    response = requests.get('https://dog.ceo/api/breed/hound/list')
    assert len(response.json()['message']) == 7
