from tkinter import *
from textblob import TextBlob

# Load dataset of correct words and their wrong counterparts
with open("C:/Users/user/desktop/aspell.csv") as file:
    dataset = {}
    for line in file:
        correct_word, wrong_word = line.strip().split(":")
        dataset[correct_word.strip()] = wrong_word.strip()

def check_spelling():
    input_text = spell_check.get()
    a = TextBlob(input_text)
    corrected_text = str(a.correct())

      # Check if the corrected text exists in the dataset
    if corrected_text.lower() in map(str.lower, dataset):
        correction = dataset[corrected_text.lower()]
    else:
        correction = "Not found in dataset"

    spell = Label(window, text="The correction is:", font=("Arial", 25, "bold"), bg="gray")
    spell.pack()
    correct_text = Label(window, text=correction, font=("Arial", 15, "bold"), bg="blue")
    correct_text.pack()


window = Tk()
window.title("Spelling Checker")
window.geometry("1500x800")
window.config(background="yellow")

text_heading = Label(window, text="Spelling Checker", font=("Arial", 50, "bold"), bg="black", fg="lightpink")
text_heading.pack()

text_check = Label(window, text="Enter your text or word", font=("Arial", 30, "bold"), bg="black", fg="pink")
text_check.pack()

spell_check = Entry(window, font=("Arial", 20, "bold"), bg="orange", width=200)
spell_check.pack()

check_button = Button(window, text="Check!", font=("Arial", 30, "bold"), bg="orange", fg="white", command=check_spelling)
check_button.pack()

not_found_text = Label(window, text="", font=("Arial", 15, "bold"), bg="red")
not_found_text.pack()

window.mainloop()