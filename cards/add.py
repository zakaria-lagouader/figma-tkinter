from icons.icons import plus_icon, cancel_icon
from services import cards as CD
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

class AddCardPage(customtkinter.CTkScrollableFrame):
    def __init__(self, master, app, flashcard, **kwargs):
        super().__init__(master, **kwargs)

        self.app = app
        self.flashcard = flashcard

        # App Configuration
        self.configure(fg_color="white")
        self.grid_columnconfigure(tuple(range(6)), weight=1, uniform="col")


        # Page Title
        self.page_title = PageTitle(
            master=self,
            text="Add Card"
        )

        self.word_input = Input(
            master=self,
            placeholder_text="Word",
            row=1,
            column=1,
            columnspan=4,
            pady=(50, 40)
        )

        self.translation_input = Input(
            master=self,
            placeholder_text="Translation",
            row=2,
            column=1,
            columnspan=4,
            pady=(0, 80)
        )

        self.add_button = IconButton(
            master=self,
            text="Add Card",
            icon=plus_icon,
            row=3,
            column=1,
            columnspan=2,
            padx=(0, 5),
            command=self.add_card
        )

        self.cancel_button = IconButton(
            master=self,
            text="Cancel",
            icon=cancel_icon,
            row=3,
            column=3,
            columnspan=2,
            padx=(5, 0),
            command=lambda: self.app.show_page("show_flashcard", self.flashcard)
        )

    def add_card(self):
        word = self.word_input.get()
        translation = self.translation_input.get()

        if translation != "" and translation != "":
            CD.add_card(self.flashcard["id"], word, translation)
            self.app.show_page("show_flashcard", self.flashcard)



