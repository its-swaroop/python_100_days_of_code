# 📘 Tkinter GUI – Complete Chapter Notes

## 1. Introduction

* Tkinter = Python’s built-in library for **Graphical User Interfaces (GUIs)**.
* In this chapter you’ll learn:

  * How to create windows, labels, buttons, and text input.
  * How to handle button clicks and configure widgets.
  * Advanced Python function arguments: default values, `*args`, `**kwargs`.
  * Layout management using `pack()`, `place()`, and `grid()`.
  * A final project: **Miles to Kilometers Converter**.
* GUI programs let users interact visually with windows, buttons, and text fields instead of typing into the console.

---

## 2. History of GUIs

* Before GUIs, computers were command-line only (e.g., MS-DOS).
* GUIs made computers accessible → windows, icons, mouse clicks.
* Key history:

  * **Apple Lisa**: one of the first GUI systems.
  * **Microsoft Windows**: led to legal battles with Apple over “copying.”
  * **Xerox PARC**: pioneered GUI concepts and the first mouse.
* Importance: GUIs were a revolution in usability → Tkinter allows us to build our own.

---

## 3. Getting Started with Tkinter

Tkinter is pre-installed with Python.

```python
import tkinter as tk

window = tk.Tk()                  # Create window
window.title("My First GUI")      # Title bar text
window.minsize(width=500, height=300)  # Minimum size
window.mainloop()                 # Keeps window open (event loop)
```

### Labels

```python
my_label = tk.Label(text="I am a Label", font=("Arial", 24, "bold"))
my_label.pack()   # Places it in the center by default
```

* `pack()` = simple layout manager.

  * `side="left" | "right" | "top" | "bottom"`
  * `expand=True` → widget stretches to fill space.

---

## 4. Default Arguments in Functions

* Functions can define **default values** for parameters.

```python
def greet(name="User"):
    print(f"Hello {name}")

greet()        # Hello User
greet("Alice") # Hello Alice
```

* Example: `turtle.write()` has defaults like `align="center"`, `move=False`.
* Required arguments must be supplied; optional ones fall back to defaults.
* Tkinter methods rely heavily on default arguments.

---

## 5. `*args` – Unlimited Positional Arguments

* `*args` allows functions to take any number of inputs.

```python
def add(*args):
    total = 0
    for n in args:
        total += n
    return total

print(add(3, 5, 6))  # 14
```

* Internally, `args` is a **tuple**.
* Used when the number of inputs isn’t fixed.

---

## 6. `**kwargs` – Unlimited Keyword Arguments

* `**kwargs` collects keyword arguments into a dictionary.

```python
def calculate(n, **kwargs):
    n += kwargs.get("add", 0)
    n *= kwargs.get("multiply", 1)
    return n

print(calculate(2, add=3, multiply=5))  # 25
```

* Tkinter widgets (`Label`, `Button`, `pack()`, etc.) accept many optional settings via `**kwargs`.

Example with a class:

```python
class Car:
    def __init__(self, **kwargs):
        self.make = kwargs.get("make")
        self.model = kwargs.get("model")

my_car = Car(make="Nissan", model="GT-R")
print(my_car.model)  # GT-R
```

---

## 7. Configuring Widgets

### Changing Label Text

```python
my_label["text"] = "New Text"
# OR
my_label.config(text="New Text")
```

### Buttons with Commands

```python
def button_clicked():
    my_label.config(text="Button got clicked!")

button = tk.Button(text="Click Me", command=button_clicked)
button.pack()
```

* `command` = function executed when button is clicked.
* Pass the **function name only** (no `()` after it).

---

## 8. Entry (Text Input) Widget

* Allows user to type into a text box.

```python
entry = tk.Entry(width=30)
entry.pack()

user_input = entry.get()  # Fetch typed text
```

Example with button:

```python
def button_clicked():
    my_label.config(text=entry.get())

button = tk.Button(text="Submit", command=button_clicked)
button.pack()
```

---

## 9. Layout Managers

Tkinter provides three main layout managers:

### `pack()`

* Simple stacking (top, bottom, left, right).

### `place()`

* Absolute positioning using coordinates.
* Rarely used → not responsive.

```python
my_label.place(x=100, y=200)
```

### `grid()`

* Most flexible → arranges widgets in a grid (like a table).

```python
label1 = tk.Label(text="Name")
label1.grid(row=0, column=0)

entry1 = tk.Entry()
entry1.grid(row=0, column=1)

button = tk.Button(text="Submit")
button.grid(row=1, column=0, columnspan=2)
```

⚠️ **Important**: Don’t mix `pack()` and `grid()` in the same window.

---

## 10. Project – Miles to Kilometers Converter

### Step 1: Create Window

```python
window = tk.Tk()
window.title("Mile to Km Converter")
window.config(padx=20, pady=20)  # Add padding
```

### Step 2: Add Widgets

```python
entry = tk.Entry(width=10)
entry.grid(row=0, column=1)

miles_label = tk.Label(text="Miles")
miles_label.grid(row=0, column=2)

is_equal_label = tk.Label(text="is equal to")
is_equal_label.grid(row=1, column=0)

km_result_label = tk.Label(text="0")
km_result_label.grid(row=1, column=1)

km_label = tk.Label(text="Km")
km_label.grid(row=1, column=2)
```

### Step 3: Button with Conversion Logic

```python
def miles_to_km():
    miles = float(entry.get())
    km = round(miles * 1.609)
    km_result_label.config(text=f"{km}")

button = tk.Button(text="Calculate", command=miles_to_km)
button.grid(row=2, column=1)
```

✅ Final result:

* Type a number of miles → click “Calculate” → label updates with kilometers.

---

# 🔑 Chapter Summary

* **Windows & Widgets**: create with `Tk()`, add labels, buttons, and entry fields.
* **Arguments in functions**:

  * Default arguments.
  * `*args` (tuple of inputs).
  * `**kwargs` (dictionary of key-value options).
* **Widget configuration**: update text, styling, properties dynamically.
* **Layout managers**:

  * `pack()` for simple stacking.
  * `place()` for fixed coordinates.
  * `grid()` for structured forms (best choice).
* **Event-driven programming**: GUIs respond to user input (button clicks, text entry).
* **Practice Project**: miles-to-km converter demonstrates all key concepts.

---

See you next time!
