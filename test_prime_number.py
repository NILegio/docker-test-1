import requests
from math import sqrt


def test_ping():
    raw = requests.get('http://localhost:8080/ping')
    assert raw.content == b'PONG'


def test_number():
    raw = requests.get('http://localhost:8080/number').json()
    assert isPrime(raw)


def test_number2():
    raw = requests.get('http://localhost:8080/number2').json()
    assert isPrime(raw)


def isPrime(number):
    for i in range (2,int(sqrt(number))+1):
        if number % i == 0: return False
    else: return True

