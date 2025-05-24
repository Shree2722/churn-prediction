import pandas as pd
import json

def preprocess_dataset(df):
    df = df.drop(['customerID'], axis=1)
    df['TotalCharges'] = pd.to_numeric(df['TotalCharges'], errors='coerce')
    df.dropna(inplace=True)

    df['gender'] = df['gender'].map({'Male': 1, 'Female': 0})
    binary_cols = ['Partner', 'Dependents', 'PhoneService', 'PaperlessBilling', 'Churn']
    for col in binary_cols:
        df[col] = df[col].map({'Yes': 1, 'No': 0})

    df = pd.get_dummies(df, drop_first=True)
    X = df.drop('Churn', axis=1)
    y = df['Churn']

    with open("model_features.json", "w") as f:
        json.dump(list(X.columns), f)

    return X, y

def preprocess_form_input(input_data):
    df = pd.DataFrame([input_data])

  
    df['gender'] = 1 if df['gender'][0] == 'Male' else 0
    bin_map = {'Yes': 1, 'No': 0}
    for col in ['Partner', 'Dependents', 'PhoneService', 'PaperlessBilling']:
        df[col] = df[col].map(bin_map)

    df = pd.get_dummies(df)

    with open("model_features.json") as f:
        expected_columns = json.load(f)

    for col in expected_columns:
        if col not in df.columns:
            df[col] = 0

    df = df[expected_columns]

    return df
