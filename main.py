# url:String

#main(): None

from request import Request
from summary import Summary
from filter import Filter

class Main:
    def __init__(self):
        self._url = "https://andreshoward.com/pharmacies"

    def main(self, pharmacy):
        data = Request(self._url)
        summary = Summary(data.get())
        filtering = Filter(summary.call())
        print(filtering.apply(pharmacy))
        

main = Main()
main.main("AHUMADA")