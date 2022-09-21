from genericpath import isfile
import pandas as pd
import os.path


def get_dataset(path_to_data):
    '''reads/downloads the SF crime stats csv for 2018-2022 and saves it into 3 separate csv files'''
    fname = path_to_data + "Police_Department_Incident_Reports__2018_to_Present.csv"
    url = "https://data.sfgov.org/api/views/wg3w-h783/rows.csv?accessType=DOWNLOAD"

    if not os.path.isfile(path_to_data + "full_data_1.csv") and \
        not os.path.isfile(path_to_data + "full_data_2.csv") and \
        not os.path.isfile(path_to_data + "full_data_3.csv"):
        
        try:
            with open(fname, "r") as f:
                full_data = pd.read_csv(f)
        except FileNotFoundError:
            # full dataset csv not found locally
            full_data = pd.read_csv(url)
        
        # write the full dataset to the data directory in 3 chunks (to limit size < 100MB)
        # note only full_data_1 will contain a header row
        full_data.iloc[:213333].to_csv(path_to_data + "full_data_1.csv")
        full_data.iloc[213333:426666].to_csv(path_to_data + "full_data_2.csv")
        full_data.iloc[426666:].to_csv(path_to_data + "full_data_3.csv")
