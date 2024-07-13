import pandas as pd
df = pd.read_csv('DataAnalyst.csv')

df.info()


def salary_set_cleaned(salary):


    if '$' in salary:
        salary = salary.replace('$', '')


    if '(Glassdoor est.)' in salary:
        salary = salary.replace('(Glassdoor est.)', '')
    if 'K' in salary:
        salary = salary.replace('K', '')

    salary_min = salary.split('-')[0]
    return salary_min
    salary_max = salary.split('-')[1]
    return salary_max






df['Salary_min'] = df['Salary Estimate'].apply(salary_set_cleaned)
df['Salary_max'] = df['Salary Estimate'].apply(salary_set_cleaned)
df.to_csv('Cleaned.csv')
#Дз видалити лишні стовпціц є приклад в дата клин після того очистити інші важливі та сробити візуалізацію


