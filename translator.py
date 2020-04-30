# importing all from tkinter
from tkinter import *
# importing Translator from googletrans
from googletrans import Translator

# creating window
win = Tk()
# giving title to the window
win.title('translator')
# specifying size of our window
win.geometry('500x100')
select = ""

# creating a function to get language
def selection():
    global select
    # getting the language to be converted too
    select = str(radio.get())

# creating a function to translate user given text
def translation():
    # dictionary with keys for specific languages
    lang = {"Spanish" : "es", "English" : "en", "French" : "fr", "German" : "de"}
    # getting text from entry field
    word = entry.get()
    # creating object of Translator
    translator = Translator(service_urls =['translate.google.com'])
    # translating the text to language specified by the user
    translation1 = translator.translate(word, dest = lang[select])
    # creating label to display the translated text
    label1 = Label(win, text = f'Translated In {select} : {translation1.text}', bg = 'yellow')
    label1.grid(row = 3)

# creating entry field
entry = Entry(win)
entry.grid(row = 1, column = 1)

# creating a radio variable to get radio button response
radio = StringVar(None, "English")

# creating button to call our translator function
button = Button(win, text = 'Translate', command = translation)
button.grid(row = 1, column = 2)

# creating radio button for spanish language
R1 = Radiobutton(win, text="Spanish", variable=radio, value="Spanish", command=selection)
R1.grid(row = 2, column = 0)
R1.grid_anchor(anchor=W)

# creating radio button for french language
R2 = Radiobutton(win, text="French", variable=radio, value="French", command=selection)
R2.grid(row = 2, column = 1)
R2.grid_anchor(anchor=W)

# creating radio button for german language
R3 = Radiobutton(win, text="German", variable=radio, value="German", command=selection)
R3.grid(row = 2, column = 2)
R3.grid_anchor(anchor=W)

# creating window loop
win.mainloop()
