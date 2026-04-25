# 🐍 Python Genesis: Programming, Data & Web Masterclass

[![Python Version](https://img.shields.io/badge/Python-3.10%2B-blue?logo=python&logoColor=white)](https://python.org)
[![Pandas Version](https://img.shields.io/badge/Pandas-Data%20Analysis-darkblue?logo=pandas&logoColor=white)](https://pandas.pydata.org)
[![Django Version](https://img.shields.io/badge/Django-Web%20Framework-green?logo=django&logoColor=white)](https://djangoproject.com)
[![Developer](https://img.shields.io/badge/Developer-Aditya%20Kumar-orange?logo=github)](https://github.com/aditya-forge)
[![Institution](https://img.shields.io/badge/B.Tech%20CSE-SRM%20University%20AP-red)](https://srmap.edu.in)

Welcome to **Python Genesis** — a master repository documenting my progressive journey from core programming foundations to data engineering and full-stack web architectures. 

This repository serves as a comprehensive reference for syntax, algorithmic problem solving, dataset manipulation, and modern web application development.

---

## 📚 Curriculum & Learning Roadmap

### 📦 Phase 1: Core Python Development
*Fundamentals, control flows, and functional abstractions.*
*   **Variables & Data Types:** Memory allocation, dynamic typing, type conversion, and input handling.
*   **Strings & Logic:** String slicing, formatting, and multi-path conditional execution (if-elif-else).
*   **Data Structures:** List manipulation, mutable vs. immutable sequences (tuples), key-value mapping (dictionaries), and unique sets.
*   **Control Flow:** Definite iteration (for), conditional iteration (while), and loop controls (break, continue, pass).
*   **Abstractions:** Functional modularity, scope resolution, and recursion theory.
*   **Data Persistence:** File stream operations (open, read, write, append) and context managers (`with`).

### 🐼 Phase 2: Data Engineering with Pandas
*Data manipulation, analysis, and statistical profiling.*
*   **Data Structures:** 1D arrays (Series) and tabular 2D relational data objects (DataFrames).
*   **Data Pipeline:** CSV and relational data loading, parsing, and serialization.
*   **Manipulation:** Data selection, axis filtering, location indexers (`.loc`, `.iloc`), and conditional subset querying.
*   **Statistics:** Summary statistics, data distributions (`.describe()`), and null-value imputation (`.fillna()`).

### 🌐 Phase 3: Web Architectures with Django
*Enterprise-ready Model-View-Template (MVT) systems.*
*   **Project Core:** Virtual environment setup, `manage.py` administrative workflow, settings routing, and application architecture.
*   **Database ORM:** Schema models, field definitions, relationships, and queries.
*   **View Layer:** URL dispatching, request-response handling, and view controllers.
*   **Templating & Styles:** Template inheritance (`extends`), context variable rendering, static asset management, and custom CSS styling.

---

## 🗂️ Repository Architecture

```text
python-genesis/
├── Python/                  # Core Python modules & practice sets
│   ├── [1-7]_*.py           # Theoretical concepts and code walkthroughs
│   └── L[1-6](PQ).py        # Practical application and algorithm questions
├── Pandas/                  # Data science modules
│   ├── Untitled.ipynb       # Jupyter notebook executing data exercises
│   └── *.csv                # Datasets utilized for engineering tasks
├── CHAI-DJANGO/             # Django web application
│   └── Project_Django/      # Core Django project root
└── README.md                # Repository overview & documentation
```

---

## 🚀 Setting Up the Workspace

### 1. Prerequisites
Ensure you have the latest version of Python and pip installed:
```bash
python --version
pip --version
```

### 2. Core Python Exercises
To run any core concept or practice solution file:
```bash
python Python/1_Variable&Datatype.py
```

### 3. Pandas Notebook
Install the required packages and run the Jupyter notebook server:
```bash
pip install pandas jupyter
jupyter notebook Pandas/Untitled.ipynb
```

### 4. Django Web Project
Set up the virtual environment, install dependencies, run migrations, and start the development server:
```bash
# Navigate to project directory
cd CHAI-DJANGO/Project_Django

# Create and activate virtual environment
python -m venv .venv
# On Windows:
.venv\Scripts\activate
# On macOS/Linux:
source .venv/bin/activate

# Install Django
pip install django

# Run migrations & start server
python manage.py migrate
python manage.py runserver
```

---

## 👨‍💻 Contact & Profile

*   **Developer:** Aditya Kumar
*   **Major:** B.Tech Computer Science and Engineering
*   **Affiliation:** SRM University, AP
*   **GitHub:** [@aditya-forge](https://github.com/aditya-forge)


