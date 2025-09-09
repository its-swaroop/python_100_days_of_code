# **Flashcard Capstone Project – Final Code**

```python
# ---------------------------- FLASHCARD CAPSTONE PROJECT ---------------------------- #
from tkinter import *
import pandas as pd
import random

# ---------------------------- CONSTANTS ------------------------------- #
BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
flip_timer = None

# ---------------------------- DATA HANDLING ---------------------------- #
# Load existing progress if available, else fallback to original dataset
try:
    data = pd.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pd.read_csv("data/french_words.csv")
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")


# ---------------------------- FUNCTIONS ------------------------------- #
def next_card():
    """Display the next random French word and set up timer for auto-flip"""
    global current_card, flip_timer
    window.after_cancel(flip_timer)  # cancel previous timer to prevent stacking
    current_card = random.choice(to_learn)
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=current_card["French"], fill="black")
    canvas.itemconfig(card_image, image=card_front)
    flip_timer = window.after(3000, func=flip_card)  # flip card after 3 sec


def flip_card():
    """Flip the current card to show the English translation"""
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")
    canvas.itemconfig(card_image, image=card_back)


def is_known():
    """
    Remove the current card from the learning list,
    save updated progress, and move to the next card.
    """
    to_learn.remove(current_card)
    pd.DataFrame(to_learn).to_csv("data/words_to_learn.csv", index=False)
    next_card()


# ---------------------------- UI SETUP -------------------------------- #
window = Tk()
window.title("Flashcard App")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

# Initialize first timer
flip_timer = window.after(3000, func=flip_card)

# Canvas for flashcards
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_front = PhotoImage(file="images/card_front.png")
card_back = PhotoImage(file="images/card_back.png")
card_image = canvas.create_image(400, 263, image=card_front)
card_title = canvas.create_text(400, 150, text="", font=("Arial", 40, "italic"))
card_word = canvas.create_text(400, 263, text="", font=("Arial", 60, "bold"))
canvas.grid(row=0, column=0, columnspan=2)

# Buttons
wrong_img = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong_img, highlightthickness=0, command=next_card)
wrong_button.grid(row=1, column=0)

right_img = PhotoImage(file="images/right.png")
right_button = Button(image=right_img, highlightthickness=0, command=is_known)
right_button.grid(row=1, column=1)

# Start the app
next_card()  # show first card
window.mainloop()
```

---

## **Folder Structure**

Make sure your project folder looks like this:

```
flashcard_project/
│
├── main.py
├── data/
│   └── french_words.csv
│
└── images/
    ├── card_front.png
    ├── card_back.png
    ├── right.png
    └── wrong.png
```

---

## **How It Works**

1. **Start App**

   * Loads saved `words_to_learn.csv` if available.
   * If not, loads `french_words.csv` as default.

2. **Next Card**

   * Displays random French word.
   * Starts a 3-second timer → flips card to English automatically.

3. **Mark Known**

   * Clicking the **right button** removes the word from `to_learn`.
   * Updates `words_to_learn.csv` to persist progress.

4. **Restart Later**

   * App resumes from the last saved progress automatically.

---

## **Testing Tips**

* Run once → check French word displays and flips to English.
* Click **right button** → verify that `words_to_learn.csv` is created and updated.
* Restart app → it should now use reduced list from saved file.
* Test **wrong button** → should move to next random card without saving progress.

---

Happy Coding!
