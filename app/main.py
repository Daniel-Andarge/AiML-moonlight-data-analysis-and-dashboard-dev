import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Set the page title and description
st.title("Solar Radiation Analysis Dashboard")
st.write("Welcome to the Solar Radiation Analysis Dashboard. Explore different statistical analysis methodologies and visualize data insights.")

# Add a sidebar for user inputs
st.sidebar.header("Data Upload")
uploaded_file = st.sidebar.file_uploader("Upload CSV file", type="csv")

# Load the solar radiation measurement data
data = pd.read_csv(uploaded_file) if uploaded_file is not None else None

# Add a separator in the sidebar
st.sidebar.markdown("---")

# Customization Options
st.sidebar.header("Customization Options")
selected_methodology = st.sidebar.selectbox("Select Methodology", ["Time-Series Analysis", "Correlation Analysis",  "Regression Analysis"])

# Perform statistical analysis based on the selected methodology
if selected_methodology == "Time-Series Analysis":
    # Perform time-series analysis
    st.header("Time-Series Analysis")


elif selected_methodology == "Correlation Analysis":
    # Perform correlation analysis
    st.header("Correlation Analysis")
 

elif selected_methodology == "Regression Analysis":
    # Perform regression analysis
    st.header("Regression Analysis")
   

# Visualize data insights
st.header("Data Insights")

if data is not None:
    # Time-series plot of GHI
    st.subheader("Time-Series Plot of Global Horizontal Irradiance (GHI)")
    plt.plot(data["Timestamp"], data["GHI"])
    plt.xlabel("Timestamp")
    plt.ylabel("GHI (W/m²)")
    plt.title("Global Horizontal Irradiance (GHI) Over Time")
    st.pyplot(plt)

    # Scatter plot of GHI vs. Ambient Temperature
    st.subheader("Scatter Plot of GHI vs. Ambient Temperature")
    plt.scatter(data["GHI"], data["Tamb"])
    plt.xlabel("GHI (W/m²)")
    plt.ylabel("Ambient Temperature (°C)")
    plt.title("GHI vs. Ambient Temperature")
    st.pyplot(plt)



# Display the cleaned data table if data is available
if data is not None:
    st.subheader("Solar Radiation Measurement Data")
    st.dataframe(data)