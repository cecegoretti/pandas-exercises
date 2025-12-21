
import pandas as pd

def find_invalid_ips(logs: pd.DataFrame) -> pd.DataFrame:
  '''
      this function detects invalid ID, an ID is invalid if contains any number 
      bigger than 255 in any octet, any octet has a leading 0, had less or more 
      than 4 octet. It returns a dataframe containing two columns, the first one 
      tells the invalid IDs and the second one the number of times it was used
  '''
    def is_invalid(stringa):
        x=stringa.split('.')
        if len(x)!=4:
            return True
        if any([j.startswith('0') for j in x]):
            return True
        if any(int(j)>255 for j in x):
            return True
        return False
    mask=logs['ip'].apply(is_invalid)
    return logs[mask].groupby('ip')['log_id'].count().reset_index().rename(columns={'log_id':'invalid_count'}).sort_values(by=['invalid_count','ip'],ascending=False)
