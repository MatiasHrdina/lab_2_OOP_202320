#data: Dictionary

#apply(): Float

class Filter:
    def __init__(self, data):
        self._data = data
    
    def apply(self):
        for pharmacy in self._data:
            
