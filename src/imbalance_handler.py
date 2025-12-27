from imblearn.over_sampling import SMOTE
from collections import Counter

class ImbalanceHandler:
    def apply_smote(self, X, y):
        print("Before SMOTE:", Counter(y))
        smote = SMOTE(random_state=42)
        X_res, y_res = smote.fit_resample(X, y)
        print("After SMOTE:", Counter(y_res))
        return X_res, y_res
