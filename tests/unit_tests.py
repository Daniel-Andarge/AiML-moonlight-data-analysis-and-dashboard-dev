import sys
import os
import unittest
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from statsmodels.tsa.seasonal import seasonal_decompose

parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(parent_dir)

from app.utils import load_data, perform_seasonal_decomposition, perform_box_plot_analysis, perform_correlation_analysis

class TestDataAnalysis(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # data  for the test cases
        cls.data_file = "cleaned_sierraleon_dataset.csv"
        cls.data = pd.read_csv(cls.data_file)

    def test_load_data(self):
        # Test if data is loaded successfully
        loaded_data = load_data(self.data_file)
        self.assertIsNotNone(loaded_data)
        self.assertIsInstance(loaded_data, pd.DataFrame)

    def test_perform_seasonal_decomposition(self):
        # Test seasonal decomposition
        period = 12
        trend, seasonal, residual = perform_seasonal_decomposition(self.data, period)
        self.assertIsNotNone(trend)
        self.assertIsNotNone(seasonal)
        self.assertIsNotNone(residual)

    def test_perform_box_plot_analysis(self):
        # Test box plot analysis
        variables = ["Variable1", "Variable2"]
        fig = perform_box_plot_analysis(self.data, variables)
        self.assertIsInstance(fig, plt.Figure)

    def test_perform_correlation_analysis(self):
        # Test correlation analysis
        variable1 = "Variable1"
        variable2 = "Variable2"
        correlation, scatter_plot_fig = perform_correlation_analysis(self.data, variable1, variable2)
        self.assertIsInstance(correlation, float)
        self.assertIsInstance(scatter_plot_fig, plt.Figure)

if __name__ == '__main__':
    unittest.main()