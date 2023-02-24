from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
from icons.icons import home_icon
import pandas as pd
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


class ShowProgressPage(customtkinter.CTkFrame):
    def __init__(self, master, app, **kwargs):
        super().__init__(master, **kwargs)

        self.app = app


        # App Configuration
        self.configure(fg_color="white")
        self.grid_columnconfigure(tuple(range(6)), weight=1, uniform="fre")

        self.page_title = PageTitle(
            master=self,
            text="Number Of Words You've Learned"
        )

        # Figure
        self.fig = Figure(
            figsize = (5, 5),
            dpi = 100
        )

  
        # adding the subplot
        self.plot = self.fig.add_subplot(111)

        # For fixing date display
        self.fig.autofmt_xdate()

        self.plot_words(self.plot)

        self.canvas = FigureCanvasTkAgg(
            figure=self.fig,
            master=self
        )

        self.canvas.draw()

        self.canvas.get_tk_widget().grid(
            row=1,
            column=1,
            columnspan=4,
            sticky="ew",
            pady=10, 
            padx=10 
        )

        self.back_button = IconButton(
            master=self,
            text="Back To Home",
            icon=home_icon,
            row=2,
            column=1, 
            columnspan=4,
            pady=(20, 0),
            command=lambda: self.app.show_page("home")
        )

    def plot_words(self, plt):
        # Create a list of dates and a list of number of words learned each day
        df = pd.read_csv('learned_words.csv')
        # correct_words = df[df["Correct"] == True]

        # Convert the 'date' column to a datetime object
        df['Date'] = pd.to_datetime(df['Date'])

        # Group the DataFrame by date and count the number of words learned on each day
        words_learned = df.groupby('Date')['Word'].count().reset_index(name='num_words')

        # Create a bar chart
        plt.bar(words_learned['Date'], words_learned['num_words'])

        # Create a line plot
        # plt.plot(words_learned['Date'], words_learned['num_words'])

        plt.locator_params(axis="y", integer=True, tight=True)

        # Add labels and title
        plt.set_xlabel('Date')
        plt.set_ylabel('Nombre de mots appris')
        plt.set_title('Mots appris chaque jour')

