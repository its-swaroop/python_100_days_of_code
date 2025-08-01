# 📘 Study Notes – Day 17/100

🔤 Topic: **Object-Oriented Programming (OOP) – Classes, Objects, and a Quiz Game in Python**

---

### 🎯 What I Built:

A fully functional **True/False quiz game** built using **custom Python classes**, with proper logic, state tracking, and scorekeeping.

---

### 🧱 Key Concepts Learned

#### 🔹 1. Creating a Custom Class

* Use the `class` keyword

```python
class User:
    pass
```

* Use **PascalCase** for class names (`UserAccount`, not `user_account`)

#### 🔹 2. Creating Objects

* Instantiate with `user_1 = User()`

#### 🔹 3. Attributes

* Attributes are variables **attached to objects**
* Can be added like `user_1.id = "001"` but not scalable

---

### 🧠 Constructors and Initialization

#### 🔸 `__init__` Method

* Special method triggered when an object is created
* Sets initial attribute values

```python
class User:
    def __init__(self, user_id, username):
        self.id = user_id
        self.username = username
        self.followers = 0
        self.following = 0
```

#### 🔸 Default Attribute Values

* Can assign static defaults (e.g., `self.followers = 0`) without needing input every time

---

### 🔧 Object Methods

#### 🔸 Methods vs Functions

* Methods are functions **within a class** and act on object data

```python
def follow(self, user):
    user.followers += 1
    self.following += 1
```

---

### 🧩 Building the Quiz Game

#### 🔸 Step 1: Question Model

* A class that represents individual quiz questions

```python
class Question:
    def __init__(self, q_text, q_answer):
        self.text = q_text
        self.answer = q_answer
```

#### 🔸 Step 2: Question Bank

* List of `Question` objects generated from a dictionary list in `data.py`

---

### 🧠 QuizBrain Class – Core Logic Engine

#### Attributes:

* `question_number` → tracks current question index
* `question_list` → list of `Question` objects
* `score` → current user score

#### Methods:

```python
def next_question(self):
    # shows the question and gets user's answer
```

```python
def still_has_questions(self):
    return self.question_number < len(self.question_list)
```

```python
def check_answer(self, user_answer, correct_answer):
    # compares answers and updates score
```

---

### 🔁 Looping Through the Quiz

```python
while quiz.still_has_questions():
    quiz.next_question()
```

At the end:

```python
print("You've completed the quiz!")
print(f"Your final score is: {quiz.score}/{quiz.question_number}")
```

---

### 🌐 Bonus: Using Open Trivia Database

* Swapped out static data with live JSON from OpenTDB
* Adjusted keys (`question` and `correct_answer`) in parsing logic
* Reinforced the **power of modularity** – `QuizBrain` didn't need to change

---

### 🚀 Takeaways That Add Value to Others

* **OOP gives structure to code**, making it scalable, readable, and reusable
* Good class design separates **data, behavior, and interface**
* With OOP, you can swap data sources, adjust logic, or build features **without breaking everything**
* Start with `__init__`, add attributes, and then **grow complexity with methods**
* The clearer your object responsibilities, the better your codebase scales

---
# POST
---
# 📌 **LinkedIn Post – Day 17/100**

> **Day 17 of #100DaysOfCode: Building with Classes, Not Just Code**
>
> Today I built a quiz game from scratch in Python using Object-Oriented Programming.
>
> But the real value wasn’t in the game—it was in learning how to design systems that scale:
>
> * Used `__init__()` to build clean, consistent objects
> * Separated behavior into clear methods like `next_question()` and `check_answer()`
> * Created a modular design where logic didn’t break when the data source changed
>
> The result? I can now swap out quiz questions from a local file, API, or any external source—without touching the quiz engine.
>
> That’s the power of good class design.
>
> If you're just starting with OOP, focus less on syntax and more on responsibility. Ask:
> → What does this object know?
> → What can it do?
>
> The more you model real-world thinking, the more natural OOP becomes.
>
> \#Python #SoftwareEngineering #ObjectOrientedProgramming #BuildInPublic #StudyInPublic

---

### 📌 **X (Twitter) Post – Short Version**

> Day 17/100: Built a quiz game using Python classes.
>
> Learned how `__init__`, method design, and modular thinking make systems maintainable.
>
> Real win: I can now swap quiz data sources without touching the logic.
>
> Code is craft. Class design matters.
>
> \#100DaysOfCode #Python #DevTips #OOP

---

TO BE CONT...
