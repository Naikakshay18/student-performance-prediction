# 🎓 Student Performance Prediction

An end-to-end Machine Learning web application that predicts student academic performance based on academic, personal, and lifestyle factors. Built using **Python**, **Scikit-learn**, and **Streamlit** with a clean and interactive user interface.

---

## 🌐 Live Demo

🚀 **Try the application here:**

**https://student-performance-predictionv1.streamlit.app/**

---

## 📖 Project Overview

Student performance is influenced by multiple factors such as study habits, attendance, parental involvement, sleep hours, and access to educational resources. This project uses Machine Learning to analyze these factors and predict a student's academic performance.

The application allows users to enter student details through an interactive web interface and instantly receive a prediction.

---

## ✨ Features

- 🎯 Predict student academic performance
- 📊 Interactive Streamlit web application
- ⚡ Real-time predictions
- 🧠 Machine Learning model trained using Scikit-learn
- 🎨 Clean and responsive user interface
- 💾 Pre-trained model using Joblib
- 📈 Easy-to-use input form

---

## 🛠️ Tech Stack

| Technology | Purpose |
|------------|---------|
| Python | Programming Language |
| Streamlit | Web Application |
| Pandas | Data Processing |
| NumPy | Numerical Computing |
| Scikit-learn | Machine Learning |
| Joblib | Model Serialization |
| Git & GitHub | Version Control |

---

## 📂 Project Structure

```text
student-performance-prediction/
│
├── app/
│   ├── app.py
│   ├── ui.py
│   └── style.css
│
├── data/
│   ├── StudentPerformanceFactors.csv
│   └── cleaned_student_data.csv
│
├── models/
│   ├── student_model.pkl
│   └── label_encoders.pkl
│
├── src/
│   ├── preprocessing.py
│   ├── train_model.py
│   ├── visualization.py
│   ├── check_categories.py
│   └── main.py
│
├── requirements.txt
├── README.md
└── .gitignore
```

---

## 🚀 Installation

### Clone the repository

```bash
git clone https://github.com/Naikakshay18/student-performance-prediction.git
```

### Go to the project folder

```bash
cd student-performance-prediction
```

### Install dependencies

```bash
pip install -r requirements.txt
```

### Run the application

```bash
streamlit run app/app.py
```

---

## 📊 Dataset

The project uses a student performance dataset containing various academic and lifestyle attributes such as:

- Hours Studied
- Attendance
- Parental Involvement
- Access to Resources
- Previous Scores
- Sleep Hours
- Motivation Level
- Internet Access
- Family Income
- Teacher Quality
- School Type
- Distance from Home
- Extracurricular Activities
- Physical Activity
- Learning Disabilities
- Gender

These features are used to predict student academic performance.

---

## 🤖 Machine Learning Pipeline

- Data Collection
- Data Cleaning
- Data Preprocessing
- Feature Encoding
