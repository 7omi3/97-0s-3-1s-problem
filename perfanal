import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load the Excel file
file_path = 'perfanal.xlsx'
sheet_name = 'Raw'

# Read the data from the "Raw" tab
df = pd.read_excel(file_path, sheet_name=sheet_name)

# Convert the date column to datetime
df.iloc[:, 0] = pd.to_datetime(df.iloc[:, 0], dayfirst=True)

# Function to calculate annualized return
def calculate_annualized_return(data, periods_per_year=12):
    compounded_growth = (1 + data).prod()
    n_periods = len(data)
    annualized_return = compounded_growth ** (periods_per_year / n_periods) - 1
    return annualized_return * 100  # Convert to percentage

# Function to calculate annualized volatility
def calculate_annualized_volatility(data, periods_per_year=12):
    volatility = data.std() * np.sqrt(periods_per_year)
    return volatility * 100  # Convert to percentage

# Function to calculate maximum drawdown
def calculate_max_drawdown(data):
    cumulative = (1 + data).cumprod()
    peak = cumulative.cummax()
    drawdown = (cumulative - peak) / peak
    max_drawdown = drawdown.min()
    return max_drawdown * 100  # Convert to percentage

# Initialize dictionary to store results
results = {}

# Define periods for analysis in years
periods = {
    '1 year': 12,
    '3 year': 36,
    '5 year': 60,
    '10 year': 120,
    '15 year': 180
}

# Calculate returns, volatility, max drawdown for each portfolio
for portfolio in df.columns[1:]:
    portfolio_data = df[[df.columns[0], portfolio]].dropna()  # Include dates for filtering
    results[portfolio] = {}
    
    # Annual performance and volatility by year
    for year in range(2019, 2025):
        year_data = portfolio_data[portfolio_data.iloc[:, 0].dt.year == year][portfolio]
        if not year_data.empty:
            annual_return = calculate_annualized_return(year_data, periods_per_year=len(year_data))
            annual_volatility = calculate_annualized_volatility(year_data, periods_per_year=len(year_data))
            results[portfolio][f'{year}'] = {
                'Return (%)': annual_return,
                'Volatility (%)': annual_volatility
            }
        else:
            results[portfolio][f'{year}'] = {
                'Return (%)': None,
                'Volatility (%)': None
            }
    
    # Long-term performance and volatility
    for period_name, period_months in periods.items():
        if len(portfolio_data) >= period_months:
            period_data = portfolio_data[portfolio].iloc[-period_months:]  # Get the data for the required period
            annualized_return = calculate_annualized_return(period_data)
            annualized_volatility = calculate_annualized_volatility(period_data)
            results[portfolio][period_name] = {
                'Return (%)': annualized_return,
                'Volatility (%)': annualized_volatility
            }
        else:
            results[portfolio][period_name] = {
                'Return (%)': None,
                'Volatility (%)': None
            }

    # Calculate max drawdown for the entire period
    max_drawdown = calculate_max_drawdown(portfolio_data[portfolio])
    results[portfolio]['Max Drawdown (%)'] = max_drawdown

    # Plot histogram of returns
    plt.figure()
    plt.hist(portfolio_data[portfolio], bins=30, edgecolor='black')
    plt.title(f'Returns Distribution for {portfolio}')
    plt.xlabel('Returns')
    plt.ylabel('Frequency')
    plt.show()

# Print results
for portfolio, metrics in results.items():
    print(f"\nPortfolio: {portfolio}")
    for metric, values in metrics.items():
        if isinstance(values, dict):
            print(f"{metric}: Return = {values['Return (%)']:.2f}% Volatility = {values['Volatility (%)']:.2f}%")
        else:
            print(f"{metric}: {values:.2f}%")

\\\
def calculate_max_drawdown(data, start_date=None, end_date=None):
    """
    Calculate the maximum drawdown for a given data series within a specified timeframe.

    Parameters:
    - data (pd.Series): A pandas Series containing the returns.
    - start_date (str or pd.Timestamp, optional): The start date for the calculation.
    - end_date (str or pd.Timestamp, optional): The end date for the calculation.

    Returns:
    - max_drawdown (float): The maximum drawdown as a percentage.
    """
    # Filter data for the specified timeframe
    if start_date is not None:
        data = data[data.index >= pd.to_datetime(start_date)]
    if end_date is not None:
        data = data[data.index <= pd.to_datetime(end_date)]

    # Calculate cumulative returns and drawdowns
    cumulative = (1 + data).cumprod()
    peak = cumulative.cummax()
    drawdown = (cumulative - peak) / peak
    max_drawdown = drawdown.min()

    return max_drawdown * 100  # Convert to percentage
\\\
