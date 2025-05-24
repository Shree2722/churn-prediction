import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
import joblib

from preprocess import preprocess_dataset

df = pd.read_csv('churn_dataset.csv')
X, y = preprocess_dataset(df)

model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X, y)

joblib.dump(model, 'churn_model.pkl')

import json

with open("model_features.json", "w") as f:
    json.dump(list(X.columns), f)
