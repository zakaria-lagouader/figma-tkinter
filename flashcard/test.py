from icons.icons import ok_icon, close_icon, cancel_icon
from services import flashcard as FC
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
        command=command,
        anchor="w"
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


class ShowTestPage(customtkinter.CTkFrame):
    def __init__(self, master, app, flashcard, **kwargs):
        super().__init__(master, **kwargs)

        self.app = app
        self.flashcard = FC.get_flashcard_by_id(flashcard["id"])
        self.cards = self.flashcard["cards"]
        self.card_index = 0
        self.current_card = self.cards[self.card_index]


        # App Configuration
        self.configure(fg_color="white")
        self.grid_columnconfigure(tuple(range(6)), weight=1, uniform="fre")

        self.progressbar = customtkinter.CTkProgressBar(
            master=self,
            progress_color="black"
        )

        self.progressbar.set(0)

        self.progressbar.grid(
            row=0,
            column=0,
            columnspan=6,
            sticky="nsew",
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
            pady=(150, 30)
        )

        self.card_info.grid_columnconfigure(0, weight=1, uniform="fred")

        self.card_info_language = customtkinter.CTkLabel(
            master=self.card_info,
            text="French:",
            font=("Roboto Mono", 64, "italic"),
            fg_color="white",
        )

        self.card_info_language.grid(
            row=0,
            column=0,
            pady=50,
            padx=17,
            sticky="ew"
        )
        self.card_info_word = customtkinter.CTkLabel(
            master=self.card_info,
            text=self.current_card["word"],
            font=("Roboto Mono", 48),
            fg_color="white",
        )

        self.card_info_word.grid(
            row=1,
            column=0,
            pady=27,
            padx=17,
            sticky="ew"
        )

        self.no_button = IconButton(
            master=self,
            row=2,
            column=1,
            columnspan=2,
            text="No",
            icon=close_icon,
            padx=(0, 5),
            command=self.onNoClick
        )
        self.no_button.grid_forget()

        self.yes_button = IconButton(
            master=self,
            row=2,
            column=3,
            columnspan=2,
            text="Yes",
            icon=ok_icon,
            padx=(5, 0),
            command=self.onYesClick
        )
        self.yes_button.grid_forget()

        self.animate_progress()

    def animate_progress(self, current = 0):
        next = current + 0.2
        if next >= 1 :
            self.progressbar.set(1)
            self.toggle_translation(show=True)
        else:
            self.progressbar.set(next)
            self.app.after(1000, self.animate_progress, next)

    def next_card(self):
        if self.card_index < len(self.cards) - 1:
            self.card_index += 1
            self.current_card = self.cards[self.card_index]
            self.toggle_translation(show=False)
            self.animate_progress()
        else:
            self.finish()

    def toggle_buttons(self, hide: bool):
        if hide:
            self.yes_button.grid_forget()
            self.no_button.grid_forget()
        else:
            self.no_button.grid(
                row=2,
                column=1,
                columnspan=2,
                padx=(0, 5),
                sticky="ew",
                ipadx=12,
                ipady=22,
            )

            self.yes_button.grid(
                row=2,
                column=3,
                columnspan=2,
                padx=(5, 0),
                sticky="ew",
                ipadx=12,
                ipady=22,
            )

    def toggle_translation(self, show: bool):
        if show:
            self.card_info_language.configure(text="English:")
            self.card_info_word.configure(text=self.current_card['translation'])
            self.toggle_buttons(hide=False)
        else:
            self.card_info_language.configure(text="Français:")
            self.card_info_word.configure(text=self.current_card['word'])
            self.toggle_buttons(hide=True)

    def onNoClick(self):
        words.add_word(
            word=self.current_card['word'],
            translation=self.current_card['translation'],
            is_correct=False
        )
        self.next_card()

    def onYesClick(self):
        words.add_word(
            word=self.current_card['word'],
            translation=self.current_card['translation'],
            is_correct=True
        )
        self.next_card()

    def finish(self):
        self.card_info.grid_forget()
        self.yes_button.grid_forget()
        self.no_button.grid_forget()
        self.progressbar.grid_forget()

        self.message_label = customtkinter.CTkLabel(
            master=self,
            text="You Have Finished The test",
            font=("Roboto Mono", 32),
            fg_color="white"
        )

        self.message_label.grid(
            row=0,
            column=0,
            columnspan=6,
            sticky="ew",
            pady=100,
        )

        self.back_button = IconButton(
            master=self,
            row=1,
            column=1,
            columnspan=4,
            text="Back To FlashCards",
            icon=cancel_icon,
            command=lambda: self.app.show_page("show_flashcard", self.flashcard)
        )

        



