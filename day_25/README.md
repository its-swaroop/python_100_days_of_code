# Day 25: <br/>Working with CSV Data & Pandas Library

### **1. Reading CSV Data**

* Python has a built-in `csv` module, but it’s a bit clunky.
* **Pandas** makes it much easier.
* `pandas.read_csv("filename.csv")` → loads CSV into a **DataFrame** (like an Excel sheet).
* DataFrame basics:

  * Columns = labels
  * Rows = records
  * Works like both a list and a dictionary.

---

### **2. Accessing Data in Pandas**

* **Get a column:**
  `data["column_name"]` or `data.column_name`
* **Convert column to list:**
  `data["column_name"].to_list()`
* **Calculate statistics:**

  * `data["column_name"].mean()`
  * `data["column_name"].max()`

---

### **3. Rows and Conditions**

* **Get a row:**
  `data[data.column_name == "value"]`
* **Example:** Find row where day == "Monday"

  ```python
  monday = data[data.day == "Monday"]
  print(monday.temp)
  ```

---

### **4. Creating DataFrames**

* Can build from scratch with a dictionary:

  ```python
  data_dict = {
      "students": ["Amy", "James", "Angela"],
      "scores": [76, 56, 65]
  }
  new_data = pandas.DataFrame(data_dict)
  new_data.to_csv("new_file.csv")
  ```

---

### **5. Real Example: Weather Data**

* Given a `weather_data.csv`:

  * Average temp: `data["temp"].mean()`
  * Max temp: `data["temp"].max()`
  * Get condition of hottest day:

    ```python
    hottest_day = data[data.temp == data.temp.max()]
    print(hottest_day.condition)
    ```

---

### **6. Key Takeaways**

* Pandas makes CSV handling much easier than raw Python.
* `DataFrame` = table-like structure, powerful for filtering & stats.
* Columns = Series (like lists), Rows = filtered by conditions.
* Easy to create new CSVs from DataFrames.
* Perfect stepping stone into **data science** workflows.

---
See you next time!
