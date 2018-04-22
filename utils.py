import numpy as np
import pandas as pd

def parse_index(index):
    TableType = index[0]
    Subject = index[1:3]
    TableNumber = index.split('_')[0][3:6]
    letters = index.split('_')[0][6:]
    if 'PR' in [letters]:
        PR = 'PR'
        RaceIteration = letters[:-2]
    else:
        PR = ''
        RaceIteration = letters
    SubCategory = index.split('_')[1][:-1]
    EM = index[-1]
    return TableType, Subject, TableNumber, RaceIteration, PR, SubCategory, EM

def make_hierarchical(df):
    keep_cols = df.columns.values.tolist()
    df = df.loc[df.index.str.contains('_')]
    df.loc[:, 'TableType'] = np.nan
    df.loc[:, 'Subject'] = np.nan
    df.loc[:, 'TableNumber'] = np.nan
    df.loc[:, 'RaceIteration'] = np.nan
    df.loc[:, 'PR'] = np.nan
    df.loc[:, 'SubCategory'] = np.nan
    df.loc[:, 'EM'] = np.nan

    TableTypes = []
    Subjects = []
    TableNumbers = []
    RaceIterations = []
    PRs = []
    SubCategorys = []
    EMs = []

    for v in df.iterrows():
        idx = v[0]
        TableType, Subject, TableNumber, RaceIteration, PR, SubCategory, EM = parse_index(idx)
        TableTypes.append(TableType)
        Subjects.append(Subject)
        TableNumbers.append(TableNumber)
        RaceIterations.append(RaceIteration)
        PRs.append(PR)
        SubCategorys.append(SubCategory)
        EMs.append(EM)
    df['TableType'] = TableTypes
    df['Subject'] = Subjects
    df['TableNumber'] = TableNumbers
    df['RaceIteration'] = RaceIterations
    df['PR'] = PRs
    df['SubCategory'] = SubCategorys
    df['EM'] = EMs
    df = df.set_index(['TableType', 'Subject', 'TableNumber', 'RaceIteration', 'PR', 'SubCategory', 'EM'])
    #df_M = pd.DataFrame(df.values, index=[init_letters, highests, measures, letters, labels, MEs])
    #df_M.columns = df.columns
    return df[keep_cols]

def combine_index(collapse, highest, measure, letters, label, ME):
    return collaplse + highest + measure + letters + '_' + label + M
