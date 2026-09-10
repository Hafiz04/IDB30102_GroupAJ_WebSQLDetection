"""
SQL Injection Detection
Data Preprocessing Module

Purpose:
Clean and prepare SQL query dataset
for machine learning model training.
"""


import pandas as pd
import re


def clean_sql_query(query):
    """
    Remove unnecessary symbols
    and convert SQL query into lowercase
    """

    query = str(query).lower()

    # remove special characters
    query = re.sub(r'[^a-z0-9\s]', '', query)

    return query



def load_dataset(file_path):

    data = pd.read_csv(file_path)

    print("Dataset loaded successfully")
    print(data.head())

    return data



def preprocess_data(data):

    # Apply cleaning on SQL query column
    data["clean_query"] = data["query"].apply(clean_sql_query)

    return data



if __name__ == "__main__":

    dataset_path = "../05_Data_or_Sample_Input/sql_injection_dataset.csv"

    dataset = load_dataset(dataset_path)

    processed_data = preprocess_data(dataset)

    print("\nProcessed Dataset:")
    print(processed_data.head())

    processed_data.to_csv(
        "processed_sql_dataset.csv",
        index=False
    )

    print("\nPreprocessing completed!")
