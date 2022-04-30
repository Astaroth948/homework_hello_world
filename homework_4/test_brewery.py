import requests
import pytest


def test_open_single_brewery() -> None:
    response = requests.get(
        'https://api.openbrewerydb.org/breweries/madtree-brewing-cincinnati')
    assert response.status_code == 200


def test_open_list_breweries() -> None:
    response = requests.get('https://api.openbrewerydb.org/breweries')
    assert response.status_code == 200


@pytest.mark.parametrize('quantity', [1, 10, 20, 30, 40, 50])
def test_quantity_breweries_per_page(quantity: int) -> None:
    response = requests.get(
        f'https://api.openbrewerydb.org/breweries?per_page={quantity}')
    assert len(response.json()) == quantity


@pytest.mark.parametrize('state', ['ohio', 'new_york', 'new%20mexico'])
def test_open_list_breweries_by_state(state: str) -> None:
    response = requests.get(
        f'https://api.openbrewerydb.org/breweries?by_state={state}')
    assert response.status_code == 200


@pytest.mark.parametrize('type_', ['micro', 'nano', 'regional', 'brewpub', 'large', 'planning', 'bar', 'contract', 'closed'])
def test_open_list_breweries_by_type(type_: str) -> None:
    response = requests.get(
        f'https://api.openbrewerydb.org/breweries?by_type={type_}')
    assert response.status_code == 200
