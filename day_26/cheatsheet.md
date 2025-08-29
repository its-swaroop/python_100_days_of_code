# Day 26 Cheat Sheet: List & Dictionary Comprehensions + Pandas

## **1. List Comprehension**

* **Syntax:**

```python
new_list = [new_item for item in iterable if condition]
```

* **Create new list from existing iterable**
* **Examples:**

```python
# Increment numbers
numbers = [1,2,3]
new_numbers = [n+1 for n in numbers]  # [2,3,4]

# Split string into letters
name = "Angela"
letters_list = [letter for letter in name]  # ['A','n','g','e','l','a']

# Double range numbers
range_list = [num*2 for num in range(1,5)]  # [2,4,6,8]

# Conditional: short names
names = ["Alex","Beth","Caroline","Dave"]
short_names = [n for n in names if len(n)<5]  # ['Alex','Beth','Dave']

# Conditional + transform: uppercase long names
long_names = [n.upper() for n in names if len(n)>=5]  # ['CAROLINE']
```

---

## **2. Dictionary Comprehension**

* **Syntax:**

```python
new_dict = {new_key: new_value for item in iterable if condition}
```

* **Create dictionary from iterable or existing dict**
* **Examples:**

```python
import random
students = ["Alex","Beth","Caroline"]
# Random scores
scores = {s: random.randint(1,100) for s in students}

# Filter dict by value
passed = {s: score for s,score in scores.items() if score>=60}
```

---

## **3. Pandas Iteration**

* Loop over columns (like dict):

```python
for col, values in df.items():
    print(col, values)
```

* Loop over rows:

```python
for idx, row in df.iterrows():
    print(row.student, row.score)
# Access a cell
row.student  # or row['student']
```

---

## **4. NATO Phonetic Alphabet Project**

1. **Create dictionary from CSV**

```python
import pandas as pd
data = pd.read_csv("nato_phonetic_alphabet.csv")
phonetic_dict = {row.letter: row.code for idx,row in data.iterrows()}
```

2. **Convert input to phonetic codes**

```python
word = input("Enter a word: ").upper()
output = [phonetic_dict[letter] for letter in word]
print(output)
```

* Example: `"Thomas"` → `['Tango','Hotel','Oscar','Mike','Alpha','Sierra']`

---

## **5. Key Tips**

* Comprehensions = concise, readable, faster than loops.
* Conditional comprehension = filter + transform in one line.
* `.iterrows()` is crucial for DataFrame row-wise operations.
* Practice combining list/dict comprehensions with real-world data (CSV, Pandas).

---

See you next time!
