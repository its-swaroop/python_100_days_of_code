# Study Notes – *How to Think Like a Programmer (Hangman Project)*

---

## 1. The Goal Is Logic, Not Code

When approaching a problem like Hangman, don’t start by typing — start by **thinking about flow**.
Programming is just a structured way to express your thought process.
If you can explain it clearly, you can code it clearly.

Before you touch the keyboard, ask:

* What is the *sequence of events*?
* What decisions must the program make?
* What information do I need to keep track of?

Thinking first prevents you from writing confusing or redundant code later.

---

## 2. Breaking Down the Problem

**Step 1: Visualize the game.**
Someone thinks of a word. The player guesses letters. Each wrong guess costs a “life.”
So, the logical structure is:

1. Choose a word.
2. Show blanks for each letter.
3. Loop until word is guessed or lives run out.

When you think this way, you’re not coding — you’re writing *mental pseudocode*.

---

## 3. Representing Information

Once the logic is clear, the next thought is: **how do I represent this in Python?**

* The *word to guess* → a string (like `"elephant"`).
* The *player’s progress* → a list of underscores `['_', '_', '_', ...]`.
* The *lives* → an integer.
* The *guessed letters* → either printed or stored to avoid repetition.

You’re modeling reality with variables.
Good programmers focus on *data representation* before they worry about syntax.

---

## 4. The Thinking Loop

The core of Hangman is a **loop that reacts to input**.

Think step-by-step:

1. Get a guess from the user.
2. Check if that guess is in the word.
3. If yes → reveal that letter’s position.
4. If no → subtract a life.
5. If all letters are revealed → game over (win).
6. If lives = 0 → game over (lose).

This is where many beginners rush into code — but the true insight is realizing:

> A loop is just repeated decision-making.

You’re automating the human thought process of “try → check → adjust.”

---

## 5. How to Think About Errors

Don’t panic when code doesn’t work.
Instead, ask:

* *What exactly did I expect to happen?*
* *What actually happened?*
* *What information does Python’s error message give me?*

Debugging is not failure — it’s feedback.
Each error refines your understanding of how the program *really* behaves.

This mindset is key: **programming = hypothesis testing**.
Every run of your code is an experiment.

---

## 6. Gradual Construction

Notice how the project builds step-by-step:

1. Start with printing blanks.
2. Add input handling.
3. Add life system.
4. Add ASCII art.

Each layer makes the game more complete, not by rewriting, but by **building on working logic**.
This modular mindset helps you debug smaller chunks instead of an entire program at once.

---

## 7. Independence From Syntax

Good programmers think in patterns, not syntax.
For example:

* “I need to repeat this” → loop.
* “I need to choose between outcomes” → condition.
* “I need to store several things” → list or dictionary.

When you think like that, Python becomes just a *language* to express your ideas.

---

## 8. The Takeaway Mental Model

To think like a programmer:

1. **Visualize the flow** before coding.
2. **Model the data** clearly.
3. **Plan the decisions** your program will make.
4. **Iterate and refine** logically.
5. **Embrace feedback** from errors.
6. **Add complexity gradually.**

That’s the core mindset that scales beyond Hangman — it applies to *every* project you’ll write.

---

## 9. The Code (for Reference)

Once your reasoning is sound, this is what the actual code ends up looking like — the “translation” of your thinking:

```python
import random
from hangman_words import word_list
from hangman_art import logo, stages

print(logo)
chosen_word = random.choice(word_list)
word_length = len(chosen_word)
end_of_game = False
lives = 6

display = ["_" for _ in range(word_length)]

while not end_of_game:
    guess = input("Guess a letter: ").lower()

    if guess in display:
        print(f"You've already guessed {guess}")

    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter

    if guess not in chosen_word:
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose.")

    print(f"{' '.join(display)}")

    if "_" not in display:
        end_of_game = True
        print("You win.")

    print(stages[lives])
```

---

Happy coding!
