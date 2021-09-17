# -*- coding: utf-8 -*-
"""Standard atomic masses from CIAAW"""
from pathlib import Path
import pandas as pd
import numpy as np

DATA_PATH = str(Path(__file__).absolute().parent) + '/data'
DATA_FILE = DATA_PATH + '/CIAAW_masses.csv'


def parse_atomic_masses():
    """
    Read the CSV file containing the CIAAW standard atomic masses
    ranges have been converted to averages

    Returns a dictionary of the atomic masses indexed by atom symbol
    """

    ciaaw_df = pd.read_csv(DATA_FILE)
    #print(df)

    masses_dict = {}
    for _, row in ciaaw_df.iterrows():
        if not np.isnan(row['mass']):
            masses_dict[row['atom_symbol']] = row['mass']

    return masses_dict
