import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from statsmodels.tsa.seasonal import seasonal_decompose

# Set the page title and description
st.title("Solar Radiation Analysis Dashboard")
st.write("Welcome to the Solar Radiation Analysis Dashboard. Explore different statistical analysis methodologies and visualize data insights.")

# Add a sidebar for user inputs
st.sidebar.header("Data Upload")
# Add a file uploader
uploaded_file = st.sidebar.file_uploader("Upload CSV file", type="csv")

# Add a separator in the sidebar
st.sidebar.markdown("---")

# Customization Options
st.sidebar.header("Customization Options")
selected_methodology = st.sidebar.selectbox("Select Methodology", ["Correlation Analysis", "Time-Series Analysis", "Box Plot Analysis"])

# Perform statistical analysis based on the user-selected methodology
if uploaded_file is not None:
    # Load the data into a DataFrame
    try:
        # Read the CSV file
        data = pd.read_csv(uploaded_file)
        
        st.subheader("Uploaded file contents")
        st.dataframe(data)
        
        # Perform further data processing or analysis if needed
    except pd.errors.ParserError:
        st.write("Error: Invalid CSV file. Please upload a valid CSV file.")
else:
    # Use default CSV file if no file is uploaded
    data = pd.read_csv("cleaned_sierraleon_dataset.csv")
    st.subheader("Uploaded file contents")
    st.dataframe(data)

# Methodology selection
if selected_methodology == "Time-Series Analysis":
    # Seasonal Decomposition
    st.header("Seasonal Decomposition")
    period = st.selectbox("Select Period", [7, 30, 365])
    decomposition = seasonal_decompose(data["GHI"], model='additive', period=period)
    trend = decomposition.trend
    seasonal = decomposition.seasonal
    residual = decomposition.resid

    # Plot the components
    st.subheader("Original")
    st.line_chart(data["GHI"])

    st.subheader("Trend")
    st.line_chart(trend)

    # Autocorrelation Analysis
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
        boxplot_data = data[variables]

        # Display the box plots
        fig, ax = plt.subplots()
        sns.boxplot(data=boxplot_data, ax=ax)
        ax.set_ylabel("Value")
        st.pyplot(fig)
    else:
        st.write("Please select at least one variable.")

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

    # Perform correlation analysis if both variables are numeric
    if variable1 and variable2:
        correlation = data[variable1].corr(data[variable2])

        # Display correlation coefficient
        st.subheader("Correlation Coefficient")
        st.write(f"The correlation coefficient between {variable1} and {variable2} is: {correlation:.2f}")

        # Create a scatter plot
        st.subheader("Scatter Plot")
        plt.figure(figsize=(8, 6))
            
        sns.scatterplot(x=data[variable1], y=data[variable2])
        plt.xlabel(variable1)
        plt.ylabel(variable2)
        plt.title("Scatter Plot")
        plt.grid(True)
        st.pyplot(plt)
    else:
        st.write("Please select numeric variables for correlation analysis.")        