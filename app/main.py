import os
import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from utils import load_data, perform_seasonal_decomposition, perform_box_plot_analysis, perform_correlation_analysis

# Set the page title and description
st.title("Solar Radiation Analysis Dashboard")
st.write("Welcome to the Solar Radiation Analysis Dashboard. Explore different statistical analysis methodologies and visualize data insights.")

# sidebar for user inputs
st.sidebar.header("Data Upload")
# file uploader
uploaded_file = st.sidebar.file_uploader("Upload CSV file", type="csv")

# separator in the sidebar
st.sidebar.markdown("---")

# Customization Options
st.sidebar.header("Customization Options")
selected_methodology = st.sidebar.selectbox("Select Methodology", ["Correlation Analysis", "Time-Series Analysis", "Box Plot Analysis"])

# Perform statistical analysis based on the user-selected methodology
if uploaded_file is not None:
    # Load the data into a DataFrame
    data = load_data(uploaded_file)
    if data is not None:
        st.subheader("Uploaded file contents - Default Cleaned Serra-Leone Data ")
        st.dataframe(data)
    else:
        st.write("Error: Invalid CSV file. Please upload a valid CSV file.")
else:
    # Use default CSV file if no file is uploaded
    data_folder = os.path.join(os.path.dirname(__file__), 'Data')
    file_path = os.path.join(data_folder, 'cleaned_sierraleon_dataset.csv')
    data = pd.read_csv(file_path)
    st.subheader("Uploaded file contents - Default Cleaned Serra-Leone Data")
    st.dataframe(data)

# Methodology selection
if selected_methodology == "Time-Series Analysis":
    # Seasonal Decomposition
    st.header("Seasonal Decomposition")
    period = st.selectbox("Select Period", [7, 30, 365])
    trend, seasonal, residual = perform_seasonal_decomposition(data, period)

    # Plot the components
    st.subheader("Original")
    st.line_chart(data["GHI"])

    st.subheader("Trend")
    st.line_chart(trend)

    # Auttocorrelation Analysis
    st.subheader("Autocorrelation Analysis")
    autocorrelation = data["GHI"].autocorr()
    st.write("Autocorrelation of GHI:", autocorrelation)

    # Moving Averages
    st.subheader("Moving Averages")
    window_size = st.slider("Select Window Size", 5, 365, 30)
    moving_average = data["GHI"].rolling(window=window_size).mean()

    st.subheader("Original vs. Moving Average")
    plt.figure(figsize=(10, 6))
    plt.plot(data.index, data["GHI"], label='Original')
    plt.plot(data.index, moving_average, label=f"Moving Average (Window Size {window_size})")
    plt.xlabel("Timestamp")
    plt.ylabel("GHI (W/m²)")
    plt.title("Moving Averages of Global Horizontal Irradiance (GHI)")
    plt.legend()
    st.pyplot(plt)

elif selected_methodology == "Box Plot Analysis":
    # Perform box plot analysis
    st.header("Box Plot Analysis")

    # Select the variables for box plot analysis
    variables = st.multiselect("Select variables", data.columns)

    if len(variables) > 0:
        # Perform box plot analysis
        fig = perform_box_plot_analysis(data, variables)

        # Display the box plots
        st.pyplot(fig)
    else:
        st.write("Please select at leastone variable for box plot analysis.")

elif selected_methodology == "Correlation Analysis":
    # Perform correlation analysis
    st.header("Correlation Analysis")

    # Select variables for correlation analysis
    numeric_columns = data.select_dtypes(include=["number"]).columns
    datetime_columns = data.select_dtypes(include=["datetime"]).columns
    variables = numeric_columns.union(datetime_columns)

    # Set default variables
    default_variable1 = "GHI"
    default_variable2 = "Tamb"

    variable1 = st.selectbox("Select Variable 1", variables, index=variables.get_loc(default_variable1))
    variable2 = st.selectbox("Select Variable 2", variables, index=variables.get_loc(default_variable2))

    # Perform correlation analysis
    correlation, scatter_plot = perform_correlation_analysis(data, variable1, variable2)

    # Display the correlation coefficient and scatter plot
    st.write("Correlation Coefficient:", correlation)
    st.pyplot(scatter_plot)