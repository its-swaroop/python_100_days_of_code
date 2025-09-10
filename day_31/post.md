## **LinkedIn Post – “Discussion Hook” Style**

**Main Post (short, curiosity-driven):**

> Today was a reminder that *notes don’t build apps — code does.*
>
> Day 31 of #100DaysOfCode: I turned my handwritten flashcard notes into a fully working Python app.
>
> The biggest challenge wasn’t writing new code… it was **making old code smarter**.
>
> Curious? The step-by-step journey + code breakdown is in the comments. 👇

---

**Comment #1 (value-packed, where you drop the gold):**

> **Day 31 – Flashcard Capstone Project (Python + Tkinter + Pandas)**
>
> **What I built:**
> A flashcard app to practice French → English vocabulary.
>
> * Auto-flips cards after 3 sec using `after()` and `after_cancel()`
> * Saves learned words to a CSV so you don’t repeat what you’ve mastered
> * Uses Pandas to manage data efficiently
>
> **Biggest takeaway:**
> Debugging timers taught me this:
> *“Bad code works once. Good code works every time.”*
>
> If you're curious, here’s a simplified version of the core logic:
>
> ```python
> flip_timer = window.after(3000, func=flip_card)
>
> def next_card():
>     global current_card, flip_timer
>     window.after_cancel(flip_timer)  # cancel stacked timers
>     current_card = random.choice(to_learn)
>     flip_timer = window.after(3000, func=flip_card)
> ```
>
> **Question for you:**
> What’s a project where you learned more fixing bugs than writing code?

---

## **X (Twitter) Post – Conversation Starter**

Main Tweet:

> Day 31 of #100DaysOfCode:
>
> Built a Python flashcard app — but the *real work* wasn’t coding, it was debugging timers that flipped cards at the wrong moment.
>
> Notes guide you. Debugging teaches you.
>
> What was your **biggest debugging lesson** so far?

Follow-up Reply (with snippet):

> The core challenge: preventing multiple timers from stacking.
>
> ```python
> window.after_cancel(flip_timer)  # key to clean timing
> flip_timer = window.after(3000, func=flip_card)
> ```
>
> A single line, but hours of confusion before I nailed it.
>
> Drop your “aha” bug fix moment below. 👇

---
happy coding!
