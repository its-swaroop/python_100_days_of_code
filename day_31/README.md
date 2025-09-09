# Flashcard Capstone Project – Step-by-Step Notes


## **Step 1 – UI Setup**

### ✨ Cues / Questions

* How do we display flashcards with both images and text?
* Why use a `Canvas` instead of Labels?
* How to center widgets cleanly with `grid()`?

---

### 📝 Notes

* `Canvas` allows layering **images + text** → perfect for flashcards.
* Front card → shows **French word**.
* Back card → shows **English translation**.
* Layout:

  ```
  [ Flashcard ]
  [ Wrong Button ] [ Right Button ]
  ```

---

### 💻 Code

```python
from tkinter import *

BACKGROUND_COLOR = "#B1DDC6"

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Flashcard App")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

# Canvas for Card
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_front = PhotoImage(file="images/card_front.png")
card_back = PhotoImage(file="images/card_back.png")
card_image = canvas.create_image(400, 263, image=card_front)
card_title = canvas.create_text(400, 150, text="", font=("Arial", 40, "italic"))
card_word = canvas.create_text(400, 263, text="", font=("Arial", 60, "bold"))
canvas.grid(row=0, column=0, columnspan=2)

# Buttons
wrong_img = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong_img, highlightthickness=0)
wrong_button.grid(row=1, column=0)

right_img = PhotoImage(file="images/right.png")
right_button = Button(image=right_img, highlightthickness=0)
right_button.grid(row=1, column=1)

window.mainloop()
```

**Test:**
Run now → you should see the blank flashcard and buttons.

---

## **Step 2 – Load Data with Pandas**

### ✨ Cues / Questions

* Why use `pandas` to handle word lists?
* How do we randomly pick a word to display?

---

### 📝 Notes

* **Data Source**: `french_words.csv` → French & English words.
* Convert CSV → list of dictionaries using `.to_dict(orient="records")`.
* Randomly select one entry to display on each new card.

---

### 💻 Code

```python
import pandas as pd
import random

data = pd.read_csv("data/french_words.csv")
to_learn = data.to_dict(orient="records")

current_card = {}

def next_card():
    global current_card
    current_card = random.choice(to_learn)
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=current_card["French"], fill="black")
    canvas.itemconfig(card_image, image=card_front)

next_card()
```

**Test:**
Manually call `next_card()` in code → a French word should appear on the card.

---

## **Step 3 – Auto Flip Card (Timer Logic)**

### ✨ Cues / Questions

* How to auto-flip the card after 3 seconds?
* Why use `after_cancel()`?

---

### 📝 Notes

* `after(ms, func)` → schedules a function after given milliseconds.
* `after_cancel(id)` → stops previously scheduled flips → **prevents stacking multiple flips**.
* Flow:

  ```
  Show French word → wait 3 seconds → flip to English automatically
  ```

---

### 💻 Code

```python
flip_timer = window.after(3000, func=lambda: None)  # placeholder timer

def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)  # cancel previous timer
    current_card = random.choice(to_learn)
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=current_card["French"], fill="black")
    canvas.itemconfig(card_image, image=card_front)
    flip_timer = window.after(3000, func=flip_card)

def flip_card():
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")
    canvas.itemconfig(card_image, image=card_back)
```

**Connect Button:**

```python
wrong_button.config(command=next_card)
```

**Test:**
Each click on the **wrong button** shows a new French word → flips automatically to English after 3 seconds.

---

## **Step 4 – Save Progress (Persistent Learning)**

### ✨ Cues / Questions

* How to save learned words between sessions?
* Why wrap file reading in `try/except`?

---

### 📝 Notes

* When a user clicks the **right button**, remove that word from `to_learn`.
* Save remaining words to `words_to_learn.csv`.
* On restart:

  * Try to load `words_to_learn.csv`.
  * If missing, fall back to `french_words.csv`.

---

### 💻 Code

```python
try:
    data = pd.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pd.read_csv("data/french_words.csv")
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")

def is_known():
    to_learn.remove(current_card)
    df = pd.DataFrame(to_learn)
    df.to_csv("data/words_to_learn.csv", index=False)
    next_card()

right_button.config(command=is_known)
```

---

## **Workflow Diagram**

```
[Start App]
   ↓
Load words_to_learn.csv
   ↓ If missing
Load french_words.csv
   ↓
Display random French word
   ↓
Timer flips to English after 3 sec
   ↓
User clicks:
   - Wrong → Next card
   - Right → Remove word → Save updated list
```

---

## **Step 5 – Final Checks**

* Verify `words_to_learn.csv` updates correctly when clicking "Right".
* Restart app → app should now use the reduced list.
* Check timer cancels cleanly when moving to next card.

---

## **Key Takeaways**

* **Pandas** simplifies data loading and saving.
* `after()` and `after_cancel()` manage precise timed events.
* Persistent progress ensures long-term learning.
* App combines **UI**, **logic**, and **file handling** seamlessly.

---

See you next time!
