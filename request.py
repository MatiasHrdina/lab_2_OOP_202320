#url: String

#get(): Dictionary
import requests

class Request:
    def __init__(self, url):
        self._url = url

    def get(self):
        Dictionary = requests.get(self._url)
        return Dictionary.json()
