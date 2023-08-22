# url:String

#main(): None

from request import Request
#from summary import Summary
#from filter import Filter

webpage = Request("https://andreshoward.com/pharmacies")
data = webpage.get()
print(data)
