import tkinter
import tkinter.messagebox
import customtkinter
from autoform import autofill
from functools import partial

customtkinter.set_appearance_mode("Light")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("green")  # Themes: "blue" (standard), "green", "dark-blue"


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        # configure window
        self.title("Form Bot")
        self.geometry(f"{720}x{400}")

        # create main entry and button
        self.first_name_entry = customtkinter.CTkEntry(self, placeholder_text="First Name")
        self.first_name_entry.grid(row=1, column=1, columnspan=1, padx=(20, 0), pady=(20, 0), sticky="ew")

        self.last_name_entry = customtkinter.CTkEntry(self, placeholder_text="Last Name")
        self.last_name_entry.grid(row=1, column=2, columnspan=1, padx=(20, 0), pady=(20, 0), sticky="ew")
        

        self.phone_entry = customtkinter.CTkEntry(self, placeholder_text="Phone")
        self.phone_entry.grid(row=2, column=1, columnspan=1, padx=(20, 0), pady=(20, 0), sticky="ew")
        
        self.email_entry = customtkinter.CTkEntry(self, placeholder_text="Email")
        self.email_entry.grid(row=2, column=2, columnspan=1, padx=(20, 0), pady=(20, 0), sticky="ew")

        self.street1_entry = customtkinter.CTkEntry(self, placeholder_text="Street 1")
        self.street1_entry.grid(row=3, column=1, columnspan=3, padx=(20, 0), pady=(20, 0), sticky="ew")

        self.street2_entry = customtkinter.CTkEntry(self, placeholder_text="Street 2")
        self.street2_entry.grid(row=4, column=1, columnspan=3, padx=(20, 0), pady=(20, 0), sticky="ew")

        self.state_entry = customtkinter.CTkEntry(self, placeholder_text="City")
        self.state_entry.grid(row=5, column=1, columnspan=1, padx=(20, 0), pady=(20, 0), sticky="ew")

        self.city_entry = customtkinter.CTkEntry(self, placeholder_text="State")
        self.city_entry.grid(row=5, column=2, columnspan=1, padx=(20, 0), pady=(20, 0), sticky="ew")

        self.zip_entry = customtkinter.CTkEntry(self, placeholder_text="Zip")
        self.zip_entry.grid(row=6, column=1, columnspan=2, padx=(20, 0), pady=(20, 0), sticky="ew")

        self.dob_entry = customtkinter.CTkEntry(self, placeholder_text="Date of Birth")
        self.dob_entry.grid(row=7, column=1, columnspan=1, padx=(20, 0), pady=(20, 0), sticky="ew")

        self.ssn_entry = customtkinter.CTkEntry(self, placeholder_text="SSN")
        self.ssn_entry.grid(row=7, column=2, columnspan=1, padx=(20, 0), pady=(20, 0), sticky="ew")
        
          # create sidebar frame with widgets
        self.sidebar_frame = customtkinter.CTkFrame(self, width=140, corner_radius=0)
        self.sidebar_frame.grid(row=0, column=0, rowspan=6, sticky="nsew")
        self.sidebar_frame.grid_rowconfigure(4, weight=1)
        self.logo_label = customtkinter.CTkLabel(self.sidebar_frame, text="Auto Form", font=customtkinter.CTkFont(size=20, weight="bold"))
        self.logo_label.grid(row=0, column=0, padx=20, pady=(20, 10))
        self.sidebar_button_1 = customtkinter.CTkButton(self.sidebar_frame, command=lambda: autofill(self.first_name_entry.get(), self.last_name_entry.get(), self.phone_entry.get(), self.email_entry.get(), self.street1_entry.get(), self.street2_entry.get(), self.city_entry.get(),  self.state_entry.get(), self.zip_entry.get(), self.dob_entry.get(), self.ssn_entry.get()), text='Submit')
        self.sidebar_button_1.grid(row=1, column=0, padx=20, pady=10)
        self.appearance_mode_label = customtkinter.CTkLabel(self.sidebar_frame, text="Appearance Mode:", anchor="w")
        self.appearance_mode_label.grid(row=6, column=0, padx=20, pady=(10, 0))
        self.appearance_mode_optionemenu = customtkinter.CTkOptionMenu(self.sidebar_frame, values=["Light", "Dark", "System"],
                                                                       command=self.change_appearance_mode_event)
        self.appearance_mode_optionemenu.grid(row=6, column=0, padx=20, pady=(10, 10))

    def open_input_dialog_event(self):
        dialog = customtkinter.CTkInputDialog(text="Type in a number:", title="CTkInputDialog")
        print("CTkInputDialog:", dialog.get_input())

    def change_appearance_mode_event(self, new_appearance_mode: str):
        customtkinter.set_appearance_mode(new_appearance_mode)

    def change_scaling_event(self, new_scaling: str):
        new_scaling_float = int(new_scaling.replace("%", "")) / 100
        customtkinter.set_widget_scaling(new_scaling_float)

    def sidebar_button_event(self):
        print("sidebar_button click")


if __name__ == "__main__":
    app = App()
    app.mainloop()
