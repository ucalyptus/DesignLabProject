
import pandas as pd
import joblib
import requests
import numpy as np
from . import ServerAPI

def sanitize_data(input_file, output_file):
    # Code from sanitize.py
    col_list = ["reports", "income", "active", "expenditure", "age"]
    df = pd.read_csv(input_file, usecols=col_list)
    df.to_csv(output_file, index=False)

def make_predictions(input_file, model_file, output_file):
    # Code from pred.py
    features = ['reports', 'expenditure', 'age', 'income']
    df = pd.read_csv(input_file)
    df = df[features]
    model = joblib.load(model_file)
    card = model.predict(df)
    df = pd.read_csv("application.csv", usecols=['ApplicationId'])
    df.insert(1, 'Status', card)
    df.to_csv(output_file, index=False)

def format_output(input_file, output_file):
    # Code from getpredout.py
    df = pd.read_csv(input_file)
    df['Status'] = df['Status'].apply(lambda x: 'Yes' if x == 1 else 'No')
    df.to_csv(output_file, index=False)

if __name__ == "__main__":
    # Download the application data
    ServerAPI.download()

    # Sanitize the data
    sanitize_data('application.csv', 'SanitizedApplication.csv')

    # Make predictions
    make_predictions('SanitizedApplication.csv', 'model.joblib', 'unapproved_prediction.csv')

    # Format the output
    format_output('unapproved_prediction.csv', 'prediction.csv')

    # Upload the predictions
    ServerAPI.upload()
