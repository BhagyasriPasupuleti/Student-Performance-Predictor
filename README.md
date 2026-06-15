# Student Performance Predictor

A machine learning application that predicts student academic performance using Linear Regression based on study hours and attendance percentage.

**Status:** Active | **Language:** Python 3.11

---

## Overview

This project implements a predictive model to forecast student marks based on key learning indicators. It enables educators and students to identify performance trends and make data-driven improvement decisions.

## Table of Contents

- [Features](#features)
- [Technology Stack](#technology-stack)
- [Installation](#installation)
- [Usage](#usage)
- [Model Details](#model-details)
- [Dataset](#dataset)
- [Results](#results)
- [Contributing](#contributing)
- [License](#license)

---

## Features

- **Predictive Modeling**: Linear Regression for mark prediction
- **Real-Time Predictions**: Get instant predictions based on user input
- **Simple Interface**: User-friendly command-line application
- **Extensible Design**: Ready for additional features and advanced models
- **CSV Data Management**: Lightweight data storage and handling

---

## Technology Stack

- **Python 3.11** - Core language
- **scikit-learn** - Machine learning library
- **pandas** - Data processing and manipulation
- **NumPy** - Numerical computing

---

## Installation

### Prerequisites
- Python 3.11 or higher
- pip (Python Package Manager)

### Quick Start
```bash
# Clone repository
git clone https://github.com/BhagyasriPasupuleti/Student-Performance-Predictor
cd student-performance-predictor

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install pandas scikit-learn numpy
```

---

## Usage

### Running the Application

```bash
python app.py
```

### Example

```
Enter Study Hours: 5
Enter Attendance Percentage: 85

Predicted Marks: 72.45
```

---

## Model Details

### Algorithm: Linear Regression

The model establishes a linear relationship between input features and student marks:

```
Input Features:
  - Study Hours (continuous)
  - Attendance % (continuous)
        ↓
  [Linear Regression]
        ↓
  Output: Predicted Marks (0-100)
```

### Training Code

```python
from sklearn.linear_model import LinearRegression

# Load data
X = data[["StudyHours", "Attendance"]]
y = data["Marks"]

# Train model
model = LinearRegression()
model.fit(X, y)

# Make predictions
prediction = model.predict([[5, 85]])
```

### Why Linear Regression?

- Simple and interpretable results
- Fast training and prediction
- Clear understanding of feature importance
- Effective for initial performance analysis

---

## Dataset

### Features

| Feature | Type | Range |
|---------|------|-------|
| StudyHours | Float | 0-15 hours |
| Attendance | Float | 0-100% |
| Marks | Float | 0-100 (target) |

### Sample Data
```
StudyHours,Attendance,Marks
2,65,35
3,70,42
4,75,48
5,80,55
6,85,62
7,90,70
8,95,80
```

---

## Results

### Sample Predictions

| Study Hours | Attendance (%) | Predicted Marks |
|-------------|-----------------|-----------------|
| 2 | 60 | 28.45 |
| 4 | 75 | 54.30 |
| 6 | 85 | 72.15 |
| 8 | 95 | 89.90 |

### Key Insights

- Strong positive correlation between study hours and marks
- Attendance is a key indicator of academic performance
- Model captures the relationship between effort and outcomes

---

## Project Structure

```
student-performance-predictor/
├── README.md                 # Documentation
├── app.py                    # Main application
├── student_data.csv          # Dataset
└── .gitignore               # Git configuration
```
---
## Author
**Bhagyasri**
- B.Tech Student | AI & ML Enthusiast
- GitHub: [@BhagyasriPasupuleti]https://github.com/BhagyasriPasupuleti
---
