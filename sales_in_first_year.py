#exercise: https://leetcode.com/problems/product-sales-analysis-iii/submissions/1863210275/
#techniques: an inner merge to make a fast selection of the desired sales

import pandas as pd

def sales_analysis(sales: pd.DataFrame) -> pd.DataFrame:
  '''
    this function returns the sales of each item in the first year eache product
    was sold
  '''
    first_year=sales.groupby('product_id')['year'].min()
    first_year.name='year'
    a=pd.merge(sales,first_year.reset_index(), how='inner')
    return a[['product_id','year','quantity','price']].rename(columns={'year':'first_year'})
