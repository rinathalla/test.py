import pandas as pd
import matplotlib.pyplot as pl
df = pd.read_csv('data.csv')
df.shape
df.describe()
df['Units'].count()
num_bins = 10
pl.hist(df['Amount'], num_bins, normed=1, facecolor='blue', alpha=0.5)
pl.show()

#Sales by month
sales_by_month = df.groupby('Month').size()
print(sales_by_month)

#Plotting the Graph
plot_by_month = sales_by_month.plot(title='Monthly Sales',xticks=(1,2))
plot_by_month.set_xlabel('Months')
plot_by_month.set_ylabel('Total Sales')

#Sales by hour
sales_by_hour = df.groupby('Hour').size()
plot_by_hour = sales_by_hour.plot(title='Hourly Sales',xticks=(range(5,22)))
plot_by_hour.set_xlabel('Working Hours')
plot_by_hour.set_ylabel('Total Sales')
