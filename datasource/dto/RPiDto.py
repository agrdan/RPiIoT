from util.JSONSerializator import JSONSerializator

"""
{
    "temperature": 27.0544140625, 
    "humidity": 56.457170377288946, 
    "pressure": 998.021063574601, 
    "objectDistance": 19.904661178588867, 
    "light": false, 
    "lastMotionDetected": "2023-05-31 19:50:51.507373"
}
"""

class RPiDto(JSONSerializator):

    def __init__(self):
        self.temperature = None
        self.humidity = None
        self.pressure = None
        self.light = None
        self.lastMotionDetected = None