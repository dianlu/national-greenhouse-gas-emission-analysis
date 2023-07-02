import pandas as pd
import numpy as np

def fetch_and_process():
    ''' 
    Fetch data from public source and preprocess for analysis.

    Return:
        data: Pandas dataframe, processed raw data
    '''
    # Load data
    data = pd.read_csv('http://www.cleanenergyregulator.gov.au/DocumentAssets/Documents/Greenhouse%20and%20energy%20information%20by%20registered%20corporation%202021-22.csv')

    # Convert String to numbers
    data['Total scope 1 emissions (t CO2-e)']=data['Total scope 1 emissions (t CO2-e)'].str.replace(',', '').astype(np.int64)
    data['Total scope 2 emissions (t CO2-e)']=data['Total scope 2 emissions (t CO2-e)'].str.replace(',', '').astype(np.int64)
    data['Net energy consumed (GJ)']=data['Net energy consumed (GJ)'].str.replace(',', '').astype(np.int64)

    # Calculate emission efficiency
    data['total emission']=data['Total scope 1 emissions (t CO2-e)']+data['Total scope 2 emissions (t CO2-e)']
    data['share']=data['total emission']/data['Net energy consumed (GJ)']
    return data
    
