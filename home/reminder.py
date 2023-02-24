from icons.icons import plus_icon, edit_icon, home_icon, play_icon
from services import words
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


class ShowReminderPage(customtkinter.CTkScrollableFrame):
    def __init__(self, master, app, **kwargs):
        super().__init__(master, **kwargs)

        self.app = app
        self.words = words.word_of_today()

        # App Configuration
        self.configure(fg_color="white")
        self.grid_columnconfigure(tuple(range(6)), weight=1, uniform="fre")


        # Page Title
        self.page_title = PageTitle(
            master=self,
            text="Reminder Of Today",
            columnspan=6
        )

        self.back_button = IconButton(
            master=self,
            text="Back To Home",
            icon=home_icon,
            row=0,
            column=5,
            command=lambda: self.app.show_page("home"),
        )

        if len(self.words) == 0:
            self.empty_label = PageTitle(
                master=self,
                text="No Words For Today !",
                row=1,
                column=1,
                columnspan=4
            )


        for i, card in enumerate(self.words):
            row = i // 3  # Determine the row index
            col = i % 3   # Determine the column index

            card_item = CardItem(
                master=self,
                app=self.app,
                card=card
            )

            card_item.grid(
                row=row + 1,
                column=col * 2,
                columnspan=2,
                sticky="nsew",
                padx=10,
                pady=10
            )


class CardItem(customtkinter.CTkFrame):
    def __init__(self, master, app = None, flashcard = None, card = None, **kwargs):
        super().__init__(master, **kwargs)

        self.card = card
        self.app = app

        self.configure(
            fg_color="white",
            border_width=2,
            border_color="black",
        )

        self.card_word = customtkinter.CTkLabel(
            master=self,
            text=self.card["Word"],
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
            text=self.card["Translation"],
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




