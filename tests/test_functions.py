
import os
import unittest
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from statsmodels.tsa.seasonal import seasonal_decompose


from app.utils import load_data, perform_seasonal_decomposition, perform_box_plot_analysis, perform_correlation_analysis



class TestFunctions(unittest.TestCase):

    def setUp(self):
        script_directory = os.path.dirname(os.path.abspath(__file__))

# Construct the path to the CSV file
        csv_file_path = os.path.join(script_directory, 'sierraleone-bumbuna.csv')

# Load the CSV file into a DataFrame
            
      
        self.data = pd.DataFrame({'GHI': [1, 2, 3, 4, 5]})
        self.variables = ['GHI', 'ModA']
        self.variable1 = 'GHI'
        self.variable2 = 'ModA'

    def test_load_data(self):
        result = load_data(self.file_path)
        self.assertIsInstance(result, pd.DataFrame)

    def test_perform_seasonal_decomposition(self):
        trend, seasonal, residual = perform_seasonal_decomposition(self.data, 2)
        self.assertIsInstance(trend, pd.Series)
        self.assertIsInstance(seasonal, pd.Series)
        self.assertIsInstance(residual, pd.Series)

    def test_perform_box_plot_analysis(self):
        fig = perform_box_plot_analysis(self.data, self.variables)
        self.assertIsInstance(fig, plt.Figure)

    def test_perform_correlation_analysis(self):
        correlation, scatter_plot = perform_correlation_analysis(self.data, self.variable1, self.variable2)
        self.assertIsInstance(correlation, float)
        self.assertIsInstance(scatter_plot, plt.Figure)


if __name__ == '__main__':
    unittest.main()