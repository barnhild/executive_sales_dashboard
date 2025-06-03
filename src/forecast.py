import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression


def forecast_sales(monthly_sales: pd.DataFrame, periods_ahead: int = 3) -> pd.DataFrame:
    # Add MonthIndex Column
    monthly_sales = monthly_sales.copy()
    monthly_sales['MonthIndex'] = np.arange(len(monthly_sales))
    # Features (X) and Target (y)
    X = monthly_sales[['MonthIndex']]
    y = monthly_sales['Sales']
    # Train Test Split
    model = LinearRegression()
    model.fit(X, y)
    # Forecast
    last_index = monthly_sales['MonthIndex'].iloc[-1]
    future_indexes = np.arange(last_index + 1, last_index + 1 + periods_ahead)
    future_X = pd.DataFrame(future_indexes, columns=['MonthIndex'])
    future_sales = model.predict(future_X)
    # Create Forecast DataFrame
    future_months = pd.period_range(start=monthly_sales['Month'].iloc[-1] + 1, periods=periods_ahead, freq='M')
    forecast_df = pd.DataFrame({
        'Month': future_months,
        'Sales': future_sales.round(0),
        'Forecast': True
    })

    # combine historical + forecast
    monthly_sales['Forecast'] = False
    combined = pd.concat([monthly_sales[['Month', 'Sales','Forecast']], forecast_df], ignore_index=True)
    return combined

