import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.seasonal import seasonal_decompose

# Load the solar radiation measurement data
data = pd.read_csv("cleaned_sierraleon_dataset.csv")


st.title("Solar Radiation Analysis Dashboard")
st.write("Welcome to the Solar Radiation Analysis Dashboard. Explore different statistical analysis methodologies and visualize data insights.")

# sidebar for user inputs
st.sidebar.header("Customization Options")
selected_methodology = st.sidebar.selectbox("Select Methodology", ["Time-Series Analysis", "Correlation Analysis", "Regression Analysis"])

if selected_methodology == "Time-Series Analysis":
    # Perform time-series analysis
    st.header("Time-Series Analysis")
    # Seasonal Decomposition
    st.subheader("Seasonal Decomposition")
    decomposition = seasonal_decompose(data["GHI"], model='additive', period=30)
    trend = decomposition.trend
    seasonal = decomposition.seasonal
    residual = decomposition.resid

    # Ploting
    st.subheader("Original")
    st.line_chart(data["GHI"])

    st.subheader("Trend")
    st.line_chart(trend)

    st.subheader("Seasonal")
    st.line_chart(seasonal)

    st.subheader("Residual")
    st.line_chart(residual)

    """ # Autocorrelation Analysis
    st.subheader("Autocorrelation Analysis")
    autocorrelation = data["GHI"].autocorr()
    st.write("Autocorrelation of GHI:", autocorrelation) """




elif selected_methodology == "Correlation Analysis":
    # Perform correlation analysis
    st.header("Correlation Analysis")
    
   

elif selected_methodology == "Regression Analysis":
    # Perform regression analysis
    st.header("Regression Analysis")
    # Add code here for regression analysis



# Visualize data insights
st.header("Data Insights")

# Example: Time-series plot of GHI
st.subheader("Time-Series Plot of Global Horizontal Irradiance (GHI)")
plt.plot(data["Timestamp"], data["GHI"])
plt.xlabel("Timestamp")
plt.ylabel("GHI (W/m²)")
plt.title("Global Horizontal Irradiance (GHI) Over Time")
st.pyplot(plt)

# Example: Scatter plot of GHI vs. Ambient Temperature
st.subheader("Scatter Plot of GHI vs. Ambient Temperature")
plt.scatter(data["GHI"], data["Tamb"])
plt.xlabel("GHI (W/m²)")
plt.ylabel("Ambient Temperature (°C)")
plt.title("GHI vs. Ambient Temperature")
st.pyplot(plt)



# Display the cleaned data table
st.subheader("Solar Radiation Measurement Data")
st.dataframe(data)

