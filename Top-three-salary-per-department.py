import pandas as pd

def top_three_salaries(employee: pd.DataFrame, department: pd.DataFrame) -> pd.DataFrame:
  '''
    fidn the employee with the top three salaries in each department
  '''
    a=employee.copy()
    a['rank_in_dep']=a.groupby('departmentId')['salary'].rank(ascending=False, method='dense')
    a.rename(columns={'id':'departmentId','name':'Department'}, inplace=True)
    t=pd.merge(a,department, on='departmentId',how='inner')
    t.rename(columns={'name':'Employee','salary':'Salary'}, inplace=True)
    return t.loc[t['rank_in_dep']<=3, ['Department','Employee','Salary']]
