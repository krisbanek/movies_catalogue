from main import app
from unittest.mock import Mock
import tmdb_client
import pytest

@pytest.mark.parametrize('results, list_type', (
    ('results, popular'),
    ('results, top_rated')
))

def test_homepage(monkeypatch):
    api_mock = Mock(return_value={'results': ['list_type']})
    monkeypatch.setattr("tmdb_client.call_tmdb_api", api_mock)

    with app.test_client() as client:
        response = client.get('/')
        assert response.status_code == 200
        api_mock.assert_called_once_with('movie/popular')