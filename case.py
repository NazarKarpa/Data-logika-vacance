import pandas as pd
df = pd.read_csv('DataAnalyst.csv')

df.info()


def salary_min(salary):


    if '$' in salary:
        salary = salary.replace('$', '')


    if '(Glassdoor est.)' in salary:
        salary = salary.replace('(Glassdoor est.)', '')
    if 'K' in salary:
        salary = salary.replace('K', '')

    salary_min = salary.split('-')[0]
    return salary_min

def max_salary(salary):
    if '$' in salary:
        salary = salary.replace('$', '')


    if '(Glassdoor est.)' in salary:
        salary = salary.replace('(Glassdoor est.)', '')
    if 'K' in salary:
        salary = salary.replace('K', '')
    salary_max = salary.split('-')[1]
    return salary_max





df['Salary_min'] = df['Salary Estimate'].apply(salary_min)
df['Salary_max'] = df['Salary Estimate'].apply(max_salary)

df = df.drop(['Unnamed: 0', 'Salary Estimate', 'Job Description', 'Company Name', 'Founded', 'Sector', 'Easy Apply', 'Headquarters', 'Location'], axis=1)#Видаляю стовпці
df.to_csv('Cleaned.csv')
df.info()
#Дз  очистити інші важливі та сробити візуалізацію


