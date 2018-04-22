import numpy as np
import pandas as pd

def parse_index(index):
    collapse = index[0]
    highest = index[1:3]
    measure = index.split('_')[0][3:6]
    letters = index.split('_')[0][6:]
    label = index.split('_')[1][:-1]
    ME = index[-1]
    return collapse, highest, measure, letters, label, ME

def make_hierarchical(df):
    keep_cols = df.columns.values.tolist()
    df = df.loc[df.index.str.contains('_')]
    df.loc[:, 'init_letter'] = np.nan
    df.loc[:, 'highest'] = np.nan
    df.loc[:, 'measure'] = np.nan
    df.loc[:, 'letters'] = np.nan
    df.loc[:, 'label'] = np.nan
    df.loc[:, 'ME'] = np.nan

    init_letters = []
    highests = []
    measures = []
    letters = []
    labels = []
    MEs = []

    for v in df.iterrows():
        idx = v[0]
        init_letter, highest, measure, letter, label, ME = parse_variable(idx)
        init_letters.append(init_letter)
        highests.append(highest)
        measures.append(measure)
        letters.append(letter)
        labels.append(label)
        MEs.append(ME)
    df_M = pd.DataFrame(df.values, index=[init_letters, highests, measures, letters, labels, MEs])
    df_M.columns = df.columns
    return df_M[keep_cols]

def combine_index(collapse, highest, measure, letters, label, ME):
    return collaplse + highest + measure + letters + '_' + label + M
