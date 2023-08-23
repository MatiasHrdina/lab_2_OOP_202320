from request import Request
from summary import Summary
from filter import Filter

class Main:
    def __init__(self, url):
        self._url = url

    def main(self, pharmacy):
        data = Request(self._url)
        summary = Summary(data.get())
        filtering = Filter(summary.call())
        print(filtering.apply(pharmacy))
        

Main("https://andreshoward.com/pharmacies").main("CRUZ VERDE")