from _pytest.config.argparsing import Parser
import pytest


def pytest_addoption(parser: Parser) -> None:
    parser.addoption('--url', action='store', default='https://ya.ru')
    parser.addoption('--status_code', action='store', default='200')


@pytest.fixture
def url_and_status_code(request: pytest.FixtureRequest) -> dict:
    return {
        "url": request.config.getoption("--url"),
        "status_code": int(request.config.getoption("--status_code"))
    }
