import requests
import pytest

host = "https://api.pokemonbattle.me:9104"
token = "f97e538cb3c5fca37ca513deca5b2612"


def test_status_code():
    response = requests.get(url=f'{host}/trainers')
    assert response.status_code == 200

def test_check_response():
    response = requests.get(url=f'{host}/trainers', params={'trainer_id': '3761'})
    assert response.json()['id'] == '3761'