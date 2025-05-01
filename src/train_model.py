import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report
from imblearn.over_sampling import SMOTE
import joblib
import os
from pathlib import Path

# Definir la ruta base del proyecto (dos niveles arriba de este script)
BASE_DIR = Path(__file__).resolve().parent.parent

def load_and_prepare_data(relative_path="data/Supplement_Sales_Weekly_Expanded.csv"):
    # Construir la ruta absoluta al dataset
    data_file = BASE_DIR / relative_path
    if not data_file.exists():
        raise FileNotFoundError(f"El archivo de datos no se encontró en: {data_file}")

    df = pd.read_csv(data_file)

    # Crear columna binaria de devoluciones
    df["Has_Returns"] = df["Units Returned"] > 0

    # Eliminar columnas innecesarias
    df.drop(columns=["Date", "Units Returned"], inplace=True)

    # Codificar columnas categóricas
    categorical_cols = ["Product Name", "Category", "Location", "Platform"]
    label_encoders = {}
    for col in categorical_cols:
        le = LabelEncoder()
        df[col] = le.fit_transform(df[col])
        label_encoders[col] = le

    # Separar X e y
    X = df.drop(columns=["Has_Returns"])
    y = df["Has_Returns"].astype(int)

    return train_test_split(X, y, test_size=0.2, random_state=42), label_encoders


def train_model(X_train, y_train):
    smote = SMOTE(random_state=42)
    X_bal, y_bal = smote.fit_resample(X_train, y_train)

    clf = RandomForestClassifier(random_state=42)
    clf.fit(X_bal, y_bal)
    return clf


def save_model(model, encoders, output_dir="model"):
    model_dir = BASE_DIR / output_dir
    os.makedirs(model_dir, exist_ok=True)
    joblib.dump(model, model_dir / "rf_model.pkl")
    joblib.dump(encoders, model_dir / "encoders.pkl")


def main():
    (X_train, X_test, y_train, y_test), encoders = load_and_prepare_data()
    model = train_model(X_train, y_train)
    save_model(model, encoders)

    # Evaluación rápida
    y_pred = model.predict(X_test)
    print(classification_report(y_test, y_pred))


if __name__ == "__main__":
    main()
