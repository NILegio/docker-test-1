import requests
from math import sqrt


def test_number():
    raw = requests.get('http://localhost:8080/number').json()
    assert isPrime(raw)


def isPrime(number):
    for i in range (2,int(sqrt(number))+1):
        if number % i == 0: return False
    else: return True
