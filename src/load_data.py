import pandas as pd

def load_sales_data(filepath: str) -> pd.DataFrame:
    df = pd.read_excel(filepath)
    df['Date'] = pd.to_datetime(df['Date'])
    df['Month'] = df['Date'].dt.to_period('M')
    return df


