# -*- coding: utf-8 -*-
"""DREIDING Force Field, from https://doi.org/10.1021/j100389a010"""
from pathlib import Path
import pandas as pd

from .codata_2018 import CAL_TO_JOULE

DATA_PATH = str(Path(__file__).absolute().parent) + '/data'
DATA_FILE = DATA_PATH + '/DREIDING.csv'


def parse_dreiding():
    """
    Read the CSV file containing the DREIDING force field parameters from
    Table II of the original paper. Units are preserved from the paper

    Returns a dictionary of the force field parameters for a conventional
    12-6 Lennard-Jones potential.

      V(r) = 4 epsilon ( (sigma/r)**12 - (sigma/r)**6 )

    sigma = angstroms
    epsilon = kJ/mol
    """

    ff_df = pd.read_csv(DATA_FILE)
    #print(df)

    ff_dict = []
    for _, row in ff_df.iterrows():
        ff_dict.append({
            'atom_label': row['atom_label'],
            'atom_symbol': row['atom_symbol'],
            'sigma': row['R0'] / 2.0**(1. / 6.),  # R0 native units are ang
            'epsilon':
            row['D0'] * CAL_TO_JOULE,  # D0 native units are kcal/mol
            'source': 'DREIDING',
            'sigma_units': 'ang',
            'epsilon_units': 'kJ/mol'
        })
    return ff_dict
