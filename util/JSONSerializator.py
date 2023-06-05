import json

class JSONSerializator:
    
    def serialize(self, model, ignoreProperties=True):
        try:
            m = self._loadModel(model)
            for key in m.keys():
                if ignoreProperties:
                    setattr(self, key, m.get(key))
                else:
                    if hasattr(self, key):
                        setattr(self, key, m.get(key))
        except Exception as e:
            print(e)

    def _loadModel(self, model):
        try:
            return json.loads(model)
        except Exception as e:
            print(e)

        return model

    def dumpModel(self):
        return json.dumps(self.__dict__, indent=4)

    def __repr__(self):
        return str(self.__dict__)

