#exercise: https://leetcode.com/problems/exchange-seats/submissions/1843398129/

import pandas as pd

def exchange_seats(seat: pd.DataFrame) -> pd.DataFrame:
    ''' 
      this funcion swap the seats of the odd indices with the seats of the student in the next row
    '''
    j=seat['id'].size
    if j%2==1:
        j-=1
    odd=seat.loc[(seat.id<=j)&(seat.id%2==1),['student']].copy()
    even=seat.loc[(seat.id<=j)&(seat.id%2==0),['student']].copy()
    seat.loc[(seat.id<=j)&(seat.id%2==1),['student']]=even.to_numpy()
    seat.loc[(seat.id<=j)&(seat.id%2==0),['student']]=odd.to_numpy()
    return seat
