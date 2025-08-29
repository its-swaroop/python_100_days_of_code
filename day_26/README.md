# Day 26: <br/>List and Dictionary Comprehensions + NATO Phonetic Project

## **1. List Comprehensions**

* **Definition:** A concise way to create a new list from an existing iterable (list, string, range, tuple, etc.).
* **Syntax:**

```python
new_list = [new_item for item in iterable if condition]
```

* **Steps to create:**

  1. `iterable` → list/string/range/tuple to loop through
  2. `item` → variable representing each element
  3. `new_item` → expression or transformation for each element
  4. Optional `if condition` → filters items based on a test

* **Example 1:** Increment numbers by 1

```python
numbers = [1, 2, 3]
new_numbers = [n + 1 for n in numbers]  # [2, 3, 4]
```

* **Example 2:** Split string into letters

```python
name = "Angela"
letters_list = [letter for letter in name]  # ['A', 'n', 'g', 'e', 'l', 'a']
```

* **Example 3:** Double numbers in a range

```python
range_list = [num*2 for num in range(1, 5)]  # [2, 4, 6, 8]
```

* **Conditional Example:** Filter short names (<5 chars)

```python
names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
short_names = [name for name in names if len(name) < 5]  # ['Alex', 'Beth', 'Dave']
```

* **Conditional with transformation:** Uppercase long names (>=5 chars)

```python
long_names = [name.upper() for name in names if len(name) >= 5]  
# ['CAROLINE', 'ELEANOR', 'FREDDIE']
```

---

## **2. Dictionary Comprehensions**

* **Definition:** Create dictionaries in a concise way from iterables or other dictionaries.
* **Syntax:**

```python
new_dict = {new_key: new_value for item in iterable if condition}
```

* **Steps to create:**

  1. Use `{}` instead of `[]`
  2. Define `new_key` and `new_value`
  3. Loop through iterable (list, string, range) or `dict.items()`
  4. Optional condition

* **Example 1:** Assign random scores to students

```python
import random
students = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
students_scores = {student: random.randint(1,100) for student in students}
```

* **Example 2:** Filter dictionary based on value

```python
passed_students = {student: score for student, score in students_scores.items() if score >= 60}
```

---

## **3. Iterating over Pandas DataFrames**

* DataFrame can be treated like a dictionary:

  ```python
  for key, value in df.items():
      print(key, value)
  ```
* Looping over rows: `.iterrows()`

```python
for index, row in df.iterrows():
    print(row.student, row.score)
```

* Access specific cell: `row.column_name`

---

## **4. NATO Phonetic Alphabet Project**

**Goal:** Convert user input into phonetic alphabet codes using list & dictionary comprehension.

* **Step 1: Convert CSV into dictionary**

```python
import pandas as pd
data = pd.read_csv("nato_phonetic_alphabet.csv")
phonetic_dict = {row.letter: row.code for index, row in data.iterrows()}
```

* **Step 2: Convert user input into phonetic codes**

```python
word = input("Enter a word: ").upper()
output_list = [phonetic_dict[letter] for letter in word]
print(output_list)
```

* Output example for `"Thomas"`:
  `['Tango', 'Hotel', 'Oscar', 'Mike', 'Alpha', 'Sierra']`

---

## **5. Key Takeaways**

* List comprehensions shorten loops and make code readable.
* Dictionary comprehensions are similar, but with `{}` and key-value pairs.
* Conditional comprehensions allow filtering while creating new lists/dictionaries.
* `.iterrows()` lets you loop through DataFrame rows like dictionaries.
* Projects like the NATO phonetic tool are excellent practice for combining loops, comprehensions, and CSV/Pandas handling.

---

See you next time!
