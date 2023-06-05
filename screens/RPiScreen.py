from tkinter import ttk
import tkinter as tk
from client.mqtt import MqttClient
from service.HandleRPiDataService import HandleRPiDataService
from util.ComponentUtil import ComponentUtil as cu


class RPiScreen(ttk.Frame):

    def __init__(self, parent):
        super().__init__(parent)
        self.grid()
        self.mqtt = MqttClient(
            "edu-agrdan.plusvps.com",
            1883,
            "iot/+"
        )
        self.mqtt.start()

        self.initScreen()

    def initScreen(self):

        lblLight = ttk.Label(self)
        cu.placeComponent(lblLight, 0, 0)

        lblMovement = ttk.Label(self)
        cu.placeComponent(lblMovement, 1, 0)

        self.service = HandleRPiDataService(self.mqtt, lblLight, lblMovement)
        self.service.start()






