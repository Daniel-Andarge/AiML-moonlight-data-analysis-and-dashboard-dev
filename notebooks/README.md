## Exploratory Data Analysis (EDA)

During the EDA phase, the following analyses are performed on the solar energy dataset:

[Please Click Here to view the Exploratory-Data-Analysis.ipynb file](https://github.com/Daniel-Andarge/MoonLight/blob/main/Exploratory-Data-Analysis.ipynb).

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
