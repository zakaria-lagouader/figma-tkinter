from icons.icons import edit_icon, cancel_icon, delete_icon
from tkinter.messagebox import askyesno
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

class EditCardPage(customtkinter.CTkScrollableFrame):
    def __init__(self, master, app, data, **kwargs):
        super().__init__(master, **kwargs)

        self.app = app
        self.flashcard = data["flashcard"]
        self.card = CD.get_card_by_id(data["flashcard"]["id"], data["card"]["id"]) 

        # App Configuration
        self.configure(fg_color="white")
        self.grid_columnconfigure(tuple(range(6)), weight=1, uniform="col")


        # Page Title
        self.page_title = PageTitle(
            master=self,
            text="Edit Card"
        )

        self.word_input = Input(
            master=self,
            placeholder_text="Word",
            row=1,
            column=1,
            columnspan=4,
            pady=(50, 40)
        )

        self.word_input.insert(0, self.card["word"])

        self.translation_input = Input(
            master=self,
            placeholder_text="Translation",
            row=2,
            column=1,
            columnspan=4,
            pady=(0, 80)
        )

        self.translation_input.insert(0, self.card["translation"])

        self.edit_button = IconButton(
            master=self,
            text="Edit Card",
            icon=edit_icon,
            row=3,
            column=1,
            columnspan=2,
            padx=(0, 5),
            command=self.edit_card
        )

        self.delete_button = IconButton(
            master=self,
            text="Delete Card",
            icon=delete_icon,
            row=3,
            column=3,
            columnspan=2,
            command=self.delete_card
        )

        self.cancel_button = IconButton(
            master=self,
            text="Cancel",
            icon=cancel_icon,
            row=4,
            column=1,
            columnspan=4,
            pady=10,
            command=lambda: self.app.show_page("show_card", {"card": self.card,"flashcard": self.flashcard,})
        )

    def edit_card(self):
        word = self.word_input.get()
        translation = self.translation_input.get()

        if translation != "" and translation != "":
            CD.update_card_by_id(self.flashcard["id"], self.card["id"], word, translation)
            self.app.show_page("show_card", {"card": self.card,"flashcard": self.flashcard,})

    def delete_card(self):
        answer = askyesno(
            title='confirmation',
            message='vous souhaitez vraiment l\'effacer'
        )
        if answer:
            CD.delete_card_by_id(self.flashcard["id"], self.card["id"])
            self.app.show_page("show_flashcard", self.flashcard)




