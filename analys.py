import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv('Cleaned.csv')
df.info()
df['Rating'].value_counts().plot(kind = 'barh')

plt.show()
