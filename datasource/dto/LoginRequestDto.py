from util.JSONSerializator import JSONSerializator


class LoginRequestDto(JSONSerializator):

    def __init__(self, username, password):
        self.username = username
        self.password = password


