from src.load_data import load_sales_data
from src.analyze import summarize_sales, summarize_by_region, summarize_by_product
from src.forecast import forecast_sales
# import pandas as pd
# import matplotlib.pyplot as plt
from src.visualize import (
    plot_monthly_sales,
    plot_region_breakdown,
    plot_product_breakdown,
    plot_forecast
)
from src.export_excel import export_report_to_excel

# from openpyxl import load_workbook
# from openpyxl.styles import Font
# from pandas import ExcelWriter
# from openpyxl.drawing.image import Image as ExcelImage
# from sklearn.linear_model import LinearRegression
# import numpy as np


# Load the Excel File

df = load_sales_data("data/sales_data.xlsx")

#step 3 Group by Month and sum the sales
monthly_sales = summarize_sales(df)
monthly_region_sales = summarize_by_region(df)
monthly_product_sales = summarize_by_product(df)

combined = forecast_sales(monthly_sales, periods_ahead = 3)

print(monthly_sales)
print("Monthly Sales data used for plotting")
print(monthly_sales)

plot_monthly_sales(monthly_sales)
plot_region_breakdown(monthly_region_sales)
plot_product_breakdown(monthly_product_sales)
plot_forecast(combined)



output_path = "output/sales_summary_report.xlsx"

charts_paths ={
    'Monthly Summary': 'output/monthly_sales_chart.png',
    'Region Breakdown': 'output/region_sales_chart.png',
    'Product Breakdown': 'output/product_sales_chart.png',
    'Forecast': 'output/sales_forecast_chart.png'
}

export_report_to_excel(
    path=output_path,
    monthly_sales=monthly_sales,
    region_data=monthly_region_sales,
    product_data=monthly_product_sales,
    forecast_data=combined,
    chart_paths=charts_paths
)



