# Day 5 Study Notes – For Loops & Password Generator

## 1. Introduction: Why Loops?

* Loops let us **repeat code automatically** without writing it multiple times.
* Useful for iterating over collections (like lists) or generating ranges of numbers.
* Example analogy: Bart Simpson writing the same sentence 100 times — a loop could do that instantly.

---

## 2. The `for` Loop with Lists

### Basic Syntax:

```python
fruits = ["apple", "peach", "pear"]

for fruit in fruits:
    print(fruit)
```

### What happens internally:

* The loop assigns each element of the list to the temporary variable (`fruit`) one by one.
* First iteration → `fruit = "apple"`, then `"peach"`, then `"pear"`.
* Each indented line executes for every item.

### Adding More Code Inside Loop:

```python
for fruit in fruits:
    print(fruit)
    print(fruit + " pie")
```

Output:

```
apple
apple pie
peach
peach pie
pear
pear pie
```

### Indentation Matters:

* Indented code runs **inside the loop**, repeated each time.
* Non-indented code runs only **after the loop ends**.

---

## 3. Looping to Build Functions Ourselves

### Example: `sum()`

Python provides `sum()`, but we can recreate it.

```python
student_scores = [150, 142, 199, 178, 155]

total = 0
for score in student_scores:
    total += score
print(total)  # 824
```

### Example: `max()`

Python has `max()`, but let’s build it manually:

```python
student_scores = [150, 142, 199, 178, 155]

max_score = 0
for score in student_scores:
    if score > max_score:
        max_score = score
print(max_score)  # 199
```

---

## 4. The `range()` Function

* Generates a sequence of numbers (not a list, but iterable).

### Basic Usage:

```python
for number in range(1, 11):  # 1 to 10 inclusive
    print(number)
```

### With Step Size:

```python
for number in range(1, 11, 3):
    print(number)  # 1, 4, 7, 10
```

---

## 5. The Gauss Challenge (Adding 1 to 100)

**Task**: Add all numbers from 1 → 100.

### Gauss’ Insight:

* Pair numbers: `1 + 100 = 101`, `2 + 99 = 101`, …
* 50 pairs of `101`.
* Answer: `50 * 101 = 5050`.

### Python Solution with Loop:

```python
total = 0
for number in range(1, 101):  # 1 to 100
    total += number
print(total)  # 5050
```

---

## 6. Project – PyPassword Generator

### Easy Version:

* Ask user how many **letters**, **symbols**, **numbers**.
* Generate in sequence: letters → symbols → numbers.

```python
import random

letters = ['a','b','c',...,'Z']
numbers = ['0','1','2',...,'9']
symbols = ['!','#','$','%','&','*','+']

nr_letters = int(input("How many letters? "))
nr_symbols = int(input("How many symbols? "))
nr_numbers = int(input("How many numbers? "))

password = ""

for char in range(nr_letters):
    password += random.choice(letters)

for char in range(nr_symbols):
    password += random.choice(symbols)

for char in range(nr_numbers):
    password += random.choice(numbers)

print(f"Your password is: {password}")
```

➡️ Generates passwords like `ghTYui@%23`.

---

### Hard Version:

* Same inputs, but order of characters is randomized.
* Store characters in a **list**, shuffle, then join into string.

```python
import random

letters = ['a','b','c',...,'Z']
numbers = ['0','1','2',...,'9']
symbols = ['!','#','$','%','&','*','+']

nr_letters = int(input("How many letters? "))
nr_symbols = int(input("How many symbols? "))
nr_numbers = int(input("How many numbers? "))

password_list = []

for char in range(nr_letters):
    password_list.append(random.choice(letters))

for char in range(nr_symbols):
    password_list.append(random.choice(symbols))

for char in range(nr_numbers):
    password_list.append(random.choice(numbers))

random.shuffle(password_list)

password = ""
for char in password_list:
    password += char

print(f"Your password is: {password}")
```

➡️ Example Output: `A2%qR7&ybT1`.
Each run → different order.

---

## 7. Key Takeaways

* `for` loops let us execute code repeatedly, often with lists or ranges.
* `range(start, end, step)` is powerful for number-based loops.
* Accumulators (`+=`) let us build totals, maximums, or strings.
* Randomness (`random.choice`, `random.shuffle`) adds unpredictability.
* Easy Password = predictable pattern; Hard Password = shuffled, much stronger.

---

## Quick Self-Check

1. What does this code print?

   ```python
   for number in range(2, 10, 2):
       print(number)
   ```
2. Rewrite `max([4, 7, 2, 9])` using a `for` loop and conditionals.
3. Why is `random.shuffle()` useful for password generation?
4. What’s the difference between these two loops?

   ```python
   for fruit in fruits: ...
   for i in range(len(fruits)): ...
   ```
5. How would you sum numbers 1 to 200 without writing 200 additions?

---

✅ That wraps up **Day 5**.
See you next time!
