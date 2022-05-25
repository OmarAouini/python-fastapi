import requests


if __name__ == "__main__":
    max = 10000
    while max != 0:
        requests.get(url=f"http://localhost:8080/items/{max}")
        max = max -1