# config.py
import os

FTP_HOST = "ftp.drivehq.com"
FTP_USER = os.environ.get("FTP_USER", "your_username")
FTP_PASS = os.environ.get("FTP_PASS", "your_password")

APPLICATION_DATA_FILE = "application.csv"
SANITIZED_DATA_FILE = "SanitizedApplication.csv"
MODEL_FILE = "model.joblib"
UNAPPROVED_PREDICTIONS_FILE = "unapproved_prediction.csv"
PREDICTIONS_FILE = "prediction.csv"
