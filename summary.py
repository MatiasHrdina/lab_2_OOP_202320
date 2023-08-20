#data: List
#frequencies: Dictionary

#call(): Dictionary
#build_summary(): None
#process_element(): None
class Summary:
    def __init__(self, Dictionary):
        self._data = data
        self._frequencies = frequencies

    def call(self):
        self._build_summary()
        
    def _build_summary(self):
        for element in data:
            self._process_element(element)

    def _process_element(self, ):
        