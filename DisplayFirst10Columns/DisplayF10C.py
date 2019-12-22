import pandas as pd
sample_data = pd.read_csv('Dispy10Row.csv')
print(sample_data.iloc[:10, :10])
