import pandas as pd 
from datetime import timedelta

def fill_missing_values(df):

    #converting date column to date time format
    df['date'] = pd.to_datetime(df['date'])

    #To ensure there is consistency in the data, sorting the data in the descending order of the date
    df = df.sort_values(by='date', ascending=False)

    expected_dates = pd.date_range(start=df['date'].min(), end=df['date'].max(), freq='D')
    missing_dates = expected_dates[~expected_dates.isin(df['date'])]

    for date in missing_dates:
        prev_day = date - timedelta(days=1)
        prev_day_data = df[df['date'] == prev_day]
        if not prev_day_data.empty:
            prev_day_values = prev_day_data.iloc[0].to_dict()
            prev_day_values['date'] = date
            df = pd.concat([df, pd.DataFrame([prev_day_values])], ignore_index=True)
    
    df = df.sort_values(by='date', ascending=True)
        
    return df