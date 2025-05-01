import streamlit as st
import requests

st.set_page_config(page_title="Predicción de Devoluciones", page_icon="📦")

st.title("📦 Predicción de Devoluciones de Producto")

st.markdown("Complete la información del producto para predecir si será devuelto.")

product = st.text_input("Nombre del producto")
category = st.selectbox("Categoría", ["Omega", "Vitamin", "Protein", "Other"])
units = st.number_input("Unidades vendidas", min_value=0, step=1)
price = st.number_input("Precio", step=0.01)
revenue = st.number_input("Ingresos", step=0.01)
discount = st.slider("Descuento aplicado", 0.0, 1.0, 0.01)
location = st.selectbox("Ubicación", ["USA", "Canada", "Mexico"])
platform = st.selectbox("Plataforma", ["Amazon", "eBay", "Shopify"])

if st.button("🔍 Predecir"):
    data = {
        "Product_Name": product,
        "Category": category,
        "Units_Sold": units,
        "Price": price,
        "Revenue": revenue,
        "Discount": discount,
        "Location": location,
        "Platform": platform
    }

    headers = {"Content-Type": "application/json"}

    try:
        response = requests.post("http://localhost:8000/predict", json=data, headers=headers)
        if response.status_code == 200:
            result = response.json()
            st.success(f"🔮 Resultado: {'Será devuelto' if result['prediction'] else 'No será devuelto'}")
            st.write(f"📊 Probabilidad de devolución: {round(result['probability_of_return'] * 100, 2)}%")
        else:
            st.error(f"❌ Error en la respuesta de la API: {response.status_code}")
    except Exception as e:
        st.error(f"❌ Error al conectarse con la API: {e}")
