import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv('Cleaned.csv')
df.info()
df.plot(kind='scatter', x = 'Size', y = 'Salary_max')

plt.show()
