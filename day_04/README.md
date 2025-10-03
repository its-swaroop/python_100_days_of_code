# Day 4 Study Notes – Randomisation & Python Lists

## 1. Randomisation in Python

* Computers are **deterministic** → they don’t naturally generate true randomness.
* Python provides **pseudo-randomness** via the `random` module.

### Importing Random

```python
import random
```

### Random Integers

```python
random_integer = random.randint(1, 10)  # inclusive of both ends
print(random_integer)
```

### Random Floats

* `random.random()` → returns float between `0.0` and `1.0` (exclusive).

```python
random_float = random.random()
print(random_float)
```

* Can scale floats:

```python
random_float = random.random() * 5   # between 0.0 and 5.0
```

---

## 2. Understanding Lists

* **List** = collection of items in square brackets `[]`.
* Example:

```python
fruits = ["apple", "banana", "cherry"]
```

* Items are ordered and accessible by **index**:

  * `fruits[0]` → `"apple"`
  * `fruits[-1]` → `"cherry"`

### Modifying Lists

```python
fruits[1] = "mango"
print(fruits)  # ['apple', 'mango', 'cherry']
```

### Adding to Lists

```python
fruits.append("orange")
fruits.extend(["grape", "kiwi"])
```

---

## 3. Nested Lists

* Lists can contain other lists:

```python
dirty_dozen = ["apple", "grapes", "cherry", ["spinach", "kale", "tomato"]]
print(dirty_dozen[3][1])  # "kale"
```

---

## 4. Random Choice from List

* Use `random.choice(list)` to pick a random element.

```python
names = ["Angela", "Ben", "Jenny", "Michael", "Chloe"]
print(random.choice(names))
```

---

## 5. Project: Rock-Paper-Scissors Game

### Steps:

1. Store ASCII art for rock, paper, scissors in a list.
2. Ask player for choice (0 = Rock, 1 = Paper, 2 = Scissors).
3. Generate computer choice with `random.randint(0, 2)`.
4. Compare and decide winner with conditions.

### Example Structure:

```python
import random
rock = """
_______
---' ____)
(_____)
(_____)
(____)
---.__(___)
"""


paper = """
_______
---' ____)____
______)
_______)
_______)
---.__________)
"""


scissors = """
_______
---' ____)____
______)
__________)
(____)
---.__(___)
"""

choices = ["Rock", "Paper", "Scissors"]

user_choice = int(input("Type 0 for Rock, 1 for Paper, 2 for Scissors: "))
computer_choice = random.randint(0, 2)

print(f"You chose {choices[user_choice]}")
print(f"Computer chose {choices[computer_choice]}")

if user_choice == computer_choice:
    print("It's a draw!")
elif user_choice == 0 and computer_choice == 2:
    print("You win!")
elif computer_choice == 0 and user_choice == 2:
    print("You lose!")
elif user_choice > computer_choice:
    print("You win!")
else:
    print("You lose!")
```

---

## 6. Key Takeaways

* Use the `random` module for pseudo-random numbers.
* Lists = ordered collections, mutable, and index-based.
* Nested lists allow structured grouping.
* `random.choice()` helps in games and simulations.
* Combining **randomness + lists + conditionals** enables interactive projects.

---

## Quick Self-Check

1. What does `random.randint(1, 5)` return?
2. How do you add `"pear"` to this list:

   ```python
   fruits = ["apple", "banana"]
   ```
3. What’s the difference between `random.random()` and `random.randint()`?
4. How do you access `"tomato"` in:

   ```python
   dirty_dozen = ["apple", "grapes", "cherry", ["spinach", "kale", "tomato"]]
   ```
5. In Rock-Paper-Scissors, why does `elif user_choice == 0 and computer_choice == 2` result in a win for the user?

---

See you next time!.
