from tkinter import ttk
import tkinter as tk
from util.ComponentUtil import ComponentUtil as cu


class CustomEntry(ttk.Frame):

    def __init__(self, parent, row, column, text, tkValue, isPassword=False):
        super().__init__(parent)
        self.grid(row=row, column=column, padx=5, pady=5, sticky=tk.E)

        self.lblText = ttk.Label(self, text=text)
        cu.placeComponent(self.lblText, 0, 0)

        self.entry = ttk.Entry(self, textvariable=tkValue)
        cu.placeComponent(self.entry, 0, 1)

        if isPassword:
            self.entry.config(show="*")