"""
This module consolidates the functionality from the previous separate scripts
(sanitize.py, pred.py, and getpredout.py) into a single pipeline for processing
credit card applications.
"""
import pandas as pd
import joblib
from . import ServerAPI
from . import config

def sanitize_data(input_file, output_file):
    """
    Reads the specified columns from the input CSV file and writes them to the output CSV file.
    Parameters
    ----------
    input_file : str
        Path to the input CSV file containing application data.
    output_file : str
        Path to the output CSV file where sanitized data will be saved.
    """
    col_list = ["reports", "income", "expenditure", "age"]
    df = pd.read_csv(input_file, usecols=col_list)
    df.to_csv(output_file, index=False)

def make_predictions(input_file, model_file, output_file):
    """
    Loads a pre-trained model and applies it to the sanitized application data to predict approval status.
    Parameters:
        input_file (str): Path to the CSV file containing sanitized application data.
        model_file (str): Path to the joblib file containing the trained model.
        output_file (str): Path to the CSV file where prediction results will be saved.
    """
    features = ['reports', 'expenditure', 'age', 'income']
    df_sanitized = pd.read_csv(input_file)
    df_features = df_sanitized[features]
    model = joblib.load(model_file)
    predictions = model.predict(df_features)
    df_original = pd.read_csv(config.APPLICATION_DATA_FILE, usecols=['ApplicationId'])
    df_original.insert(1, 'Status', predictions)
    df_original.to_csv(output_file, index=False)

def format_output(input_file, output_file):
    """
    Formats the prediction output by converting the 'Status' column from numeric values to string labels.
    Args:
        input_file (str): Path to the input CSV file containing predictions with numeric 'Status'.
        output_file (str): Path to the output CSV file where formatted predictions will be saved.
    """
    df = pd.read_csv(input_file)
    df['Status'] = df['Status'].apply(lambda x: 'Yes' if x == 1 else 'No')
    df.to_csv(output_file, index=False)

if __name__ == "__main__":
    # Download the application data
    ServerAPI.download()

    # Sanitize the data
    sanitize_data(config.APPLICATION_DATA_FILE, config.SANITIZED_DATA_FILE)

    # Make predictions
    make_predictions(config.SANITIZED_DATA_FILE, config.MODEL_FILE, config.UNAPPROVED_PREDICTIONS_FILE)

    # Format the output
    format_output(config.UNAPPROVED_PREDICTIONS_FILE, config.PREDICTIONS_FILE)

    # Upload the predictions
    ServerAPI.upload()
