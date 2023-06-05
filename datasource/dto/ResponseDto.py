from util.JSONSerializator import JSONSerializator

class ResponseDto(JSONSerializator):

    def __init__(self):
        self.data = None
        self.message = None
        self.code = None