"""
SQL Injection Detection using Ensemble Learning

Data Preprocessing Module

Purpose:
This script prepares SQL query dataset before
machine learning model training.

Processing steps:
1. Load SQL injection dataset
2. Clean SQL query text
3. Remove unnecessary symbols
4. Convert text into standard format
5. Save processed dataset
"""


import pandas as pd
import re



# =====================================
# Function: Clean SQL Query
# =====================================

def clean_sql_query(query):

    """
    Clean SQL query input by:
    - converting text to lowercase
    - removing unnecessary symbols
    - removing extra spaces
    """

    # Convert input into string
    query = str(query)


    # Convert to lowercase
    query = query.lower()


    # Remove special characters
    query = re.sub(
        r'[^a-z0-9\s]',
        '',
        query
    )


    # Remove extra spaces
    query = re.sub(
        r'\s+',
        ' ',
        query
    )


    return query.strip()




# =====================================
# Function: Load Dataset
# =====================================

def load_dataset(file_path):

    """
    Load SQL injection dataset from CSV file.
    """

    data = pd.read_csv(file_path)


    print("Dataset Loaded Successfully")
    print("----------------------------")

    print(data.head())


    return data





# =====================================
# Function: Preprocess Dataset
# =====================================

def preprocess_dataset(data):

    """
    Apply text cleaning on SQL query column.
    """


    # Create new cleaned query column

    data["clean_query"] = data["query"].apply(
        clean_sql_query
    )


    return data





# =====================================
# Main Program
# =====================================

if __name__ == "__main__":


    # Dataset location

    dataset_path = (
        "../05_Data_or_Sample_Input/"
        "sql_injection_dataset.csv"
    )



    # Load dataset

    dataset = load_dataset(
        dataset_path
    )



    # Data preprocessing

    processed_dataset = preprocess_dataset(
        dataset
    )



    print("\nProcessed Dataset")
    print("-----------------")

    print(
        processed_dataset.head()
    )



    # Save processed dataset

    processed_dataset.to_csv(
        "processed_sql_dataset.csv",
        index=False
    )



    print(
        "\nData preprocessing completed successfully!"
    )
