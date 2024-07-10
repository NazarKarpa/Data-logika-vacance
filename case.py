import pandas as pd
df = pd.read_csv('DataAnalyst.csv')

df.info()


def salary_set_cleaned(salary):

    if '$' in salary:
        salary = salary.replace('$', '')
    if '-' in salary:
        salary = salary.replace('-', '')
    if '(Glassdoor est.)' in salary:
        salary = salary.replace('(Glassdoor est.)', '')
    if 'K' in salary:
        salary = salary.replace('K', '')
    return salary
def group_salary(salary):
    global df

    for df['Salary Estimate'] in range(2253):
        df.insert(2, 'Min_salary', 1)

df = group_salary(['Salary Estimate'])

df['Salary Estimate'] = df['Salary Estimate'].apply(salary_set_cleaned)
df.to_csv('Cleaned.csv')



