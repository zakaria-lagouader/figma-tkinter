from icons.icons import drop_icon, plus_icon, home_icon
from tkinter.colorchooser import askcolor
from services import flashcard as FC
import customtkinter

def PageTitle(master, text: str, row = 0, column = 0, columnspan = 6, pady = 50, padx = 0):
    title = customtkinter.CTkLabel(
        master,
        text=text,
        font=("Roboto Mono", 32),
        fg_color="white"
    )

    title.grid(
        row=row,
        column=column,
        columnspan=columnspan,
        sticky="ew",
        pady=pady,
        padx=padx,
    )

    return title

def IconButton(master, text: str, icon = None, command = None, row = None, column = None, columnspan = None, pady = None, padx = None):
    button = customtkinter.CTkButton(
        master,
        text=text,
        font=("Roboto Mono", 16),
        cursor="hand2",
        fg_color="white",
        border_width=2,
        border_color="black",
        text_color="black",
        hover_color="#f4f4f4",
        image=icon, 
        compound="left",
        command=command,
        anchor="w"
    )

    button.grid(
        row=row,
        column=column,
        sticky="ew",
        ipadx=12,
        ipady=22,
        columnspan=columnspan,
        pady=pady,
        padx=padx
    )

    return button

def Input(master, placeholder_text: str, row = 0, column = 0, columnspan = 6, pady = 50, padx = 0):
    input = customtkinter.CTkEntry(
        master,
        placeholder_text=placeholder_text,
        font=("Roboto Mono", 14),
        fg_color="white",
        border_color="black",
        corner_radius=4,
        border_width=2,
    )

    input.grid(
        row=row,
        column=column,
        columnspan=columnspan,
        sticky="ew",
        ipadx=12,
        ipady=22,
        pady=pady,
        padx=padx
    )
    return input

class AddFlashCardPage(customtkinter.CTkScrollableFrame):
    def __init__(self, master, app, **kwargs):
        super().__init__(master, **kwargs)

        self.app = app

        # App Configuration
        self.configure(fg_color="white")
        self.grid_columnconfigure(tuple(range(6)), weight=1, uniform="col")


        # Page Title
        self.page_title = PageTitle(
            master=self,
            text="Add FlashCard"
        )

        self.name_input = Input(
            master=self,
            placeholder_text="Name",
            row=1,
            column=1,
            columnspan=4,
            pady=(50, 40)
        )

        self.color_input = IconButton(
            master=self,
            text="Choose Color",
            icon=drop_icon,
            row=2,
            column=1,
            columnspan=4,
            pady=(0, 80),
            command=self.shoose_color
        )

        self.add_button = IconButton(
            master=self,
            text="Add FlashCard",
            icon=plus_icon,
            row=3,
            column=1,
            columnspan=2,
            padx=(0, 5),
            command=self.add_flashcard
        )

        self.cancel_button = IconButton(
            master=self,
            text="Back Home",
            icon=home_icon,
            row=3,
            column=3,
            columnspan=2,
            padx=(5, 0),
            command=lambda: self.app.show_page("home")
        )

    def add_flashcard(self):
        name = self.name_input.get()
        color = self.color_input.cget("fg_color")

        if name != "" and color != "":
            flashcard = FC.add_flashcard(name, color)
            self.app.show_page("show_flashcard", flashcard)

    def shoose_color(self):
        colors = askcolor(
            title="Choisir une couleur", 
            initialcolor=self.color_input.cget("fg_color")
        )
        if colors[1] != None:
            self.color_input.configure(fg_color=colors[1], hover_color=colors[1])



