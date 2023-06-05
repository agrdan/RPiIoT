from tkinter import ttk, StringVar, messagebox
import tkinter as tk
from screens.components.CustomEntry import CustomEntry
from util.ComponentUtil import ComponentUtil as cu
import requests
from datasource.dto.LoginRequestDto import LoginRequestDto
from datasource.dto.ResponseDto import ResponseDto
from screens.RPiScreen import RPiScreen


class LoginScreen(ttk.Frame):

    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.grid()
        self.initScreen()

    def initScreen(self):
        self.tkUsername = StringVar()
        self.tkPassword = StringVar()

        self.username = CustomEntry(self, 0, 0, "Username: ", self.tkUsername)
        self.password = CustomEntry(self, 1, 0, "Password: ", self.tkPassword, True)

        btnLogin = ttk.Button(self, text="Login", command=self.login)
        cu.placeComponent(btnLogin, 2, 0, sticky=tk.EW)

    def login(self):
        self.grid_remove()
        RPiScreen(self.parent)
        """
        if self.tkUsername.get() != "" and self.tkPassword.get() != "":
            loginRequest = LoginRequestDto(self.tkUsername.get(), self.tkPassword.get())
            response = requests.post(
                "http://edu-agrdan.plusvps.com/user-profile/login",
                json=loginRequest.dumpModel()
            )
            print(response.text)
            responseDto = ResponseDto()
            responseDto.serialize(response.text, ignoreProperties=False)
            if responseDto.code is not None:
                if responseDto.code == 200:
                    messagebox.showinfo("Login", responseDto.data)
                    self.grid_remove()
                    RPiScreen(self.parent)
                else:
                    messagebox.showerror("Error", responseDto.data)
            else:
                messagebox.showinfo("Error", "Check your request!")
        else:
            messagebox.showerror("Error", "Username and/or password should not be empty!")
        """