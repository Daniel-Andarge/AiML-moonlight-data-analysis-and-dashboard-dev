import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Set up the Streamlit app
st.title("Correlation Analysis")
uploaded_file = st.file_uploader("Upload a CSV file", type="csv")

if uploaded_file is not None:
    # Load the data into a DataFrame
    data = pd.read_csv(uploaded_file)

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