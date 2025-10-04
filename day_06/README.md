# Day 6 Study Notes – Functions, Indentation, & While Loops

## 1. Functions: Reusable Code Blocks

### What are functions?

* Functions let you **group code** into reusable actions.
* Python already has built-ins like:

  ```python
  print("Hello")
  len("Python")
  int("5")
  range(1, 10)
  ```

  Each performs a specific job — all follow the same structure:
  **name + parentheses (with or without arguments).**

---

### Defining Your Own Function

```python
def my_function():
    print("Hello")
    print("Bye")
```

* `def` → keyword to define a function.
* `my_function` → name (lowercase, underscores).
* `()` → parentheses for arguments.
* `:` → marks the start of a code block.
* **Indentation** → all code inside must be indented.

But defining ≠ running.
You must **call** it:

```python
my_function()
```

---

### Why Functions Matter

They bundle repeated logic:
Instead of:

```python
turn_left()
turn_left()
```

You can write:

```python
def turn_around():
    turn_left()
    turn_left()

turn_around()
```

Cleaner, shorter, and easier to understand.

---

### Practice Challenge

Create your own `turn_right()` function:

```python
def turn_right():
    turn_left()
    turn_left()
    turn_left()
```

Then make the robot draw a square:

```python
move()
turn_right()
move()
turn_right()
move()
turn_right()
move()
turn_right()
```

Result → fewer lines, more readable.

---

## 2. Code Blocks & Indentation

Python uses **indentation instead of braces `{}`** to define scope.

Example:

```python
def greet():
    print("Hello")
    print("World")

print("Outside function")
```

* Only the indented lines belong to the function.
* Everything at the same indentation level is treated equally.

### Nested Indentation

Blocks can be nested inside each other:

```python
def check_weather():
    if sky == "clear":
        print("Blue sky!")
    else:
        print("Maybe stay in.")
```

Indentation = structure.

---

### Tabs vs Spaces

The eternal war.
Python’s official guide (PEP 8):

* Use **4 spaces per indent**.
* **Don’t mix** tabs and spaces in the same file.
* Most editors insert 4 spaces automatically when you hit Tab.

💡 Spaces > Tabs (and apparently, spaces-users statistically earn more 😄).

---

## 3. While Loops

### Syntax:

```python
while condition:
    # do something
```

* Keeps running **while** the condition is true.
* Stops when it becomes false.

Example:

```python
number_of_hurdles = 6
while number_of_hurdles > 0:
    jump()
    number_of_hurdles -= 1
```

Equivalent to:

```python
for step in range(6):
    jump()
```

---

### `while` vs `for`

| Feature                  | `for` loop | `while` loop |
| ------------------------ | ---------- | ------------ |
| Repeats over known range | ✅          | ❌            |
| Stops based on condition | ❌          | ✅            |
| Safer (auto stops)       | ✅          | ❌            |
| Risk of infinite loop    | Low        | High         |

Use `for` when you know **how many times** to run.
Use `while` when you don’t — e.g. until a goal is reached.

---

### Infinite Loops

```python
while 5 > 3:
    print("oops")
```

Never ends → Python keeps printing forever.
Always ensure something **changes** inside the loop that can make the condition false.

---

## 4. Hurdle Challenges 🏃‍♂️

### Hurdle 1: Basic Jump

Goal → make the robot jump six hurdles.

* Use `def jump():` to define steps.
* Then loop:

  ```python
  for step in range(6):
      jump()
  ```

Or with a while loop:

```python
number_of_hurdles = 6
while number_of_hurdles > 0:
    jump()
    number_of_hurdles -= 1
```

---

### Hurdle 2: Unknown Goal

You don’t know how many hurdles → use condition:

```python
while not at_goal():
    jump()
```

Stops automatically when the goal is reached.

---

### Hurdle 3: Random Walls

Walls appear randomly → need `if` checks.

```python
while not at_goal():
    if wall_in_front():
        jump()
    else:
        move()
```

Modified `jump()` function (no initial move):

```python
def jump():
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()
```

---

### Hurdle 4: Variable Wall Height

Walls now vary in height → dynamic logic needed:

```python
def jump():
    turn_left()
    while wall_on_right():
        move()
    turn_right()
    move()
    turn_right()
    while front_is_clear():
        move()
    turn_left()
```

→ Robot climbs up until right side is clear, then descends.

---

## 5. Final Project – Maze Solver 🧭

Goal: robot finds the exit in a **random maze**, starting from a random position and direction.

Algorithm = *Right-hand rule*:

> Always follow the right wall until you reach the goal.

### Step-by-Step Logic

```python
def turn_right():
    turn_left()
    turn_left()
    turn_left()

while not at_goal():
    if right_is_clear():
        turn_right()
        move()
    elif front_is_clear():
        move()
    else:
        turn_left()
```

Works — but can create **infinite loops** if robot starts in open space.

---

### Fixing the Infinite Loop

Before starting the main loop, make sure the robot has a wall on its right:

```python
while front_is_clear():
    move()
turn_left()
```

Then enter the main loop.
This ensures it always begins with a wall to follow, preventing the infinite spiral.

---

### Debugging Technique

* Use **step-through execution** to trace line-by-line behavior.
* Add `print()` statements to inspect logic.
* Test frequently — don’t write 50 lines before running.

---

## 6. Reflection

Learning functions and while loops is like finally teaching your robot **how to think** instead of just **what to do**.
You’re no longer writing every movement — you’re designing strategies.
The maze challenge? It’s not about code — it’s about logic.

---

## Quick Self-Check

1. What does this code print?

   ```python
   def greet():
       print("Hi")
   greet()
   ```
2. Why must code inside a function be indented?
3. When do you use a while loop instead of a for loop?
4. What’s the difference between `while at_goal()` and `while not at_goal()`?
5. How does the robot avoid infinite loops in the maze challenge?

---

✅ **End of Day 6**
Functions make code reusable.
Indentation defines structure.
While loops make your robot smart — but only if you control them.

---

See you next time!
