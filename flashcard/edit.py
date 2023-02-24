from icons.icons import drop_icon, edit_icon, cancel_icon, delete_icon
from tkinter.colorchooser import askcolor
from tkinter.messagebox import askyesno
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

def IconButton(master, text: str, icon = None, command = None, fg_color="white", row = None, column = None, columnspan = None, pady = None, padx = None):
    button = customtkinter.CTkButton(
        master,
        text=text,
        font=("Roboto Mono", 16),
        cursor="hand2",
        fg_color=fg_color,
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

class EditFlashCardPage(customtkinter.CTkScrollableFrame):
    def __init__(self, master, app, flashcard, **kwargs):
        super().__init__(master, **kwargs)

        self.app = app
        self.flashcard = FC.get_flashcard_by_id(flashcard["id"])

        # App Configuration
        self.configure(fg_color="white")
        self.grid_columnconfigure(tuple(range(6)), weight=1, uniform="col")


        # Page Title
        self.page_title = PageTitle(
            master=self,
            text=f"Edit {self.flashcard['name']}"
        )

        self.name_input = Input(
            master=self,
            placeholder_text="Name",
            row=1,
            column=1,
            columnspan=4,
            pady=(50, 40)
        )

        self.name_input.insert(0, self.flashcard["name"])

        self.color_input = IconButton(
            master=self,
            text="Choose Color",
            icon=drop_icon,
            row=2,
            column=1,
            columnspan=4,
            pady=(0, 80),
            command=self.shoose_color,
            fg_color=self.flashcard["color"]
        )

        self.edit_button = IconButton(
            master=self,
            text="Edit FlashCard",
            icon=edit_icon,
            row=3,
            column=1,
            columnspan=2,
            padx=(0, 5),
            command=self.edit_flashcard
        )

        self.delete_button = IconButton(
            master=self,
            text="Delete FlashCard",
            icon=delete_icon,
            row=3,
            column=3,
            columnspan=2,
            padx=(5, 0),
            command=self.delete_flashcard,
        )

        self.cancel_button = IconButton(
            master=self,
            text="Cancel",
            icon=cancel_icon,
            row=4,
            column=1,
            columnspan=4,
            pady=10,
            command=lambda: self.app.show_page("show_flashcard", self.flashcard)
        )

    def edit_flashcard(self):
        name = self.name_input.get()
        color = self.color_input.cget("fg_color")

        if name != "" and color != "":
            flashcard = FC.update_flashcard_by_id(self.flashcard["id"], name, color)
            self.app.show_page("show_flashcard", flashcard)

    def delete_flashcard(self):
        answer = askyesno(
            title='confirmation',
            message='vous souhaitez vraiment l\'effacer'
        )
        if answer:
            FC.delete_flashcard_by_id(self.flashcard["id"])
            self.app.show_page("home")


    def shoose_color(self):
        colors = askcolor(
            title="Choisir une couleur", 
            initialcolor=self.color_input.cget("fg_color")
        )
        if colors[1] != None:
            self.color_input.configure(fg_color=colors[1], hover_color=colors[1])



