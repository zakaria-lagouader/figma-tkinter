from icons.icons import plus_icon, edit_icon, home_icon, play_icon
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


class ShowFlashCardPage(customtkinter.CTkScrollableFrame):
    def __init__(self, master, app, flashcard, **kwargs):
        super().__init__(master, **kwargs)

        self.app = app
        self.flashcard = FC.get_flashcard_by_id(flashcard["id"])
        self.cards = self.flashcard["cards"]

        # App Configuration
        self.configure(fg_color="white")
        self.grid_columnconfigure(tuple(range(6)), weight=1, uniform="fre")


        # Page Title
        self.page_title = PageTitle(
            master=self,
            text=self.flashcard["name"],
            columnspan=3
        )

        self.back_button = IconButton(
            master=self,
            text="Home",
            icon=home_icon,
            row=0,
            column=3,
            command=lambda: self.app.show_page("home"),
        )

        self.add_flashcard_button = IconButton(
            master=self,
            text="Add Card",
            icon=plus_icon,
            row=0,
            column=4,
            padx=10,
            command=lambda: self.app.show_page("add_card", self.flashcard),
        )

        self.edit_button = IconButton(
            master=self,
            text="Edit FlashCard",
            icon=edit_icon,
            row=0,
            column=5,
            command=lambda: self.app.show_page("edit_flashcard", self.flashcard),
        )

        if len(self.cards) == 0:
            self.empty_label = PageTitle(
                master=self,
                text="No Cards Found !",
                row=1,
                column=1,
                columnspan=4
            )
        else: 
            self.start_test_button = IconButton(
                master=self,
                text="Start Test",
                icon=play_icon,
                row=1,
                column=0,
                columnspan=6,
                padx=10,
                pady=20,
                command=lambda: self.app.show_page("start_test", self.flashcard),
            )

        for i, card in enumerate(self.cards):
            row = i // 3  # Determine the row index
            col = i % 3   # Determine the column index

            card_item = CardItem(
                master=self,
                app=self.app,
                flashcard=self.flashcard,
                card=card
            )

            card_item.grid(
                row=row + 2,
                column=col * 2,
                columnspan=2,
                sticky="nsew",
                padx=10,
                pady=10
            )


class CardItem(customtkinter.CTkFrame):
    def __init__(self, master, app = None, flashcard = None, card = None, **kwargs):
        super().__init__(master, **kwargs)

        self.flashcard = flashcard
        self.card = card
        self.app = app

        self.configure(
            fg_color="white",
            border_width=2,
            border_color="black",
            cursor="hand2",
        )

        self.card_word = customtkinter.CTkLabel(
            master=self,
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
            master=self,
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

        self.bind("<Button-1>", self.show_card)

    def show_card(self, event):
        self.app.show_page("show_card", {
            "card": self.card,
            "flashcard": self.flashcard,
        })



