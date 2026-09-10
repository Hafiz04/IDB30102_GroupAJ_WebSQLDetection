"""
SQL Injection Attack Detection
Using Ensemble Learning Approach

Algorithms:
- Random Forest
- Gradient Boosting
- Voting Classifier
"""


import pandas as pd

from sklearn.model_selection import train_test_split

from sklearn.feature_extraction.text import TfidfVectorizer

from sklearn.ensemble import (
    RandomForestClassifier,
    GradientBoostingClassifier,
    VotingClassifier
)

from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    classification_report
)



# ==========================
# Load Dataset
# ==========================


dataset = pd.read_csv(
    "../05_Data_or_Sample_Input/sql_injection_dataset.csv"
)


print(dataset.head())


# ==========================
# Feature Extraction
# Convert SQL text into numerical features
# ==========================


vectorizer = TfidfVectorizer()

X = vectorizer.fit_transform(
    dataset["query"]
)


y = dataset["label"]



# ==========================
# Split Training and Testing Data
# ==========================


X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)



# ==========================
# Individual Machine Learning Models
# ==========================


random_forest = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)



gradient_boosting = GradientBoostingClassifier()



# ==========================
# Ensemble Learning Model
# ==========================


ensemble_model = VotingClassifier(
    estimators=[
        (
            "random_forest",
            random_forest
        ),

        (
            "gradient_boosting",
            gradient_boosting
        )
    ],

    voting="soft"
)



# ==========================
# Training Model
# ==========================


ensemble_model.fit(
    X_train,
    y_train
)


print(
    "Model training completed!"
)



# ==========================
# Prediction
# ==========================


prediction = ensemble_model.predict(
    X_test
)



# ==========================
# Evaluation
# ==========================


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



print("\nEvaluation Result")

print("----------------")

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



print(
    "\nDetailed Report:"
)

print(
    classification_report(
        y_test,
        prediction
    )
)
