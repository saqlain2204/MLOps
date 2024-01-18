from zenml import pipeline, step
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from zenml.steps import Output
import numpy as np

@step
def load_data():
    "Loading the dataset"
    training_data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
    print("Data loaded successfully")
    return {'features': training_data}

@step
def process_data(data: dict):
    "Processing the dataset"
    df = pd.DataFrame(data)
    print("Data processed successfully")
    return df

@step
def sum(df: pd.DataFrame):
    "Printing the sum of the dataset"
    ans = np.sum(df)
    print(ans)

@pipeline
def simple_pipeline():
    print("Running pipeline")
    data = load_data()
    df = process_data(data)
    sum(df)
    

if __name__ == "__main__":
    run = simple_pipeline()
