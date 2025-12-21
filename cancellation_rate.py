import pandas as pd

def trips_and_users(trips: pd.DataFrame, users: pd.DataFrame) -> pd.DataFrame:
  '''
      The cancellation rate is computed by dividing the number of canceled (by client or driver) 
      requests with unbanned users by the total number of requests with unbanned users on that day.
      This function finds the cancellation rate of requests with unbanned users (both client and 
      driver must not be banned) each day between "2013-10-01" and "2013-10-03" with at least one trip.
      The Cancellation Rate is rounded to two decimal points.
  '''
    clients_unban=users[(users.role=='client') &(users.banned=='No')].rename(columns={'users_id':'client_id'})
    drivers_unban=users[(users.role=='driver')&(users.banned=='No')].rename(columns={'users_id':'driver_id'})
    t1=pd.merge(trips,clients_unban, on='client_id', how='inner')
    t2=pd.merge(t1,drivers_unban, on='driver_id',how='inner')
    t2['is_completed'] = (t2['status'] == 'completed').astype(int)
    t3 = 1 - t2.groupby('request_at')['is_completed'].mean().round(2)
    t3.name='Cancellation Rate'
    t4=t3.reset_index()
    t4.rename(columns={'request_at':'Day'},inplace=True)
    return t4[(t4['Day']>'2013-10-00') & (t4['Day']<'2013-10-04')]
