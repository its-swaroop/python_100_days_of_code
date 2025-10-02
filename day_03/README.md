# Study Notes – Day 3 (Conditionals & Logic in Python)

## 1. Conditional Statements

* **if / else**

  * Used to make decisions in code.
  * Syntax:

    ```python
    if condition:
        # code if true
    else:
        # code if false
    ```
  * Indentation is **critical** (blocks of code must align properly).
* **elif (else if)**

  * Used for multiple conditions.
  * Only one branch executes in an `if / elif / else` chain.

---

## 2. Comparison Operators

* `>` greater than
* `<` less than
* `>=` greater or equal
* `<=` less or equal
* `==` equal to
* `!=` not equal to
* Difference: `=` assigns, `==` compares.

---

## 3. Real-World Examples

* **Bathtub overflow analogy** → conditional check (if water > 80 cm → drain, else → fill).
* **Roller coaster ticketing**

  * Height check: must be ≥ 120 cm.
  * Age-based pricing:

    * `<12` → $5
    * `12–18` → $7
    * `>18` → $12

---

## 4. Modulo Operator (%)

* Returns remainder of division.
* Example:

  * `10 % 5 = 0` (even division)
  * `10 % 3 = 1` (remainder = 1)
* **Odd/Even check**:

  * `if number % 2 == 0 → even`
  * `else → odd`.

---

## 5. Nested & Multiple Conditions

* **Nested if** → an `if` inside another `if`.
* Example: after checking height, also check age.
* **Multiple if** → independent conditions that can all be checked, not just one.

---

## 6. Updating Variables

* `+=` shortcut:

  ```python
  bill += 3  # same as bill = bill + 3
  ```

---

## 7. Logical Operators

* `and` → both conditions must be true.
* `or` → at least one condition must be true.
* `not` → reverses truth value.

Example:

```python
if age >= 45 and age <= 55:
    print("Free ride (midlife crisis special!)")
```

---

## 8. Projects & Challenges

* **Roller Coaster Pricing** (with optional $3 photo add-on).
* **Python Pizza Delivery Program**

  * Inputs: size (S/M/L), pepperoni (Y/N), cheese (Y/N).
  * Bill calculation with nested & multiple ifs.
* **Treasure Island Game (Final Project)**

  * Text-based adventure using conditionals.
  * Choices (left/right → swim/wait → doors).
  * Use `.lower()` to handle different input cases.
  * ASCII art can be added with triple quotes (`'''`).

---

## 9. Key Takeaways

* Indentation defines code blocks.
* Always use correct comparison operators.
* Break problems into flowcharts before coding.
* Combine conditions using logical operators.
* Make projects creative to reinforce learning.

---

See you next time!
