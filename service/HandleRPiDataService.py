from threading import Thread
from time import sleep as delay
from tkinter import ttk
from client.mqtt import MqttClient
from datasource.dto.RPiDto import RPiDto
from PIL import Image, ImageTk
from datetime import datetime as dt

class HandleRPiDataService(Thread):

    def __init__(self, mqtt: MqttClient, lblLight: ttk.Label, lblMovement: ttk.Label):
        super().__init__()
        self.interrupted = False
        self.mqtt = mqtt
        self.lblMovement = lblMovement
        self.lblLight = lblLight
        self.loadImages()
        self.lblMovement.config(image=self.noMovement)
        self.lblLight.config(image=self.lightOff)
        self.lightStatus = None
        self.time = None
        self.isBurglar = False
        self.isSave = False


    def run(self):

        while not self.interrupted:
            msg = self.mqtt.getFromQueue()
            if msg is not None:
                dto = RPiDto()
                try:
                    topic, message, time = msg.split(";")
                    dto.serialize(message, ignoreProperties=True)
                    print(dto.dumpModel())
                    if self.lightStatus != dto.light:
                        if dto.light:
                            self.lblLight.config(image=self.lightOn)
                        else:
                            self.lblLight.config(image=self.lightOff)
                        self.lightStatus = dto.light

                    self.time = dto.lastMotionDetected
                except Exception as e:
                    print(e)

            self.calculateTimeDifference()
            delay(1)

    def calculateTimeDifference(self):
        # 2023-05-31 20:34:24.622699

        if self.time is not None:
            dTime = dt.strptime(self.time, "%Y-%m-%d %H:%M:%S.%f")
            diff = dt.now() - dTime
            if diff.seconds < 20:
                if not self.isBurglar:
                    self.lblMovement.config(image=self.burglar)
                    self.isBurglar = True
                    self.isSave = False
            else:
                if not self.isSave:
                    self.lblMovement.config(image=self.noMovement)
                    self.isSave = True
                    self.isBurglar = False

    def close(self):
        self.interrupted = True

    def loadImages(self):
        lightOn = Image.open("images/light_on.png")
        lightOff = Image.open("images/light_off.png")
        burglar = Image.open("images/burglar.png")
        noMovement = Image.open("images/no_movement.png")

        self.lightOn = ImageTk.PhotoImage(lightOn)
        self.lightOff = ImageTk.PhotoImage(lightOff)
        self.burglar = ImageTk.PhotoImage(burglar)
        self.noMovement = ImageTk.PhotoImage(noMovement)

