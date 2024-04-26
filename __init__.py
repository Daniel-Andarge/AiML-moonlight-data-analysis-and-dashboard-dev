
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from .app.utils import load_data, perform_seasonal_decomposition, perform_box_plot_analysis, perform_correlation_analysis

# Define any global variables or configurations
DEFAULT_FILE = "app/data/cleaned_sierraleon_dataset.csv"