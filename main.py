# url:String

#main(): None

from request import Request
from summary import Summary
from filter import Filter

class Main:
    def __init__(self, url):
        self._url = url

    def main(self):
        data = Request(self._url)
        summary = Summary(data.get())
        filtering = Filter(summary.call())
        print(filtering.apply("CRUZ VERDE"))
        

Main("https://andreshoward.com/pharmacies").main()