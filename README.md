# 🚀 Nested JSON to Tabular using PySpark

## 📌 Project Overview

This project demonstrates how to process **nested JSON data** and convert it into a **structured tabular format** using PySpark.

The dataset follows a hierarchical structure:

user → orders → items

---

## ⚙️ Pipeline Steps

1. Read multi-line nested JSON
2. Apply explicit schema
3. Use explode() to flatten arrays
4. Transform nested structure into columns
5. Prepare clean dataset for analytics

---

## 📊 Output Schema

* USERID
* USERNAME
* EMAIL
* COUNTRY
* ORDERID
* ITEMID
* PRODUCT
* PRICE
* AMOUNT

---

## 🛠 Tech Stack

* PySpark
* JSON
* Data Transformation

---

## 💡 Key Learnings

* Handling nested JSON (arrays + structs)
* Importance of schema over inferSchema
* Using explode() for flattening
* Real-world ETL transformation logic

---

## 🚀 How to Run

```bash
pip install pyspark
python nested_json_pyspark.py
```

---

## 📷 Sample Output

(Add your screenshots here)

---

## 🔥 Real-World Use Case

This pipeline simulates how raw JSON data is transformed into structured format before storing in **Parquet / Data Lake** for analytics.

---

#DataEngineering #PySpark #BigData
