import requests


def decode(code):
    return requests.get('http://ip.starxy.cc/decode.php?code=' + code).json()
