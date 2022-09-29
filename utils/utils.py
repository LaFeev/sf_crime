from genericpath import isfile
import pandas as pd


def get_dataset(path_to_data):
    '''reads/downloads the SF crime stats csv for 2018-2022, trims columns, and returns a DataFrame'''
    fname = path_to_data + "Police_Department_Incident_Reports__2018_to_Present.csv"
    url = "https://data.sfgov.org/api/views/wg3w-h783/rows.csv?accessType=DOWNLOAD"

    # this function gets called at the beginning of the notebook, every time.  If you want to change
    #  which columns get dropped, update the remove_cols.dat file prior to running/rerunning the
    #  notebook.  Because the columns are being read in from file, it isn't necessary to re-import
    #  the utils module after making a change to the remove_cols.dat file.
    cols_fname = path_to_data + "remove_cols.dat"

    try:
        # try to open the full data file
        with open(fname, "r") as f:
            full_data = pd.read_csv(f)
    except FileNotFoundError:
        # full dataset csv not found locally, go download it
        full_data = pd.read_csv(url)
        # write the full dataset to the data directory to avoid downloading next time
        full_data.to_csv(fname, index=False)

    # remove columns specified by cols_fname
    cols = pd.read_csv(cols_fname)
    trim_data = full_data.drop(cols['col'], axis = 1)

    return trim_data
