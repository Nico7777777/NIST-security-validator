import tkinter as tk
import tkinter.messagebox as tkmsg
import customtkinter as ctk
from autocorelation import *
from serial import *

ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")


def open_input_dialog_event():
    dialog = ctk.CTkInputDialog(text="Type in a number:", title="CTkInputDialog")
    print("CTkInputDialog:", dialog.get_input())


def change_appearance_mode_event(new_appearance_mode: str):
    ctk.set_appearance_mode(new_appearance_mode)


def change_scaling_event(new_scaling: str):
    new_scaling_float = int(new_scaling.replace("%", "")) / 100
    ctk.set_widget_scaling(new_scaling_float)


def sidebar_button_event():
    print("sidebar_button click")


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
        self.sidebar_frame.grid_rowconfigure(4, weight=1)  # Sidebar-ul va lua tot spatiul disponibil de ocupat
        self.logo_label = ctk.CTkLabel(self.sidebar_frame, text="N.S.V.", font=ctk.CTkFont(size=20, weight="bold"))

        # TODO: trebuie sa creez 4 event-listener diferite pentru cele 4 teste facute de Ema
        self.sidebar_button_1 = ctk.CTkButton(self.sidebar_frame, command=sidebar_button_event,
                                              text="Frequency Test")
        self.sidebar_button_1.grid(row=1, column=0, padx=20, pady=20)

        self.sidebar_button_2 = ctk.CTkButton(self.sidebar_frame, command=sidebar_button_event,
                                              text="M-bit Test")
        self.sidebar_button_2.grid(row=2, column=0, padx=20, pady=20)

        self.sidebar_button_3 = ctk.CTkButton(self.sidebar_frame, command=sidebar_button_event,
                                              text="Autocorrelation Test")
        self.sidebar_button_3.grid(row=3, column=0, padx=20, pady=20)

        self.sidebar_button_4 = ctk.CTkButton(self.sidebar_frame, command=sidebar_button_event,
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
        self.entry = ctk.CTkEntry(self, placeholder_text="Introduceti hash-ul aici")
        self.entry.grid(row=3, column=1, columnspan=2, padx=(20, 0), pady=(20, 20), sticky="nsew")

        self.main_button_1 = ctk.CTkButton(master=self, fg_color="transparent", border_width=2,
                                           text_color=("blue", "#DCE4EE"), text="Run tests", height=100)
        self.main_button_1.grid(row=3, column=3, padx=(20, 20), pady=(20, 20), sticky="nsew")

        # TEXTBOX
        self.textbox = ctk.CTkTextbox(self, width=250)
        self.textbox.grid(row=0, column=1, rowspan=3, columnspan=3, padx=(20, 20), pady=(20, 0), sticky="nsew")

        # set default values
        self.appearance_mode_option_menu.set("Dark")
        self.scaling_option_menu.set("100%")
        self.textbox.insert("0.0", "bla bla hat mat johnutule.\n\n" * 20)


if __name__ == "__main__":
    # app = App()
    # app.mainloop()
    # autocorelation()
    serial()