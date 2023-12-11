# transformers.py

import pandas as pd
from sklearn.base import BaseEstimator, TransformerMixin


def cabin_transformer(cabin):
    if pd.isna(cabin) or cabin == '':
        return 0
    return ord(cabin[0]) - ord('A') + 1


class CabinToNumber(BaseEstimator, TransformerMixin):
    def fit(self, X, y=None):
        return self

    def transform(self, X, y=None):
        X = pd.DataFrame(X)
        X['Cabin'] = X['Cabin'].apply(cabin_transformer)
        return X
