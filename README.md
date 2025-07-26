# Diabetes-Prediction-Model
# Diabetes Prediction Machine Learning Project

Predicting diabetes risk using clinical and lifestyle data with interpretable machine learning models.

---

## Table of Contents

- [Project Overview](#project-overview)  
- [Dataset](#dataset)  
- [Project Structure](#project-structure)  


---

## Project Overview

This project builds a machine learning pipeline for predicting diabetes onset using the Pima Indians Diabetes Dataset. It covers:

- Data cleaning and preprocessing  
- Feature engineering  
- Exploratory data analysis (EDA)  
- Model training with Logistic Regression, Random Forest, and XGBoost  
- Model evaluation using classification metrics and confusion matrices  
- Model interpretation with SHAP and LIME  
- (Optional) Deployment using Streamlit for an interactive web app  

---

## Dataset

- **Source:** [Pima Indians Diabetes Dataset on Kaggle](https://www.kaggle.com/datasets/uciml/pima-indians-diabetes-database)  
- **Description:** 768 samples, 8 clinical predictive features (e.g., Glucose, BMI, Age), and a binary target `Outcome` (0 = non-diabetic, 1 = diabetic).  
- **Stored in:** `data/raw/diabetes.csv`

---

## Project Structure

diabetes-ml/
│
├── data/
│ ├── raw/ # Original raw dataset CSV
│ └── processed/ # Scaled and feature-engineered datasets
│
├── models/ # Saved trained models and scalers
│
├── notebooks/ # Jupyter notebooks for each phase
│ ├── 1_data_preprocessing.ipynb # Data cleaning and preprocessing
│ ├── 2_exploratory_data_analysis.ipynb # Exploratory data analysis (EDA)
│ └── 3_model_building_training.ipynb # Model training and evaluation
│
└── README.md # Project documentation


