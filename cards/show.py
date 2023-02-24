from icons.icons import edit_icon, cancel_icon
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
    search_bar_button = customtkinter.CTkButton(
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
        command=command
    )

    search_bar_button.grid(
        row=row,
        column=column,
        sticky="ew",
        ipadx=12,
        ipady=9,
        columnspan=columnspan,
        pady=pady,
        padx=padx
    )

    return search_bar_button


class ShowCardPage(customtkinter.CTkScrollableFrame):
    def __init__(self, master, app, data, **kwargs):
        super().__init__(master, **kwargs)

        self.app = app
        self.flashcard = data["flashcard"] 
        self.card = CD.get_card_by_id(data["flashcard"]["id"], data["card"]["id"]) 


        # App Configuration
        self.configure(fg_color="white")
        self.grid_columnconfigure(tuple(range(6)), weight=1, uniform="fre")


        # Page Title
        self.page_title = PageTitle(
            master=self,
            text="Show Card",
            columnspan=3
        )

        self.back_button = IconButton(
            master=self,
            text="Back",
            icon=cancel_icon,
            row=0,
            column=4,
            command=lambda: self.app.show_page("show_flashcard", self.flashcard),
        )

        self.edit_button = IconButton(
            master=self,
            text="Edit Card",
            icon=edit_icon,
            row=0,
            column=5,
            padx=(5, 0),
            command=lambda: self.app.show_page("edit_card", {"card": self.card,"flashcard": self.flashcard,}),
        )

        self.card_info = customtkinter.CTkFrame(
            master=self,
            fg_color="white",
            border_width=2,
            corner_radius=8,
            border_color="black",
        )

        self.card_info.grid(
            row=1,
            column=1,
            columnspan=4,
            sticky="nsew",
            pady=70
        )

        self.card_word = customtkinter.CTkLabel(
            master=self.card_info,
            text=self.card["word"],
            font=("Roboto Mono", 32),
            fg_color="white",
        )

        self.card_word.grid(
            row=0,
            column=0,
            pady=(27, 50),
            padx=17,
            sticky="w"
        )
        self.card_translation = customtkinter.CTkLabel(
            master=self.card_info,
            text=self.card["translation"],
            font=("Roboto Mono", 16, "bold"),
            fg_color="white",
        )

        self.card_translation.grid(
            row=1,
            column=0,
            pady=(0, 27),
            padx=17,
            sticky="w"
        )

        



