import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from statsmodels.tsa.seasonal import seasonal_decompose


def load_data(file_path):
    try:
        data = pd.read_csv(file_path)
        return data
    except pd.errors.ParserError:
        return None


def perform_seasonal_decomposition(data, period):
    decomposition = seasonal_decompose(data["GHI"], model='additive', period=period)
    trend = decomposition.trend
    seasonal = decomposition.seasonal
    residual = decomposition.resid
    return trend, seasonal, residual


def perform_box_plot_analysis(data, variables):
    boxplot_data = data[variables]
    fig, ax = plt.subplots()
    sns.boxplot(data=boxplot_data, ax=ax)
    ax.set_ylabel("Value")
    return fig


def perform_correlation_analysis(data, variable1, variable2):
    correlation = data[variable1].corr(data[variable2])
    scatter_plot = plt.figure(figsize=(8, 6))
    sns.scatterplot(x=data[variable1], y=data[variable2])
    plt.xlabel(variable1)
    plt.ylabel(variable2)
    plt.title("Scatter Plot")
    plt.grid(True)
    return correlation, scatter_plot