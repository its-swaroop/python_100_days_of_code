# 📘 Day 2 Study Notes – Data Types, Numbers & Tip Calculator

## 1. Data Types in Python

* **String (`str`)**: Text enclosed in quotes → `"hello"`, `"123"`.

  * Characters can be accessed by index → `"hello"[0]` → `"h"`.
  * Negative indices count from the end → `"hello"[-1]` → `"o"`.
  * `"123" + "345"` → `"123345"` (concatenation, not math).

* **Integer (`int`)**: Whole numbers → `123`, `-7`, `0`.

  * Can include underscores for readability → `1_000_000`.

* **Float (`float`)**: Numbers with decimals → `3.14`, `-0.5`.

* **Boolean (`bool`)**: `True` / `False`.

  * Used for conditions and logic.

---

## 2. Functions & Data Types

* Functions expect certain types of inputs.
  Example: `len("hello")` → `5`, but `len(123)` → **TypeError**.

* Use `type()` to check data type:

  ```python
  print(type("hello"))  # <class 'str'>
  print(type(123))      # <class 'int'>
  print(type(3.14))     # <class 'float'>
  print(type(True))     # <class 'bool'>
  ```

---

## 3. Type Conversion (Casting)

* Convert between types:

  ```python
  int("123")    # 123
  float("3.14") # 3.14
  str(123)      # "123"
  bool(0)       # False
  ```

⚠️ Some conversions fail → `int("abc")` → **ValueError**.

---

## 4. Mathematical Operators

* `+` (add), `-` (subtract), `*` (multiply), `/` (divide → always float).
* `//` → floor division (drops decimals).
* `%` → modulo (remainder).
* `**` → exponentiation (power).

### Operator Precedence (PEMDAS):

1. Parentheses `( )`
2. Exponents `**`
3. Multiplication / Division `*`, `/`, `//`, `%`
4. Addition / Subtraction `+`, `-`
   ➡️ Left-to-right if same level.

Example:

```python
print(3 * 3 + 3 / 3 - 3)  # → 7.0
```

---

## 5. Rounding & Assignment Operators

* **Rounding numbers**:

  ```python
  round(8/3)       # 3
  round(8/3, 2)    # 2.67
  ```

* **Flooring (remove decimals)**:

  ```python
  int(8/3)  # 2
  ```

* **Shorthand operators**:

  ```python
  score = 0
  score += 1  # 1
  score -= 1  # -1
  score *= 2  # multiply
  score /= 2  # divide
  ```

---

## 6. f-Strings

Easier way to mix text + variables.

```python
score = 10
height = 1.8
is_winning = True
print(f"Score: {score}, Height: {height}, Winning: {is_winning}")
```

➡️ No need for `str()` conversions.

---

## 7. 🛠️ Project – Tip Calculator

### Goal:

Split a bill + tip fairly among friends.

**Steps:**

1. Ask user for inputs:

   * Total bill (float)
   * Tip % (int)
   * Number of people (int)
2. Convert values to correct data types.
3. Calculate:

   ```python
   tip_as_percent = tip / 100
   total_bill = bill * (1 + tip_as_percent)
   bill_per_person = total_bill / people
   final_amount = round(bill_per_person, 2)
   ```
4. Print result with f-string:

   ```python
   print(f"Each person should pay: ${final_amount}")
   ```

✅ Example:

```
Bill: 124.56
Tip: 12
People: 7
→ Each person should pay: $19.93
```

---

## 8. Key Takeaways

* Strings, Integers, Floats, Booleans = **primitive data types**.
* Use `type()` to check, and casting (`int()`, `str()`, etc.) to convert.
* Division → `/` float, `//` floor.
* Always remember PEMDAS for calculations.
* Use `round()` to control decimals (useful for money).
* f-strings = best way to mix variables with text.
* Project applied all concepts into a **practical program**.

---

## 🎯 Quick Self-Check

1. What’s the output?

   ```python
   print("123" + "456")
   ```
2. What’s the difference between `/` and `//`?
3. How do you check if a variable `x` is a float?
4. Write one line to round `3.14159` to 2 decimal places.
5. Modify this to fix the error:

   ```python
   name = input("Name: ")
   print("Your name has " + len(name) + " letters")
   ```

---

See you next tume!
