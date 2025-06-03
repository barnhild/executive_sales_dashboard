import pandas as pd

def summarize_sales(df: pd.DataFrame) -> pd.DataFrame:
    monthly_sales = df.groupby('Month')['Sales'].sum().reset_index()
    monthly_sales['Growth (%)'] = monthly_sales['Sales'].pct_change() * 100
    return monthly_sales

def summarize_by_region(df: pd.DataFrame) -> pd.DataFrame:
    monthly_region_sales = df.groupby(['Month','Region'])['Sales'].sum().unstack()
    monthly_region_sales.index = monthly_region_sales.index.strftime('%Y-%m')
    return monthly_region_sales

def summarize_by_product(df: pd.DataFrame) -> pd.DataFrame:
    monthly_product_sales = df.groupby(['Month','Product'])['Sales'].sum().unstack()
    monthly_product_sales.index = monthly_product_sales.index.strftime('%Y-%m')
    return monthly_product_sales


