# 📘 Password Manager with Tkinter – Complete Chapter Notes

## 1. Introduction – Project Overview

* Goal: Build a **Password Manager App** to securely store and generate strong passwords.
* Core Features:

  1. **GUI** built with Tkinter.
  2. Save website, email/username, and password to a text file.
  3. Generate **random strong passwords** automatically.
  4. Validate user input before saving.
  5. Use popup dialogs to alert the user about actions or errors.
* Why this project matters:

  * Practice **Tkinter widgets** like `Entry`, `Label`, `Button`.
  * Understand file handling in Python.
  * Learn how to structure a small real-world app.

---

## 2. UI Setup

* Tkinter window configured with **padding and title**:

  ```python
  window = Tk()
  window.title("Password Manager")
  window.config(padx=50, pady=50)
  ```
* Use a **Canvas widget** to display a logo image:

  ```python
  canvas = Canvas(width=200, height=200)
  logo_img = PhotoImage(file="logo.png")
  canvas.create_image(100, 100, image=logo_img)
  canvas.grid(row=0, column=1)
  ```
* Layout uses `grid()` to align widgets cleanly.

---

## 3. Form Inputs & Layout

The form consists of three input fields:

1. **Website**
2. **Email/Username**
3. **Password**

Example layout:

```python
# Labels
website_label = Label(text="Website:")
website_label.grid(row=1, column=0)
email_label = Label(text="Email/Username:")
email_label.grid(row=2, column=0)
password_label = Label(text="Password:")
password_label.grid(row=3, column=0)

# Entry fields
website_entry = Entry(width=35)
website_entry.grid(row=1, column=1, columnspan=2)
website_entry.focus()

email_entry = Entry(width=35)
email_entry.grid(row=2, column=1, columnspan=2)
email_entry.insert(0, "user@example.com")  # default text

password_entry = Entry(width=21)
password_entry.grid(row=3, column=1)
```

Buttons:

```python
generate_button = Button(text="Generate Password", command=generate_password)
generate_button.grid(row=3, column=2)

add_button = Button(text="Add", width=36, command=save_password)
add_button.grid(row=4, column=1, columnspan=2)
```

---

## 4. Validating Input & Popups – *Focus Lesson*

### Why validation is needed:

* Prevent saving incomplete or incorrect data.
* Ensure the file remains organized and reliable.

### Popup Dialogs:

* Use **Tkinter messagebox** for user alerts:

  ```python
  from tkinter import messagebox
  messagebox.showinfo(title="Title", message="Details")
  messagebox.showwarning(title="Warning", message="Incomplete data!")
  ```

### Validation Logic:

```python
def save_password():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    if len(website) == 0 or len(password) == 0:
        messagebox.showwarning(title="Oops", message="Please don't leave any fields empty!")
    else:
        is_ok = messagebox.askokcancel(
            title=website,
            message=f"These are the details entered:\nEmail: {email}\nPassword: {password}\nIs it ok to save?"
        )
        if is_ok:
            with open("data.txt", "a") as file:
                file.write(f"{website} | {email} | {password}\n")
            website_entry.delete(0, END)
            password_entry.delete(0, END)
```

---

## 5. Password Generator – *Focus Lesson*

Generates **secure, random passwords** with a mix of letters, numbers, and symbols.

### Steps:

1. Use `random` and `string` modules.
2. Combine character sets: letters, digits, symbols.
3. Shuffle and join for randomness.

### Code:

```python
import random

def generate_password():
    letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    numbers = '0123456789'
    symbols = '!#$%&()*+'

    password_letters = [random.choice(letters) for _ in range(random.randint(8, 10))]
    password_symbols = [random.choice(symbols) for _ in range(random.randint(2, 4))]
    password_numbers = [random.choice(numbers) for _ in range(random.randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    random.shuffle(password_list)

    password = "".join(password_list)
    password_entry.delete(0, END)
    password_entry.insert(0, password)
```

---

## 6. Final Integration & Workflow – *Focus Lesson*

### Final Flow:

1. **User enters website & email** → clicks **Generate Password**.
2. Password is auto-filled in the password field.
3. **Click Add** → app validates input:

   * If fields empty → warning popup.
   * If valid → confirm popup.
4. Data saved to `data.txt` in the format:

   ```
   Website | Email | Password
   ```
5. Clears the website and password fields for next entry.

---

## ✅ Summary

* **Lesson 1–3:** Built the interface → logo, labels, entry fields, buttons.
* **Lesson 4:** Added validation with `messagebox` to prevent errors and confirm actions.
* **Lesson 5:** Created a secure password generator with `random`.
* **Lesson 6:** Integrated all parts into a complete app with clean data flow.

**Outcome:**
A fully functional Password Manager capable of generating, validating, and storing secure passwords with a simple Tkinter GUI.

---

See you next time!
