# Credit Card Fraud Detection

## Project Overview

Credit card fraud is a growing problem in the financial sector, leading to significant financial losses for banks and customers. The goal of this project is to build a machine learning model that can accurately detect fraudulent credit card transactions to minimize false positives and false negatives, thereby improving security and customer trust.

---

## Problem Statement

The task is to develop a predictive model that classifies transactions as fraudulent or legitimate based on historical transaction data. The challenge lies in dealing with highly imbalanced data (fraud cases are rare compared to legitimate transactions), requiring effective data preprocessing, feature engineering, and model tuning.

---

## Dataset

- The dataset contains anonymized credit card transactions.
- Features are numeric and have been transformed via PCA for confidentiality.
- Target variable: `Class` (0 = Legitimate, 1 = Fraudulent).

---

## Approach

1. **Data Exploration & Preprocessing**
   - Handled class imbalance with techniques such as SMOTE (Synthetic Minority Over-sampling Technique).
   - Feature scaling and normalization.
   - Analyzed feature distributions and correlations.

2. **Modeling**
   - Tried several classification algorithms:
     - Logistic Regression
     - Random Forest Classifier
     - Gradient Boosting Machines (XGBoost/LightGBM)
     - Support Vector Machines (SVM)
     - Neural Networks
   - Used cross-validation for robust evaluation.

3. **Evaluation Metrics**
   - Due to imbalanced data, accuracy is not a reliable metric.
   - Focused on precision, recall, F1-score, and especially ROC-AUC.
   - Confusion matrix analysis to understand false positives and false negatives.

4. **Hyperparameter Tuning**
   - Used Grid Search and Random Search for optimizing model parameters.

---

## Key Results

- Best performing model: [Model Name, e.g., XGBoost] with ROC-AUC of [value].
- Achieved high recall to reduce missed fraud cases while maintaining acceptable precision.
- Confusion matrix insights show effective separation between fraudulent and legitimate transactions.

---
## Tools and Libraries

- Python 3.x
- pandas, numpy
- scikit-learn
- imbalanced-learn (for SMOTE)
- matplotlib, seaborn
- XGBoost / LightGBM


** This project was completed as part of my ML & AI PG Diploma program.
