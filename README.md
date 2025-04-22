# Supplement Return Prediction Project

Este proyecto de MLOps predice si un suplemento será devuelto o no, utilizando un modelo de Random Forest entrenado sobre un dataset de ventas semanales.

## 🔍 Objetivo

Predecir devoluciones de productos a partir de información como nombre del producto, categoría, precio, descuento, país, plataforma, etc.

## 📁 Estructura del Proyecto

```
mlops_supplements_project/
├── data/
├── notebooks/
├── src/
├── api/
├── model/
├── .github/workflows/
```

## 🚀 Cómo Ejecutar

### 1. Clonar y preparar entorno

```bash
git clone <repo_url>
cd mlops_supplements_project
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### 2. Entrenar modelo

```bash
python src/train_model.py
```

### 3. Correr la API

```bash
uvicorn api.main:app --reload
```

### 4. Usar la API

**POST** `/predict`

```json
{
  "Product Name": "Fish Oil",
  "Category": "Omega",
  "Units Sold": 150,
  "Price": 15.99,
  "Revenue": 2398.5,
  "Discount": 0.1,
  "Location": "Canada",
  "Platform": "Amazon"
}
```

## 🐳 Docker

```bash
docker build -t supplement-api .
docker run -p 8000:8000 supplement-api
```

## 🔁 Reentrenamiento y versionado

- Modelo se guarda como `model/rf_model.pkl`
- Encoders como `model/encoders.pkl`
- Se utiliza `joblib` para serialización
- Se usa `DVC` para versionar datos y modelos

## ✅ CI/CD con GitHub Actions

Archivo en `.github/workflows/ci_cd.yml`

## 🧠 Estudiantes

#Gabriel Domingues, Sebastian Martinez, Andres Uribe
Branches utilizados:

- `main`
- `develop`
- `staging`

---

**Repositorio público:** [enlace aquí]\
**Dirección del API en la nube:** [IP o DNS aquí]

