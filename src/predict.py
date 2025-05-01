import joblib
import pandas as pd
import numpy as np
import os

MODEL_PATH = "model/rf_model.pkl"
ENCODERS_PATH = "model/encoders.pkl"

# Cargar modelo y encoders
model = joblib.load(MODEL_PATH)
encoders = joblib.load(ENCODERS_PATH)

def preprocess_input(data_dict):
    df = pd.DataFrame([data_dict])

    # Codificar usando los encoders guardados
    for col, encoder in encoders.items():
        if col in df:
            df[col] = encoder.transform(df[col])

    return df

def predict_return(input_dict):
    X = preprocess_input(input_dict)
    pred = model.predict(X)[0]
    prob = model.predict_proba(X)[0][1]
    return {"prediction": bool(pred), "probability_of_return": round(prob, 3)}

# Ejemplo de uso local
if __name__ == "__main__":
    sample_input = {
        "Product Name": "Fish Oil",
        "Category": "Omega",
        "Units Sold": 150,
        "Price": 15.99,
        "Revenue": 2398.5,
        "Discount": 0.1,
        "Location": "Canada",
        "Platform": "Amazon"
    }

    result = predict_return(sample_input)
    print(result)
