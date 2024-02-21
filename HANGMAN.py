from tkinter import *
import random
import time
import os


cwd = os.getcwd()

class wordBank:
    tutorial = ["Bacon", "Hello", "Hi"]
    easy = ["Arm", "Burn", "Bad", "Comb", "Dull", "Energy", "Fail", "Fill", "Great", "Good", "Hard", "Easy", "Igloo", "Jump", "Joy", "Lake", "Rewind", "Wind", "Water", "Volcano"]
    medium = ["Airplane", "Burning", "Climber", "Counter", "Counting", "Abascus", "Disco", "Electric", "Elasticity", "Frankenfuter", "Exercise", "Question", "Query", "Mountain", "Mountaineer"]
    hard = ["Miniscule", "Accommodate", "Acquiesce", "Fuchsia", "Gibberish", "Nauseous", "Conscientious", "Indict", "Liaison", "Sacrilege", "Bologna", "Baloney", "Weird", "Pharaoh", "Wednesday"]
    insane = ["Necessary", "Narcissistic", "Occasion", "Fjord", "Vacuum", "Accessory", "Broccoli", "Zucchini", "Spaghetti", "Bourbon", "Entrepreneur", "Connecticut", "Massachusetts", "Epitome", "Asthma"]
    extreme = ["Bourbon", "Phlegm", "Paradigm", "Pneumonia", "Acquiesce", "Cavalcade", "Martyr", "Olfactory", "Gruesome", "Spasmodic", "Stringent", "Euphemism", "Facetious", "Hyperbole", "Didatic", "Anonymous"]
    impossible = ["Loadicean", "Logorrhea", "Laodicean", "Autochthonous", "Euonym", "Elucubrate", "Smaragdine", "Eudaemonic", "Odontalgia", "Vivisepulture"]

#Word Class
class hiddenWord(wordBank):
    word = "Placeholder"
    
    def __init__(self, difficulty):
        if difficulty == "tutorial":
            self.word = random.choice(self.tutorial)
        elif difficulty == "easy":
            self.word = random.choice(self.easy)
        elif difficulty == "medium":
            self.word = random.choice(self.medium)
        elif difficulty == "hard":
            self.word = random.choice(self.hard)
        elif difficulty == "insane":
            self.word = random.choice(self.insane)
        elif difficulty == "extreme":
            self.word = random.choice(self.extreme)
        elif difficulty == "impossible":
            self.word = random.choice(self.impossible)
    
    def format(self):
        self.word = self.word.lower()

#HANGMAN MAIN MENU
def MAIN_MENU():
    
    HULL.place(x=0, y=0)
    HULL2.place_forget()
    
    Hangman_TITLE["text"] = "HANGMAN"
    Hangman_TITLE.place(x=25,y=25)

    TUTORIAL.place(x=60,y=400)
    HULL.create_image(125,225, anchor=NW, image=TUTORIALIMG)

    EASY.place(x=440,y=400)
    HULL.create_image(444,225, anchor=NW, image=EASYIMG)

    MEDIUM.place(x=690,y=400)
    HULL.create_image(740,225, anchor=NW, image=MEDIUMIMG)

    HARD.place(x=1040,y=400)
    HULL.create_image(1050,225, anchor=NW, image=HARDIMG)

    RETURN.place_forget()
    
    INSANE.place(x=1310,y=400)
    HULL.create_image(1340,225, anchor=NW, image=INSANEIMG)

    EXTREME.place(x=60,y=800)
    HULL.create_image(110,600, anchor=NW, image=EXTREMEIMG)

    IMPOSSIBLE.place(x=440,y=800)
    HULL.create_image(500,600, anchor=NW, image=IMPOSSIBLEIMG)

    Hangman_AUTHORS.place(x=85,y=160)

    global stage
    stage = 0

    global BAD_LETTERS
    BAD_LETTERS = []

    BAD_BANK["text"] = ""
    
    Hangman_EXIT.place(x=1550,y=952)
    
    WORDS.place_forget()
    BAD_BANK.place_forget()

    keys = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","space"]
    for i in keys:
        Hangman_WINDOW.unbind(f"<{i}>")
#Close Out Function
def close():
    Hangman_WINDOW.destroy()

revealed = []

def keypress_check(event):
    string = ""
    characters_right = []
    if event.keysym in CORRECT_WORD:
        global revealed
        revealed += event.keysym
        for i in CORRECT_WORD:
            if i in revealed:
                string += i + " "
            else:
                string += "_ "
        
        global pos2
        pos2 = 0
        
        for i in CORRECT_WORD:
            if i in revealed and i in CORRECT_WORD2:
                print("FOUND ", i)
                pos2 = 0
                for i in CORRECT_WORD2:
                    if i in revealed and i in CORRECT_WORD2:
                        del CORRECT_WORD2[pos2]
                        pos2 = 0
                    elif pos2 > len(CORRECT_WORD2) == 1:
                        pos2 = 0
                    else:
                        pos2 += 1
                print(CORRECT_WORD2)
                print(pos2)
            else:
                pos2 += 1
        
        if len(CORRECT_WORD2) == 0:
            MAIN_MENU()
            global STAGE
            global STAGEIMG
            STAGE = 0
            STAGEIMG = PhotoImage(file = cwd + f"\\{STAGE}.png").subsample(1, 1)
            Hangman_TITLE["font"] = ("Rockwell Extra Bold", 44)
            Hangman_TITLE["text"] = "YOU WIN! THE WORD WAS " + CORRECT_WORD.upper() + "!"
        else:
            WORDS["text"] = string
    else:
        global BAD_LETTERS

        STAGE += 1

        STAGEIMG['file'] = cwd + f"\\{STAGE}.png"

        if STAGE >= 6:
            MAIN_MENU()
            STAGE = 0
            STAGEIMG = PhotoImage(file = cwd + f"\\{STAGE}.png").subsample(1, 1)
            Hangman_TITLE["font"] = ("Rockwell", 44)
            Hangman_TITLE["text"] = "YOU LOSE! THE WORD WAS " + CORRECT_WORD.upper() + "!"
        else:
            if event.keysym not in BAD_LETTERS:
                BAD_LETTERS.append(event.keysym)
            string = ""
            for i in BAD_LETTERS:
                string += i + ", "
            BAD_BANK["text"] = string
        
def difficulty_set(button):
    global STAGE
    STAGE = 0

    global STAGEIMG
    STAGEIMG = PhotoImage(file = cwd + f"\\{STAGE}.png").subsample(1, 1)

    global revealed
    revealed = []

    global BAD_BANK
    BAD_BANK["text"] = ""

    button.lower()

    HULL2.place(x=900, y=150)
    
    global HANGMAN_KEY
    
    HANGMAN_KEY = hiddenWord(button)

    HANGMAN_KEY.format()

    STAGEIMG.borderwidth=0
    
    Hangman_TITLE["text"] = button.upper()

    HULL.place_forget()
    TUTORIAL.place_forget()
    EASY.place_forget()
    MEDIUM.place_forget()
    HARD.place_forget()
    INSANE.place_forget()
    EXTREME.place_forget()
    IMPOSSIBLE.place_forget()

    HANGMAN_KEY = hiddenWord(button)

    HANGMAN_KEY.format()

    HULL2.create_image(-160,0, anchor=NW, image=STAGEIMG)
    
    RETURN.place(x=1600,y=700)
    WORDS.place(x=200,y=350)
    BAD_BANK.place(x=100,y=930)

    keys = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","space"]

    for i in keys:
        Hangman_WINDOW.bind(f"<{i}>", keypress_check)
    
    global string
    string = ""

    global CORRECT_WORD
    CORRECT_WORD = HANGMAN_KEY.word

    global CORRECT_WORD2
    CORRECT_WORD2 = list(CORRECT_WORD)
    
    for i in CORRECT_WORD:
        string += "_ "

    WORDS["text"] = string
    
global Hangman_WINDOW
Hangman_WINDOW = Tk()
Hangman_WINDOW.title("Hangman")
Hangman_WINDOW.configure(background='orange')
Hangman_WINDOW.attributes('-fullscreen', True)
BACK = PhotoImage(file = cwd + "\MAIN PAGE.png").subsample(4, 4)

global BAD_LETTERS
BAD_LETTERS = []

RETURN = Button(Hangman_WINDOW, background="Orange", text = "", font=("Rockwell", 44), command = MAIN_MENU, image=BACK)
WORDS = Label(Hangman_WINDOW, text="PLACEHOLDER", font=("Rockwell", 44), bg='orange')
BAD_BANK = Label(Hangman_WINDOW, text="", font=("Rockwell", 44), bg='orange')

HULL = Canvas(Hangman_WINDOW, width = 1920, height = 1080, bg='orange')
HULL2 = Canvas(Hangman_WINDOW, width = 600, height = 700, bg='orange',borderwidth=-3)

HULL2.place(x=0, y=0)

Hangman_TITLE = Label(Hangman_WINDOW, text="HANGMAN", font=("Rockwell Extra Bold", 100), bg='orange')

Hangman_AUTHORS = Label(Hangman_WINDOW, text="By Erik and Colin", font=("Comic Sans MS", 25, "italic"), bg='orange')

TUTORIAL = Button(Hangman_WINDOW, background="Green", text = "TUTORIAL", font=("Rockwell", 44), command = lambda: difficulty_set(button="tutorial"))
TUTORIALIMG = PhotoImage(file = cwd + "\Tutorial.png").subsample(5, 5)

EASYIMG = PhotoImage(file = cwd + "\Easy.png").subsample(5, 5)
EASY = Button(Hangman_WINDOW, background="Blue", text = "EASY", font=("Rockwell", 44), command = lambda: difficulty_set(button="easy"))

MEDIUMIMG = PhotoImage(file = cwd + "\Medium.png").subsample(5, 5)
MEDIUM = Button(Hangman_WINDOW, background="Yellow", text = "MEDIUM", font=("Rockwell", 44), command = lambda: difficulty_set(button="medium"))

HARDIMG = PhotoImage(file = cwd + "\Hard.png").subsample(5, 5)
HARD = Button(Hangman_WINDOW, background="deep pink", text = "HARD", font=("Rockwell", 44), command = lambda: difficulty_set(button="hard"))

INSANEIMG = PhotoImage(file = cwd + "\Insane.png").subsample(5, 5)
INSANE = Button(Hangman_WINDOW, background="Red", text = "INSANE", font=("Rockwell", 44), command = lambda: difficulty_set(button="insane"))

EXTREMEIMG = PhotoImage(file = cwd + "\Extreme.png").subsample(4, 4)
EXTREME = Button(Hangman_WINDOW, background="red3", text = "EXTREME", font=("Rockwell", 44), command = lambda: difficulty_set(button="extreme"))

IMPOSSIBLEIMG = PhotoImage(file = cwd + "\Impossible.png").subsample(4, 4)
IMPOSSIBLE = Button(Hangman_WINDOW, background="maroon", text = "IMPOSSIBLE", font=("Rockwell", 44), command = lambda: difficulty_set(button="impossible"))

Hangman_EXIT = Button(Hangman_WINDOW, background="Orange Red", text = "Give Up", command = exit, font=("Rockwell Extra Bold", 50))

Hangman_WINDOW.protocol("WM_DELETE_WINDOW", close)

STAGE = 0
STAGEIMG = PhotoImage(file = cwd + f"\\{STAGE}.png").subsample(1, 1)

window_x = Hangman_WINDOW.winfo_x()
window_y = Hangman_WINDOW.winfo_y()

MAIN_MENU()

Hangman_WINDOW.mainloop()
