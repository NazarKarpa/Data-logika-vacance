import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv('Cleaned.csv')
df.info()
df.plot(y = 'Revenue', x = 'Salary_max', kind = 'scatter')

plt.show()
