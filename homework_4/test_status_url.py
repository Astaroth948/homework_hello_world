import requests


def test_status_url(url_and_status_code) -> None:
    response = requests.get(url_and_status_code['url'])
    assert response.status_code == url_and_status_code['status_code']
