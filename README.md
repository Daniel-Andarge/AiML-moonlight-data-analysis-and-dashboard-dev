# MoonLight Energy Solutions Project

This repository contains the code and resources for the MoonLight Energy Solutions project. The project aims to provide a comprehensive analysis of solar energy data and develop a Streamlit dashboard for visualization and exploration. This README file serves as a guide for setting up the project environment and provides an overview of the development process.

## Usage Instructions

To set up the Python environment for this project, follow the steps below:

1. Clone the repository to your local machine:

   ```
   git clone https://github.com/Daniel-Andarge/MoonLight.git
   ```

2. Navigate to the project directory:

   ```
   cd moonlight-energy-solutions
   ```

3. Create a virtual environment specific to this project. Use the appropriate command for your operating system:

   - **Windows:**

     ```
     python -m venv venv
     venv\Scripts\activate
     ```

   - **Linux and macOS:**
     ```
     python3 -m venv venv
     source venv/bin/activate
     ```

4. Install the required packages by running the following command:

   ```
   pip install -r requirements.txt
   ```

5. With the environment set up and packages installed, you can now run the project.

## Development Process

The development process for the MoonLight Energy Solutions project involves two main stages: Exploratory Data Analysis (EDA) and Dashboard Development using Streamlit.

### 2.1 Exploratory Data Analysis (EDA)

During the EDA phase, the following analyses are performed on the solar energy dataset:

- Summary Statistics: Calculate descriptive statistics such as mean, median, and standard deviation for each numeric column in order to understand the data distribution.

- Data Quality Check: Identify missing values, outliers, or incorrect entries in columns such as GHI, DNI, DHI, and others.

- Time Series Analysis: Analyze how variables like GHI, DNI, DHI, and Tamb change over time. Plotting these metrics across the 'Timestamp' can help identify patterns or anomalies.

- Correlation Analysis: Determine the correlation between different variables, such as solar radiation components (GHI, DHI, DNI) and temperature measures (TModA, TModB), to uncover relationships.

- Wind Analysis: Explore wind speed (WS, WSgust, WSstdev) and wind direction (WD, WDstdev) data to identify trends or notable wind events.

- Temperature Analysis: Compare module temperatures (TModA, TModB) with ambient temperature (Tamb) to understand their relationship or variation under different conditions.

- Histograms: Create histograms for variables like GHI, DNI, DHI, WS, and temperatures to visualize their frequency distribution.

- Box Plots: Use box plots to examine the spread and presence of outliers in the solar radiation and temperature data.

- Scatter Plots: Generate scatter plots to explore relationships between pairs of variables, such as GHI vs. Tamb or WS vs. WSgust.

- Data Cleaning: Based on the initial analysis, handle anomalies and missing values, especially in columns like Comments, which may have null values.

### 2.2 Dashboard Development Using Streamlit & Deployment

Streamlit is a powerful Python library used for building interactive web applications. In this project, Streamlit is used to develop a dashboard for visualizing and exploring the solar energy data.

To run the Streamlit dashboard locally, execute the following command in your virtual environment:

```
streamlit run dashboard.py
```

The dashboard provides an intuitive interface to interact with the analyzed data and gain insights.

#### Deployment

The deployed version of the Streamlit dashboard can be accessed at [Deployment URL](https://example.com).

## Conclusion

The MoonLight Energy Solutions project aims to provide valuable insights into solar energy data through Exploratory Data Analysis and dashboard development using Streamlit.
