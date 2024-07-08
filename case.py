import pandas as pd
df = pd.read_csv('DataAnalyst.csv')

df.info()


def salary_set_min(salary):
    global df
    if salary[0] == '$':
        df = df.replace({'$': ''})

    else:
        return -1

df['Salary Estimate'] = df['Salary Estimate'].apply(salary_set_min)
df.to_csv('Cleaned.csv')



