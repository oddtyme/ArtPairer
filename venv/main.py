# import Tkinter fof GUI framework
from tkinter import *
from Assets import *
import random

class Album:
    Name = ""
    Mood = ""
    Artist = ""
    Year = 0
    Genre = ""

    def __init__(self, name, artist, year, genre, mood):
        self.Name = name
        self.Artist = artist
        self.Year = year
        self.Genre = genre
        self.Mood = mood


class Piece:
    Name = ""
    Artist = ""
    Year = ""
    Movement = ""
    Mood = ""
    Image = []

    def __init__(self, name, artist, year, movement, mood, image):
        self.Name = name
        self.Artist = artist
        self.Year = year
        self.Movement = movement
        self.Mood = mood
        self.Image = image


# Main App class and and behaviour
class App:

    def __init__(self, master):

        # parent widget
        self.master = master
        master.title("Art Pairer")

        # Declaration and display of welcome text
        self.welcome = Label(master, text="Welcome to ArtPairer!", anchor='n')
        self.welcome.pack()

        # Declaration and display of instruction text
        self.instructions = Label(master, text="Please enter an album to see"
                                               " what it pairs well with.")
        self.instructions.pack()

        searchbar = Frame(master)

        # Declaration and display of search
        self.search = Entry(searchbar, width=70)
        self.search.grid(row=2, column=1)

        self.artfr = Frame(master)

        self.Analysis = Label()
        self.Picture = Label()
        self.Error = Label()

        # TODO Allow user to push button using Enter key
        # Push method: what happens when you click "Pair"
        def push():
            # Erase current picture and description
            self.artfr.pack_forget()
            self.Analysis.pack_forget()
            self.Picture.pack_forget()
            self.Error.pack_forget()

            text = self.search.get()

            print((text in album_directory))
            # check for existence of album
            if not text in album_directory:
                self.Error = Label(self.artfr, text="Album not found! Please check for misspellings, or try another.")
                self.Error.pack()
                self.artfr.pack()
            else:
                mood = album_directory.get(text).Mood

                candidates = piece_directory.get(mood)

                self.i = 0

                # Refresh function for button
                def refresh():
                    self.Analysis.pack_forget()
                    self.Picture.pack_forget()
                    self.artfr.pack_forget()

                    if self.i == len(candidates) - 1:
                        self.i = 0
                    else:
                        self.i = self.i + 1

                    print(self.i)

                    next = candidates[self.i]

                    print(next.Name)
                    analysis = text + " pairs well with " + "\"" + next.Name + "\" by " + next.Artist + \
                            ". This " + next.Movement + " piece was completed in " + str(next.Year) + "."
                    self.Analysis = Label(self.artfr, text=analysis)
                    self.Analysis.pack()
                    self.Picture = Label(self.artfr, image=next.Image)
                    self.Picture.pack()

                    self.artfr.pack()

                # Refresh Button
                Refresh = Button(searchbar, text="Next", command=refresh)
                Refresh.grid(row=2, column=3)

                first_result = candidates[self.i]
            
                analysis = text + " pairs well with " + "\"" + first_result.Name + "\" by " + first_result.Artist + \
                           ". This " + first_result.Movement + " piece was completed in " + str(first_result.Year) + "."
                self.Analysis = Label(self.artfr, text=analysis)
                self.Analysis.pack()
                self.Picture = Label(self.artfr, image=first_result.Image)
                self.Picture.pack()

                self.artfr.pack()

        # Declaration and display of pair button
        self.button = Button(searchbar, text="Pair", command=push)
        self.button.grid(row=2, column=2)

        searchbar.pack()

    @staticmethod
    def create_album_dict():
        # TODO Enter many new albums *OR* Find way to do so algorithmically
        # Album Creation
        master_of_puppets = Album("Master of Puppets", "Metallica", 1986, "Thrash Metal", "Aggressive")

        # TODO Enter many new pieces *OR* Find way to do so algorithmically
        # Set Creation
        album_list = dict([('Master of Puppets', master_of_puppets)])
        return album_list

    @staticmethod
    def create_piece_dict():
        # Piece Creation
        destruction = Piece("Destruction (The Course of an Empire)", "Thomas Cole", 1836, "Romantic", "Aggressive",
                            PhotoImage(file="C:/Users/seamus/PycharmProjects/ArtPairer/venv/Assets/Destruction.PPM"))
        dante_and_virgil_in_hell = Piece("Dante and Virgil", "William-Adolphe Bouguereau", 1850, "Romantic", "Aggressive",
                            PhotoImage(file="C:/Users/seamus/PycharmProjects/ArtPairer/venv/Assets/Dante and Virgil in Hell.PPM"))
        agr_list = list([destruction, dante_and_virgil_in_hell])

        piece_dict = dict([('Aggressive', agr_list)])

        return piece_dict


# Run application2
root = Tk()
app = App(root)
root.state('zoomed')

# Create list of albums
album_directory = App.create_album_dict()
piece_directory = App.create_piece_dict()

root.mainloop()
