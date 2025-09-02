# ⏱️ Pomodoro Timer App with Tkinter – Enhanced Notes (Portfolio Style)

---

## 1. Introduction – Pomodoro Technique

* Work in **25 min sessions**, separated by **5 min breaks**.
* After 4 sessions → **long break (20 min)**.

**Visual Cycle**:

```
[ Work 25 ] → [ Break 5 ] → [ Work 25 ] → [ Break 5 ] 
     ↑                                    ↓
     ←------ Long Break (20) after 4 -----→
```

---

## 2. UI with Canvas & Image

* `Canvas` lets you overlay **image + text**.

```python
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
```

---

## 3. Layout with Grid & Widgets

* **Grid layout** for structure:

```
   Row 0 →   [     "Timer" Label     ]
   Row 1 →   [      Tomato Canvas    ]
   Row 2 → [Start Btn]   [Reset Btn]
   Row 3 →   [   ✔ Progress Label    ]
```

---

## 4. Timer Mechanism (Core Logic)

* Tkinter’s `after()` schedules function calls.

**Flowchart**:

```
count_down(time)
   ↓
 update canvas → if count > 0 → after(1000, count_down)
   ↓
 count == 0 → start_timer() → decide session type
```

### Key Code

```python
def count_down(count):
    mins, secs = divmod(count, 60)
    canvas.itemconfig(timer_text, text=f"{mins}:{secs:02d}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
```

---

## 5. Reset Button Functionality

* Must cancel active `after()` calls or multiple timers run.

```python
def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    title_label.config(text="Timer", fg=GREEN)
    check_marks.config(text="")
    global reps
    reps = 0
```

---

## 6. Checkmark Tracker

* Motivational ✔ for each work session.

```python
marks = ""
work_sessions = reps // 2
marks = "✔" * work_sessions
check_marks.config(text=marks)
```

**Progress Example**:

```
Work → ✔
Work + Break → ✔✔
4 Sessions → ✔✔✔✔
```

---

# 🎯 Mini Exercises (Portfolio Extensions)

1. **Custom Session Lengths**

   * Change work session to **50 min**, short break to **10 min**.
   * Tip: update constants in `start_timer()`.

2. **Pause Button**

   * Add `pause_timer()` to freeze current countdown.
   * Hint: store `count` value globally and cancel `after()`.

3. **Different Progress Icons**

   * Replace ✔ with emojis: 🌱 → 🌿 → 🌳.
   * Example: after 4 sessions → 🌳🌳🌳🌳.

4. **Sound Alert**

   * Play a beep when switching sessions (`winsound.Beep()` on Windows).

5. **Dark Mode UI**

   * Add toggle button that switches background & text colors dynamically.

---

# 🔑 Big Picture Recap

* **UI** → Canvas, Grid, Labels, Buttons.
* **Logic** → `after()` for countdown, reps counter for sessions.
* **Reset** → cancels timers, clears state.
* **Progress** → ✔ or custom symbols for work completion.

👉 With these notes + exercises, you not only **understand the Pomodoro app**, but also have **clear next steps** to extend it into a *portfolio-ready project*.

---

See you next time!
