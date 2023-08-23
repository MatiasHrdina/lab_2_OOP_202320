class Filter:
    def __init__(self, data):
        self._data = data
    
    def apply(self, pharmacy):
        for element in self._data:
            if element["local_nombre"] == pharmacy:
                return element
        return None
            
