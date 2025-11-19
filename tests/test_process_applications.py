
import unittest
import os
import sys
import pandas as pd
from sklearn.tree import DecisionTreeClassifier
import joblib
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from src import process_applications

class TestProcessApplications(unittest.TestCase):

    def setUp(self):
        # Create a dummy application.csv for testing
        self.application_data = {
            'ApplicationId': [1, 2, 3],
            'reports': [0, 1, 0],
            'income': [50000, 75000, 60000],
            'active': [1, 0, 1],
            'expenditure': [2000, 1500, 2500],
            'age': [30, 45, 35]
        }
        self.application_df = pd.DataFrame(self.application_data)
        self.application_df.to_csv('application.csv', index=False)

        # Create a dummy model for testing
        X = [[0, 0, 0, 0], [1, 1, 1, 1], [0, 1, 0, 1]]
        y = [0, 1, 0]
        self.model = DecisionTreeClassifier()
        self.model.fit(X, y)
        joblib.dump(self.model, 'model.joblib')


    def tearDown(self):
        # Clean up the dummy files
        os.remove('application.csv')
        os.remove('model.joblib')
        if os.path.exists('SanitizedApplication.csv'):
            os.remove('SanitizedApplication.csv')
        if os.path.exists('unapproved_prediction.csv'):
            os.remove('unapproved_prediction.csv')
        if os.path.exists('prediction.csv'):
            os.remove('prediction.csv')

    def test_sanitize_data(self):
        process_applications.sanitize_data('application.csv', 'SanitizedApplication.csv')
        sanitized_df = pd.read_csv('SanitizedApplication.csv')
        self.assertEqual(list(sanitized_df.columns), ['reports', 'income', 'expenditure', 'age'])

    def test_make_predictions(self):
        process_applications.sanitize_data('application.csv', 'SanitizedApplication.csv')
        process_applications.make_predictions('SanitizedApplication.csv', 'model.joblib', 'unapproved_prediction.csv')
        predictions_df = pd.read_csv('unapproved_prediction.csv')
        self.assertEqual(list(predictions_df.columns), ['ApplicationId', 'Status'])

    def test_format_output(self):
        process_applications.sanitize_data('application.csv', 'SanitizedApplication.csv')
        process_applications.make_predictions('SanitizedApplication.csv', 'model.joblib', 'unapproved_prediction.csv')
        process_applications.format_output('unapproved_prediction.csv', 'prediction.csv')
        formatted_df = pd.read_csv('prediction.csv')
        self.assertTrue(all(status in ['Yes', 'No'] for status in formatted_df['Status']))

if __name__ == '__main__':
    unittest.main()
