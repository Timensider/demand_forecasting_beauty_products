# pipeline/predict.py

import joblib
import pandas as pd
import numpy as np

def predict_lgb_from_dataframe(df: pd.DataFrame, feature_cols_lgb: list, model_path: str) -> np.ndarray:
    """
    Modularized prediction function for loading model, selecting features, and predicting Units_Sold.
    """
    model = joblib.load(model_path)

    missing_cols = set(feature_cols_lgb) - set(df.columns)
    if missing_cols:
        raise ValueError(f"Missing columns in input data: {missing_cols}")

    X = df[feature_cols_lgb].copy()
    preds_log = model.predict(X)
    preds_actual = np.expm1(preds_log)
    return preds_actual


