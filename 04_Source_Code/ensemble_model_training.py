"""
SQL Injection Attack Detection

Ensemble Learning Approach

Algorithms:
- Random Forest
- XGBoost
- Voting Classifier

Feature Extraction:
- TF-IDF Vectorization
"""


import pandas as pd


from sklearn.model_selection import train_test_split


from sklearn.feature_extraction.text import TfidfVectorizer


from sklearn.ensemble import RandomForestClassifier, VotingClassifier


from xgboost import XGBClassifier


from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    classification_report
)



# ==============================
# Load Dataset
# ==============================


dataset = pd.read_csv(
    "../05_Data_or_Sample_Input/sql_injection_dataset.csv"
)


print("Dataset Loaded")
print(dataset.head())



# ==============================
# Feature Extraction
# Convert SQL Query into numerical vector
# ==============================


vectorizer = TfidfVectorizer(
    lowercase=True
)


X = vectorizer.fit_transform(
    dataset["query"]
)


y = dataset["label"]



# ==============================
# Split Dataset
# ==============================


X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)



# ==============================
# Machine Learning Models
# ==============================


random_forest = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)



xgboost_model = XGBClassifier(
    n_estimators=100,
    random_state=42,
    eval_metric="logloss"
)



# ==============================
# Ensemble Learning Model
# ==============================


ensemble_model = VotingClassifier(

    estimators=[

        (
            "Random Forest",
            random_forest
        ),

        (
            "XGBoost",
            xgboost_model
        )

    ],

    voting="soft"

)



# ==============================
# Training
# ==============================


ensemble_model.fit(
    X_train,
    y_train
)


print(
    "\nEnsemble Model Training Completed"
)



# ==============================
# Prediction
# ==============================


prediction = ensemble_model.predict(
    X_test
)



# ==============================
# Performance Evaluation
# ==============================


accuracy = accuracy_score(
    y_test,
    prediction
)


precision = precision_score(
    y_test,
    prediction,
    average="weighted"
)


recall = recall_score(
    y_test,
    prediction,
    average="weighted"
)


f1 = f1_score(
    y_test,
    prediction,
    average="weighted"
)



print("\nModel Evaluation Result")
print("======================")

print(
    "Accuracy:",
    accuracy
)


print(
    "Precision:",
    precision
)


print(
    "Recall:",
    recall
)


print(
    "F1 Score:",
    f1
)



print("\nClassification Report")

print(
    classification_report(
        y_test,
        prediction
    )
)
