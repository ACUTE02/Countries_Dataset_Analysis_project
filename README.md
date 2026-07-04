# 🌍 Countries Data Analysis with Python

### Exploratory Data Analysis (EDA) using Pandas & NumPy

![Python](https://img.shields.io/badge/Python-3.8+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-Data%20Analysis-150458?style=for-the-badge&logo=pandas&logoColor=white)
![NumPy](https://img.shields.io/badge/NumPy-Numerical%20Computing-013243?style=for-the-badge&logo=numpy&logoColor=white)
![Status](https://img.shields.io/badge/Status-Completed-success?style=for-the-badge)

---

# 📖 Overview

This project performs **Exploratory Data Analysis (EDA)** on a global countries dataset using **Python, Pandas, and NumPy**.

The objective is to practice data preprocessing techniques and solve real-world analytical questions related to countries, populations, political leaders, democracy scores, regions, and continents.

It is a beginner-friendly project for learning practical Pandas operations used in Data Science.

---

# 📂 Repository Structure

```text
Countries-Data-Analysis/
│
├── Countries.csv
├── capstone_project.py
└── README.md
```

---

# 📊 Dataset Information

The dataset contains information about countries, including:

- 🌍 Country Name
- 🏛 Capital City
- 👥 Population
- 🌎 Continent
- 🌐 Region
- 🗳 Democracy Score
- 👤 Political Leader
- 📄 Country Long Name

---

# 🔍 Analysis Performed

## ✅ Data Preprocessing

- Dataset Information
- Shape of Dataset
- Data Types
- Summary Statistics
- Column Inspection

---

## ✅ Population Analysis

- Country with the highest population
- Country with the lowest population
- Capital city of the most populated country
- Capital city of the least populated country

---

## ✅ Democracy Score Analysis

- Countries sorted by democracy score
- Ranking based on democracy index

---

## ✅ Region Analysis

- Total number of unique regions
- Number of countries in each region
- Countries belonging to Eastern Europe

---

## ✅ Political Leader Analysis

- Political leader of the second most populated country
- Countries with missing political leader information

---

## ✅ String Operations

Using the `apply()` function to:

- Count countries whose names start with a specific letter
- Count countries containing the word **Republic**

---

## ✅ Continent Analysis

Finding the most populated country in Africa.

---

# 📚 Pandas Concepts Used

✔ Data Loading

```python
pd.read_csv()
```

✔ Dataset Inspection

```python
info()
describe()
shape
columns
```

✔ Filtering

```python
df[df['column']]
```

✔ Sorting

```python
sort_values()
```

✔ Counting

```python
value_counts()
count()
```

✔ Largest Values

```python
nlargest()
```

✔ Missing Values

```python
isna()
```

✔ String Processing

```python
apply()
startswith()
lower()
```

---

# 🛠 Technologies Used

- Python
- Pandas
- NumPy

---

# 🚀 Installation

Clone the repository

```bash
git clone https://github.com/your-username/Countries-Data-Analysis.git
```

Move into the project

```bash
cd Countries-Data-Analysis
```

Install dependencies

```bash
pip install pandas numpy
```

Run the project

```bash
python capstone_project.py
```

---

# 📊 Project Workflow

```
Countries Dataset
        │
        ▼
Data Loading
        │
        ▼
Data Inspection
        │
        ▼
Data Preprocessing
        │
        ▼
Exploratory Data Analysis
        │
        ▼
Insights & Results
```

---

# 🎯 Skills Demonstrated

- Exploratory Data Analysis (EDA)
- Data Preprocessing
- Data Cleaning
- Filtering & Sorting
- Missing Value Analysis
- String Operations
- Aggregation
- Data Querying
- Pandas Fundamentals
- NumPy Basics

---

# 📌 Sample Insights

- 🌍 Most populated country
- 🏛 Capital of the largest country
- 🌎 Number of world regions
- 👤 Missing political leader records
- 📊 Democracy score rankings
- 🌍 Largest country in Africa by population
- 🌐 Countries in Eastern Europe

---

# 👨‍💻 Author

**Ayushmaan Gupta**

🎓 B.Tech CSE (AI & ML)

### Skills

- Python
- Pandas
- NumPy
- Data Analysis
- Machine Learning

---

# ⭐ Support

If you found this project useful,

⭐ Star this repository

🍴 Fork the project

📢 Share it with others

---

<div align="center">

**Made with ❤️ by Ayushmaan Gupta**

*"Data is the new oil, but insight is the refined fuel."*

</div>
