import os
import pandas as pd


def combine_data (path):
    folder_path = f'{path}//'
    combined_data = pd.DataFrame()

    for filename in os.listdir(folder_path):
        if filename.endswith('.csv'):
            # Extract company name from the file name
            company_name = filename.split('_')[0]

            # Read the CSV file into a DataFrame
            file_path = os.path.join(folder_path, filename)
            data = pd.read_csv(file_path)

            # Add a 'company' column with the extracted company name
            data['ticker'] = company_name

            # Concatenate the data to the combined DataFrame
            combined_data = pd.concat([combined_data, data], ignore_index=True)

    combined_data.to_csv(f'{path}//combined_tata_data.csv', index=False)

    return print('Combined data available in the original folder')