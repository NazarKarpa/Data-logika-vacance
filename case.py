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

'201 to 500 employees'
def max_empress(empress):
    if 'employees' in empress:
        empress = empress.replace('+', '')
    if 'employees' in empress:
        empress = empress.replace('employees', '')
    empres_max = empress.split('to')[-1]




    return empres_max


'Company - Private, Company - Public'
def private_public_company(company):
    if 'count' in  company:
        company_list = company.replace('count', '')
    if 'Company' in  company:
        company_list = company.replace('Company', '')

    else:
        return 'Other'
    company_ = company_list.split('-')[-1]
    return company_

#$1 to $5 million (USD), $500 million to $1 billion (USD)

def reventue(reventue):

    if 'million' in reventue:
        reventue = reventue.replace('million', 'M')
    if '(USD)' in reventue:
        reventue = reventue.replace('(USD)', '')
    if '$' in reventue:
        reventue = reventue.replace('$', '')
    if 'billion' in reventue:
        reventue = reventue.replace('billion', 'B')
    if '+' in reventue:
        reventue = reventue.replace('+', '')

    reventue_max = reventue.split('to')[-1]
    return reventue_max

df['Type of ownership'] = df['Type of ownership'].apply(private_public_company)
df['Size'] = df['Size'].apply(max_empress)
df['Salary_min'] = df['Salary Estimate'].apply(salary_min)
df['Salary_max'] = df['Salary Estimate'].apply(max_salary)
df['Revenue'] = df['Revenue'].apply(reventue)

df = df.drop(['Unnamed: 0', 'Salary Estimate', 'Job Description', 'Company Name', 'Founded', 'Sector', 'Easy Apply', 'Headquarters', 'Location'], axis=1)#Видаляю стовпці
df.to_csv('Cleaned.csv')
df.info()
