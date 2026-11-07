"""
Risk scoring and explainability inference script for collections prioritization.
"""
import joblib
import pandas as pd
import numpy as np
from sklearn.linear_model import LogisticRegression

def train_risk_model(X_train, y_train):
    model = LogisticRegression(class_weight='balanced', max_iter=1000, random_state=42)
    model.fit(X_train, y_train)
    return model

def calculate_delinquency_risk(model, X_new):
    probabilities = model.predict_proba(X_new)[:, 1]
    return probabilities

def segment_risk_tier(prob):
    if prob >= 0.70:
        return 'High Risk - Proactive Restructuring'
    elif prob >= 0.40:
        return 'Medium Risk - Early Reminder & Support'
    else:
        return 'Low Risk - Standard Servicing'
