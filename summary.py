#data: List
#frequencies: Dictionary

#call(): Dictionary
#build_summary(): None
#process_element(): None
class Summary:
    def __init__(self, Dictionary):
        self._data = Dictionary
        self._frequencies = []

    def call(self):
        self._build_summary()
        return self._frequencies
        
    def _build_summary(self):
        for element in self._data:
            self._process_element(element)

    def _process_element(self, element):
        processed = False
        for registered in self._frequencies:
          if registered['local_nombre'] in element['local_nombre']:
              registered['value'] += 1
              processed = True
            
        if not processed :
            self._frequencies.append({'local_nombre' : element['local_nombre'],'value' : 1})
