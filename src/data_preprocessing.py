"""
Data preprocessing pipeline for Geldium Finance delinquency dataset.
"""
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler

def load_data(filepath: str) -> pd.DataFrame:
    df = pd.read_csv(filepath)
    return df

def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    df_clean = df.copy()
    # Check for missing values and impute with median if needed
    for col in df_clean.select_dtypes(include=[np.number]).columns:
        if df_clean[col].isnull().sum() > 0:
            df_clean[col] = df_clean[col].fillna(df_clean[col].median())
    return df_clean

def extract_features(df: pd.DataFrame):
    feature_cols = [
        'age', 'annual_income', 'credit_limit', 'current_balance',
        'credit_utilization_ratio', 'debt_to_income_ratio', 'missed_payments_6m'
    ]
    X = df[feature_cols]
    y = df['delinquent_flag'] if 'delinquent_flag' in df.columns else None
    return X, y
