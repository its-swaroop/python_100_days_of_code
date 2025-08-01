# 🧠 Study Notes: Python Coffee Machine Project

*(Made using effective note-making strategies)*

---

### 📌 Overview

* Project simulates a real-life **coin-operated coffee machine**
* Must handle **3 drink types**: **Espresso**, **Latte**, and **Cappuccino**
* Key features:

  * Manage resources (water, milk, coffee)
  * Handle coin input (pennies, nickels, dimes, quarters)
  * Validate orders, process transactions
  * Provide reports and allow shutdown

---

### 🔧 Initial Setup

* **MENU** is a dictionary with drink names as keys, holding:

  * `ingredients` (water, milk, coffee)
  * `cost`
* **resources** is a dictionary tracking available ingredients
* `profit = 0` initialized to track earned money

---

### 🛠 Functional Requirements

#### 1. 🟢 Prompt User Input

* Ask: `"What would you like? (espresso/latte/cappuccino): "`
* Wrap input in a `while` loop to keep running until user types `"off"`

#### 2. 🔴 Shutdown Command

* If input is `"off"`, set `is_on = False` to break loop

#### 3. 📊 Print Report

* If input is `"report"`, print current `resources` and `profit`

```python
Water: 100ml  
Milk: 50ml  
Coffee: 30g  
Money: $2.50
```

---

### ⚙ Functional Breakdown

#### ✅ Check Resource Sufficiency

* Function: `is_resource_sufficient(order_ingredients)`
* Loops through required ingredients
* If any resource is **less than needed**, print `"Sorry, not enough [ingredient]"` and return `False`

#### 💰 Process Coins

* Function: `process_coins()`
* Ask user for:

  * # of quarters (×0.25)
  * # of dimes (×0.10)
  * # of nickels (×0.05)
  * # of pennies (×0.01)
* Calculate and return total inserted amount

#### 💳 Verify Transaction

* Function: `is_transaction_successful(money_received, drink_cost)`
* If **money < cost**: refund and return `False`
* If **money ≥ cost**:

  * Return change (`round(money - cost, 2)`)
  * Add drink cost to `profit`
  * Return `True`

#### ☕ Make Coffee

* Function: `make_coffee(drink_name, order_ingredients)`
* Deduct ingredients from `resources`
* Print `"Here is your [drink_name] ☕. Enjoy!"`

---

### 🌀 Program Flow (simplified)

```python
while is_on:
    choice = input()
    
    if choice == "off":
        is_on = False
    elif choice == "report":
        print resource levels and profit
    else:
        drink = MENU[choice]
        if is_resource_sufficient(drink["ingredients"]):
            payment = process_coins()
            if is_transaction_successful(payment, drink["cost"]):
                make_coffee(choice, drink["ingredients"])
```

---

### 🧠 Active Learning Reminders

* 💡 Think of each feature as a **modular function**
* ✂️ Avoid copying code without understanding (active > passive)
* 🔁 Use TODO comments to track implementation
* 🧩 Look for **connections** between requirements and Python structures (e.g., dictionaries, loops, conditionals)

---

### 🔍 What to Review Later

* How Python handles **global vs. local variables** (`global profit`)
* Best practices for **looping through dictionaries**
* Use of **f-strings** for formatting output
* Function return values and flow control (`if ... return False`)

---

### 📁 Filing & Organization Tips

* File: `main.py`
* Use comments like `# TODO 1: Print report` to break the task into manageable parts
* Organize functions at the top or bottom for easy editing

Crystal clear. You're using **"study in public"** not just to log progress—but to **add value** to your network. That means your posts should:

* Teach or inspire others (not just self-promote)
* Share insights, not just achievements
* Encourage others to try, reflect, or engage
* Show thoughtfulness in what you're learning and how you're applying it

---

### ✅ LinkedIn Post: *Documenting to Add Value*

> 🚀 **From Coffee to Code: What a Coffee Machine Taught Me About Python and Problem Decomposition**
>
> This week I built a virtual coffee machine in Python ☕—not with fancy hardware, but with logic, flow control, and a surprising number of design decisions.
>
> ✅ I practiced decomposing real-world problems into code
> ✅ Designed reusable functions like `process_coins()`, `make_coffee()`, and `is_transaction_successful()`
> ✅ Simulated real-world constraints (resource tracking, coin validation, feedback loops)
>
> But here’s where the value really clicked:
> → Even the simplest machines involve hidden logic
> → Small, clear functions help you test and think better
> → Clean structure = fewer bugs = more confidence
>
> If you’re starting out in Python or building your problem-solving skills, consider rebuilding a real-life process in code. It teaches more than tutorials ever could.
>
> I’ll be sharing more from my **study-in-public** journey. Feel free to connect if you’re building too 💻
>
> \#Python #100DaysOfCode #BuildInPublic #DevLearning #CodeNewbie #SoftwareEngineering #StudyInPublic #LearningByDoing

---

### ✅ X Post (Short + Value-First)

> Just built a virtual coffee machine in Python ☕
>
> It reinforced a lesson every new dev needs:
> → Break real-world logic into small, testable functions
> → Focus on clarity, not cleverness
>
> Code isn’t just syntax. It’s systems thinking.
>
> \#100DaysOfCode #Python #DevTips #BuildInPublic


To BE CONT.....
