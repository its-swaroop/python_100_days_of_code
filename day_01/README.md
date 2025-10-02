# Python Day 1 Notes

## 1. Writing Your First Code

* **Why programming?** → To tell the computer what to do.
* **First command**:

  ```python
  print("Hello world!")
  ```

  * `print` → built-in function (always lowercase).
  * `()` → parentheses contain what to output.
  * `"Hello world!"` → text string, enclosed in **quotes**.
  * Output appears in the console.

Example output:

```
Hello world!
Process finished with exit code 0
```

---

## 2. Anatomy of Output

* **Top line** → file location of the executed script.
* **Middle lines** → your program’s output.
* **Final line** → exit code (0 = success).

Make sure "Current File" is selected when running in PyCharm.

---

## 3. Strings & Quotation Marks

* **Strings** = text inside quotes (`"Hello"`, `'World'`).
* Always close your quotes.
* Missing a quote → `SyntaxError`.
* Editors (PyCharm, etc.) help with **syntax highlighting**:

  * Colors show what’s string vs. code.
  * Red squiggly = error.
  * Yellow squiggly = warning (style issue, e.g., missing newline at EOF).

---

## 4. Common Errors

* **SyntaxError** → e.g., missing quotes/parentheses.
* **IndentationError** → extra/missing spaces/tabs.
* **NameError** → using an undefined/misspelled variable.

Debugging workflow:

1. Read the error message.
2. Look at the highlighted line.
3. Google the error (StackOverflow is very useful).

*Fun fact*: The term *debugging* came from an actual moth found in a computer in the 1940s.

---

## 5. Working with Strings

* **New lines**: use `\n`.

  ```python
  print("Hello\nWorld")
  ```

* **Concatenation**: use `+`.

  ```python
  print("Hello " + "Angela")
  # Output: Hello Angela
  ```

* Don’t forget spaces: `"Hello " + "Angela"`.

Python is strict about **spaces in code** (not inside strings).

---

## 6. Taking User Input

* Use `input()` to get data from the user:

  ```python
  input("What is your name? ")
  ```

* Capturing input into a variable:

  ```python
  name = input("What is your name? ")
  print("Hello " + name + "!")
  ```

* Combine functions inside each other:

  ```python
  print("Hello " + input("What is your name? ") + "!")
  ```

---

## 7. Comments in Code

* Add notes for yourself:

  ```python
  # This line prints a greeting
  print("Hello world!")
  ```

* Shortcut:

  * Mac → `Cmd + /`
  * Windows/Linux → `Ctrl + /`

---

## 8. Variables

* Store values with `=`:

  ```python
  username = input("What is your name? ")
  length = len(username)
  print(length)
  ```

* Variables **can change**:

  ```python
  x = "Jack"
  x = "Angela"
  ```

* Naming rules:

  * Use meaningful names (`user_name`, not `x`).
  * Use underscores for multi-word names.
  * Can include numbers, but not at start (`name1` is valid; `1name` is not).
  * Don’t use reserved words (e.g., `print`, `input`).

---

## 9. Good Practices

* Make variable names descriptive (`user_name`, not `n`).
* Consistency matters → typo in name leads to `NameError`.
* Readability is more important than shortness.

---

## 10. Project: Band Name Generator

**Goal** → Create a fun band name by combining two user inputs.

```python
print("Welcome to the Band Name Generator.")
city = input("Which city did you grow up in?\n")
pet = input("What is the name of your pet?\n")
print("Your band name could be " + city + " " + pet)
```

Concepts used: printing, input, variables, string concatenation, new lines (`\n`).

---

## 11. Key Takeaways

* Programming = telling computers what to do.
* **Core building blocks so far**: `print()`, `input()`, variables, strings.
* Errors are normal → learn to read & fix them.
* Use **comments** to explain new concepts in your code.
* Always aim for **readable, consistent, and bug-free code**.

---

**End of Day 1** — You’ve learned enough to build your first project.

---

See you next time!
