from icons.icons import search_icon, plus_icon, chart_icon, bell_icon
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

def SearchBar(master, row = None, column = None, columnspan = None, pady = None, padx = None):
    search_bar = customtkinter.CTkEntry(
        master,
        placeholder_text="Search...",
        font=("Roboto Mono", 16),
        fg_color="white",
        border_color="black",
        corner_radius=4,
        border_width=2,
    )

    search_bar.grid(
        row=row,
        column=column,
        columnspan=columnspan,
        sticky="ew",
        ipadx=12,
        ipady=12,
        pady=pady,
        padx=padx
    )
    return search_bar

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

class HomePage(customtkinter.CTkScrollableFrame):
    def __init__(self, master, app, **kwargs):
        super().__init__(master, **kwargs)

        self.app = app
        self.flashcards = FC.get_all_flashcards()
        self.flashcard_widgets = []

        # App Configuration
        self.configure(fg_color="white")
        self.grid_columnconfigure(tuple(range(6)), weight=1, uniform="col")


        # Page Title
        self.page_title = PageTitle(
            master=self,
            text="My FlashCards",
            columnspan=3
        )

        self.reminder_button = IconButton(
            master=self,
            text="Reminder",
            icon=bell_icon,
            row=0,
            column=3,
            padx=(0, 5),
            command=lambda: self.app.show_page("reminder")
        )

        self.add_flashcard_button = IconButton(
            master=self,
            text="Add FlashCard",
            icon=plus_icon,
            row=0,
            column=4,
            padx=(0, 5),
            command=lambda: self.app.show_page("add_flashcard")
        )

        self.progress_button = IconButton(
            master=self,
            text="Your Progress",
            icon=chart_icon,
            row=0,
            column=5,
            command=lambda: self.app.show_page("show_progress")
        )

        # Search bar
        self.search_bar = SearchBar(
            master=self,
            row=1,
            column=0,
            columnspan=5,
            pady=(0, 45),
            padx=(10, 0)
        )

        # SearchBUtton
        self.search_bar_button = IconButton(
            master=self,
            text="Search",
            icon=search_icon,
            row=1,
            column=5,
            pady=(0, 45),
            padx=(8, 10),
            command=self.filter_flashcards
        )

        self.empty_label = PageTitle(
            master=self,
            text="No FlashCards Found !",
            row=2,
            column=1,
            columnspan=4
        )

        self.render_list()
        

    def filter_flashcards(self):
        name = self.search_bar.get()
        self.flashcards = FC.get_by_flashcards_name(name)
        for w in self.flashcard_widgets:
            w.destroy()
        self.flashcard_widgets = []
        self.render_list()

    def render_list(self):
        if len(self.flashcards) == 0:
            self.empty_label.grid(
                row=2,
                column=1,
                columnspan=4,
                sticky="ew",
                pady=50,
            )
        else:
            self.empty_label.grid_forget()

        for i, flashcard in enumerate(self.flashcards):
            row = i // 3  # Determine the row index
            col = i % 3   # Determine the column index

            self.flashcard_item = FlashCardItem(
                master=self,
                app=self.app,
                flashcard=flashcard
            )

            self.flashcard_item.grid(
                row=row + 2,
                column=col * 2,
                columnspan=2,
                sticky="nsew",
                padx=10,
                pady=10
            )
            self.flashcard_widgets.append(self.flashcard_item)
        



class FlashCardItem(customtkinter.CTkFrame):
    def __init__(self, master, app = None, flashcard = None, **kwargs):
        super().__init__(master, **kwargs)

        self.flashcard = flashcard
        self.app = app

        self.configure(
            fg_color=self.flashcard["color"],
            border_width=2,
            border_color="black",
            cursor="hand2"
        )

        self.card_name = customtkinter.CTkLabel(
            master=self,
            text=self.flashcard["name"],
            font=("Roboto Mono", 32),
            fg_color=self.flashcard["color"],
        )

        self.card_name.grid(
            row=0,
            column=0,
            pady=(27, 50),
            padx=17,
            sticky="w"
        )
        cards_count = len(self.flashcard["cards"])
        self.card_count = customtkinter.CTkLabel(
            master=self,
            text=f"{cards_count} cards",
            font=("Roboto Mono", 16, "bold"),
            fg_color=self.flashcard["color"],
        )

        self.card_count.grid(
            row=1,
            column=0,
            pady=(0, 27),
            padx=17,
            sticky="w"
        )

        self.bind("<Button-1>", self.show_flashcard)

    def show_flashcard(self, event):
        self.app.show_page("show_flashcard", self.flashcard)