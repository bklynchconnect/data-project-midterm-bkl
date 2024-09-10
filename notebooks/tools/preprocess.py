import json
import pandas as pd

def load_json_file(fname):
    """
        This function loads a JSON file (assumed to be ASCII-readable) and then uses pandas json_normalize
        to extract the list of results.

        Arguments:
            fname -> string with the full path to the file

        Returns:
            df -> pandas dataframe of the results from this JSON file
    """

    # read the JSON file
    with open(fname,'r') as f:
        data_json = json.load(f)

    # convert JSON file to pandas dataframe
    df = pd.json_normalize(data_json['data']['results'])

    # return dataframe as function output
    return df