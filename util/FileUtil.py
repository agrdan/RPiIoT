from os import path

# serverUrl: edu-agrdan.plusvps.com
# port: 1883

# edu-agrdan.plusvps.com;1883

class FileUtil:

    @staticmethod
    def writeServerInfo(fileName, info): #(fileName, serverUrl, port)
        with open(fileName, "w") as f:
            f.write(f"{info}") # f.write(f"{serverUrl};{port}")
            f.close()


    @staticmethod
    def readServerInfo(fileName):
        if path.exists(fileName):
            f = open(fileName, "r")
            line = f.readline()
            f.close()
            try:
                url, port = line.split(";")
                return url, port
            except:
                print("File does not contain server info.")
                return None, None
        else:
            print("File does not exist.")
            return None, None