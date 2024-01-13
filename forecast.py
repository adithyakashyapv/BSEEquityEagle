import os
import pandas as pd 
from prophet import Prophet


def forecast(folder_path):
    for filename in os.listdir(folder_path):
        if filename.endswith('.csv'):
            company_name = filename.split('.')[0]
            file_path = os.path.join(folder_path, filename)
            data = pd.read_csv(file_path)
            new_data = data[['date', 'close']]
            new_data['date'] = pd.to_datetime(new_data['date'])
            
            # Rename columns to match Prophet's expectations
            new_data.rename(columns={'date': 'ds', 'close': 'y'}, inplace=True)
            
            print(new_data)
            
            m = Prophet()
            m.add_country_holidays(country_name='IN')
            m.fit(new_data)
            future = m.make_future_dataframe(periods=365)
            forecast = m.predict(future)
            forecast = forecast[['ds', 'yhat', 'yhat_lower', 'yhat_upper']]
            forecast.to_csv(os.path.join(folder_path, f'{company_name}_forecast_data.csv'))
            print(f'Forecast data of {company_name} available in the original folder')

def main():
    # Specify the folder path here or pass it as an argument when running the script
    folder_path = 'path'

    forecast(folder_path)

if __name__ == "__main__":
    main()

