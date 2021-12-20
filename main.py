from tkinter import *
import pandas

BACKGROUND_COLOR = "#B1DDC6"
FONT_LABEL = ("Ariel", 40, "italic")
FONT_WORD = ("Ariel", 60, "bold")


# ---------------------------- DATA MGMT ----------------------------------------- #
data = pandas.read_csv("data/french_words.csv")
question_row = pandas.DataFrame()
# data = pandas.read_csv("data/french_words.csv").to_dict(orient="records")


def word_setup():
    global question_row, flip_timer
    window.after_cancel(flip_timer)
    question_word = question_row["French"].item()
    canvas.itemconfig(question_label, text="French", fill="black")
    canvas.itemconfig(canvas_image, image=image_card_front)
    # random_word = random.choice(data)["French"]
    canvas.itemconfig(question_word_placeholder, text=question_word, fill="black")
    flip_timer = window.after(3000, func=flip_card)


# ---------------------------- FLIP CARD ----------------------------------------- #
def flip_card():
    canvas.itemconfig(canvas_image, image=image_card_back)
    canvas.itemconfig(question_label, text="English", fill="white")
    global question_row
    question_translation = question_row["English"].item()
    canvas.itemconfig(question_word_placeholder, text=question_translation, fill="white")


# ---------------------------- UI SETUP ----------------------------------------- #
window = Tk()
window.title("Flash card translation")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
flip_timer = window.after(3000, func=flip_card)

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
image_card_front = PhotoImage(file="images/card_front.png")
image_card_back = PhotoImage(file="images/card_back.gif")
canvas_image = canvas.create_image(400, 263, image="")
question_label = canvas.create_text(400, 150, text="", font=FONT_LABEL)
canvas.grid(row=0, column=0, columnspan=2)

question_word_placeholder = canvas.create_text(400, 263, text="", font=FONT_WORD)
word_setup()

# Button right
image_right = PhotoImage(file="images/right.png")
button_right = Button(image=image_right, highlightthickness=0, command=word_setup)
button_right.grid(row=1, column=0)

# Button wrong
image_wrong = PhotoImage(file="images/wrong.png")
button_wrong = Button(image=image_wrong, highlightthickness=0, command=word_setup)
button_wrong.grid(row=1, column=1)

window.mainloop()
