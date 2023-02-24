from home.index import HomePage
from home.progress import ShowProgressPage
from home.reminder import ShowReminderPage
from flashcard.show import ShowFlashCardPage
from flashcard.add import AddFlashCardPage
from flashcard.edit import EditFlashCardPage
from flashcard.test import ShowTestPage
from cards.add import AddCardPage
from cards.show import ShowCardPage
from cards.edit import EditCardPage
import customtkinter

customtkinter.set_appearance_mode("light")

class Window(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        # Window Title and Geometry
        self.title("Flashcards App")
        self.geometry("1168x760")
        self.resizable(False, True)


        # Container to stack the pages
        self.container = customtkinter.CTkFrame(self, fg_color="white")
        self.container.pack(side="top", fill="both", expand=True)
        self.container.grid_rowconfigure(0, weight=1)
        self.container.grid_columnconfigure(0, weight=1)

        self.show_page("home")

        

    def show_page(self, page: str, data = None):
        for widget in self.container.winfo_children():
            widget.destroy()

        match page:
            case 'home':
                self.current_page = HomePage(
                    self.container,
                    app=self
                )
            case 'show_flashcard':
                self.current_page = ShowFlashCardPage(
                    self.container,
                    app=self,
                    flashcard = data
                )
            case 'add_flashcard':
                self.current_page = AddFlashCardPage(
                    self.container,
                    app=self,
                )

            case 'edit_flashcard':
                self.current_page = EditFlashCardPage(
                    self.container,
                    app=self,
                    flashcard=data
                )
            case 'add_card':
                self.current_page = AddCardPage(
                    self.container,
                    app=self,
                    flashcard=data
                )
            case 'show_card':
                self.current_page = ShowCardPage(
                    self.container,
                    app=self,
                    data=data
                )
            case 'edit_card':
                self.current_page = EditCardPage(
                    self.container,
                    app=self,
                    data=data
                )
            case 'start_test':
                self.current_page = ShowTestPage(
                    self.container,
                    app=self,
                    flashcard=data
                )
            case 'show_progress':
                self.current_page = ShowProgressPage(
                    self.container,
                    app=self,
                )
            case 'reminder':
                self.current_page = ShowReminderPage(
                    self.container,
                    app=self,
                )
            case _:
                print('Page Not found')

        # Render the page
        self.current_page.grid(
            row=0,
            column=0,
            sticky="nsew",
        )



app = Window()
app.mainloop()