from fastapi import FastAPI
from pydantic import BaseModel, Field
from src.predict import predict_return

app = FastAPI(title="Supplement Return Prediction API")

class SupplementInput(BaseModel):
    Product_Name: str = Field(..., alias="Product Name")
    Category: str
    Units_Sold: int = Field(..., alias="Units Sold")
    Price: float
    Revenue: float
    Discount: float
    Location: str
    Platform: str

@app.post("/predict")
def predict(input_data: SupplementInput):
    input_dict = input_data.dict(by_alias=True)
    result = predict_return(input_dict)
    return result

@app.get("/")
def read_root():
    return {"message": "API funcionando correctamente. Usa /predict para enviar datos."}
