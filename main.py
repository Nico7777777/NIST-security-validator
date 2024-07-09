import tkinter as tk
import tkinter.messagebox as tkmsg
from tkinter import END

import customtkinter as ctk
from enum import Enum

from monobit import monoBit
from mbit import mBit
from serial import serial
from autocorelation import autocorrelation
from token_utils import *

ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")


class NIST(Enum):
    MONOBIT = 1
    MBIT = 2
    AUTOCORRELATION = 3
    SERIA = 4

test_number = NIST.MONOBIT
root = None


def open_input_dialog_event():
    dialog = ctk.CTkInputDialog(text="Type in a number:", title="CTkInputDialog")
    print("CTkInputDialog:", dialog.get_input())


def change_appearance_mode_event(new_appearance_mode: str):
    ctk.set_appearance_mode(new_appearance_mode)


def change_scaling_event(new_scaling: str):
    new_scaling_float = int(new_scaling.replace("%", "")) / 100
    ctk.set_widget_scaling(new_scaling_float)


def monobit_button_event():
    print("Monobit Event")
    global test_number
    test_number = NIST.MONOBIT


def mbit_button_event():
    print("MBit Event")
    global test_number
    test_number = NIST.MBIT


def autocorrelation_button_event():
    print("Autocorrelation Event")
    global test_number
    test_number = NIST.AUTOCORRELATION


def seria_button_event():
    print("Seria Event")
    global test_number
    test_number = NIST.SERIA


def run_test():
    root.textbox.delete('1.0', END)
    print(test_number)
    token = root.entry.get()
    print("The token is: " + token)

    token = formatToken(token)
    print("The formated token is: " + token)

    # Validate Token
    if not validateToken(token):
        root.textbox.insert("0.0", "The hash is not valid.")
        print("M-Bit response:", "Token not valid")
        return

    pop_up_alpha = ctk.CTkInputDialog(text="Enter the significance level: ", title="Alpha")
    alpha = float(pop_up_alpha.get_input())
    print(f"The alpha is: {alpha}")

    match test_number:
        case NIST.MONOBIT:
            # Call Monobit
            response = monoBit(alpha, token)
            root.textbox.insert("0.0", response)
            print("Monobit response:", response)
        case NIST.MBIT:
            # Read M
            pop_up_m = ctk.CTkInputDialog(text="Enter the sequence length: ", title="M value")
            m = int(pop_up_m.get_input())
            print(f"The m is: {m}")
            # Call MBit
            response = mBit(alpha, m, token)
            root.textbox.insert("0.0", response)
            print("M-Bit response:", response)
        case NIST.AUTOCORRELATION:
            # Read X
            pop_up_x = ctk.CTkInputDialog(text="Enter X: ", title="X")
            x = int(pop_up_x.get_input())
            print(f"The x is: {x}")
            # Read Y
            pop_up_y = ctk.CTkInputDialog(text="Enter Y: ", title="Y")
            y = int(pop_up_y.get_input())
            print(f"The y is: {y}")
            # Call Autocorrelation
            response = autocorrelation(len(token), token, alpha, x, y)
            root.textbox.insert("0.0", response)
            print("Autocorrelation response:", response)

        case NIST.SERIA:
            # Read M
            pop_up_m = ctk.CTkInputDialog(text="Enter the sequence length: ", title="M Value")
            m = int(pop_up_m.get_input())
            print(f"The m is: {m}")
            # Call Serial
            response = serial(len(token), token, alpha, m)
            root.textbox.insert("0.0", response)
            print("Serial response:", response)


class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        # window configuration
        self.title("NIST security validator")
        self.geometry(f"{2400}x{1250}")

        # configure grid layout - 4x4
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure((2, 3), weight=0)
        self.grid_rowconfigure((0, 1, 2), weight=1)

        # create sidebar frame with widgets
        self.sidebar_frame = ctk.CTkFrame(self, width=140, corner_radius=0)
        self.sidebar_frame.grid(row=0, column=0, rowspan=4, sticky="nsew")
        self.sidebar_frame.grid_rowconfigure(5, weight=1)  # Sidebar-ul va lua tot spatiul disponibil de ocupat
        self.logo_label = ctk.CTkLabel(self.sidebar_frame, text="N.S.V.", font=ctk.CTkFont(size=20, weight="bold"))

        self.sidebar_button_1 = ctk.CTkButton(self.sidebar_frame, command=monobit_button_event,
                                              text="Frequency Test")
        self.sidebar_button_1.grid(row=1, column=0, padx=20, pady=20)

        self.sidebar_button_2 = ctk.CTkButton(self.sidebar_frame, command=mbit_button_event,
                                              text="M-bit Test")
        self.sidebar_button_2.grid(row=2, column=0, padx=20, pady=20)

        self.sidebar_button_3 = ctk.CTkButton(self.sidebar_frame, command=autocorrelation_button_event,
                                              text="Autocorrelation Test")
        self.sidebar_button_3.grid(row=3, column=0, padx=20, pady=20)

        self.sidebar_button_4 = ctk.CTkButton(self.sidebar_frame, command=seria_button_event,
                                              text="Seria Test")
        self.sidebar_button_4.grid(row=4, column=0, padx=20, pady=20)

        # ------------------------------------------------------------------------------------------------
        self.appearance_mode_option_menu = ctk.CTkOptionMenu(self.sidebar_frame, values=["Light", "Dark", "System"],
                                                             command=change_appearance_mode_event)
        self.appearance_mode_option_menu.grid(row=6, column=0, padx=20, pady=(10, 10))

        self.scaling_label = ctk.CTkLabel(self.sidebar_frame, text="UI Scaling:", anchor="w")
        self.scaling_label.grid(row=7, column=0, padx=20, pady=(10, 10))
        self.scaling_option_menu = ctk.CTkOptionMenu(self.sidebar_frame, values=["90%", "100%", "150%", "175%", "200%"],
                                                     command=change_scaling_event)
        self.scaling_option_menu.grid(row=8, column=0, padx=20, pady=(10, 10))

        # INTERACTIUNEA CU USER-UL
        self.entry = ctk.CTkEntry(self, placeholder_text="Enter the hash")
        self.entry.grid(row=3, column=1, columnspan=2, padx=(20, 0), pady=(20, 20), sticky="nsew")

        self.main_button_1 = ctk.CTkButton(master=self, fg_color="transparent", border_width=2,
                                           text_color=("blue", "#DCE4EE"), text="Run tests", height=100, command=run_test)
        self.main_button_1.grid(row=3, column=3, padx=(20, 20), pady=(20, 20), sticky="nsew")

        # TEXTBOX
        self.textbox = ctk.CTkTextbox(self, width=250)
        self.textbox.grid(row=0, column=1, rowspan=3, columnspan=3, padx=(20, 20), pady=(20, 0), sticky="nsew")

        # set default values
        self.appearance_mode_option_menu.set("Dark")
        self.scaling_option_menu.set("100%")


if __name__ == "__main__":
    root = App()
    root.mainloop()
