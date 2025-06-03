import matplotlib.pyplot as plt

def plot_monthly_sales(monthly_sales, path="output/monthly_sales_chart.png"):
    plt.figure(figsize=(8,5))
    plt.bar(monthly_sales['Month'].astype(str), monthly_sales['Sales'],color='steelblue')
    plt.title('Monthly Total Sales')
    plt.xlabel('Month')
    plt.ylabel("Total Sales ($)")
    plt.tight_layout()
    plt.savefig(path)
    plt.close()

def plot_region_breakdown(region_df, path="output/region_sales_chart.png"):
    region_df.plot(kind='bar', stacked=True, figsize=(8,5))
    plt.title('Monthly Sales by Region')
    plt.xlabel('Month')
    plt.ylabel("Total Sales ($)")
    plt.tight_layout()
    plt.savefig(path)
    plt.close()

def plot_product_breakdown(product_df, path="output/product_sales_chart.png"):
    product_df.plot(kind='line', marker ='o', figsize=(8,5))
    plt.title('Monthly Sales by Product')
    plt.xlabel('Month')
    plt.ylabel("Total Sales ($)")
    plt.tight_layout()
    plt.savefig(path)
    plt.close()

def plot_forecast(combined_df, path="output/sales_forecast_chart.png"):
    actual = combined_df[combined_df['Forecast'] == False]
    forecast = combined_df[combined_df['Forecast'] == True]

    plt.figure(figsize=(8,4))
    plt.plot(actual['Month'].astype(str), actual['Sales'], marker ='o', label='Actual')
    plt.plot(forecast['Month'].astype(str), forecast['Sales'], marker ='o', linestyle='--', color = 'orange', label='Forecast')

    plt.title("Monthly Sales with Forecast")
    plt.xlabel("Month")
    plt.ylabel("Sales ($)")
    plt.legend()
    plt.tight_layout()
    plt.savefig(path)
    plt.close()


