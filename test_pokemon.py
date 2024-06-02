import requests
import pytest

URL = 'https://pokemonbattle.ru/v2'
TOKEN = '41f444b969c1989ab84c73465b7dd4e7'
HEADER = {'Conten-Type' : 'application/json', 'trainer_token' : TOKEN}
TRAINER_ID = 4113

def test_status_code():
    response = requests.get(url = f'{URL}/trainers', params = {'trainer_id' : TRAINER_ID})
    assert response.status_code == 200

def test_trainer_name():
    response_get = requests.get(url = f'{URL}/trainers', params = {'trainer_id' : TRAINER_ID})
    assert response_get.json()['name'] == 'Ira'