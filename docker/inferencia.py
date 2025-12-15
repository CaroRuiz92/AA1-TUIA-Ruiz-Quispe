import json
import pickle
import numpy as np
import pandas as pd
import tensorflow as tf


#Modelo
model = tf.keras.models.load_model("model.h5")
print("Modelo cargado")

#Scaler
with open("scaler.pkl", "rb") as f:
    scaler = pickle.load(f)

# Carga features
with open("features.json", "r", encoding="utf-8") as f:
    features = json.load(f)
print("Features cargadas")
print(f"Cantidad de features usadas: {len(features)}")

#INPUT DUMMY
data = {feat: 0 for feat in features}
df = pd.DataFrame([data])

# Asegurar orden
df = df[features]

# Escalado

if hasattr(scaler, "transform"):
    # Caso correcto: scaler es un StandardScaler o similar
    X_scaled = scaler.transform(df)
    print("Escalado aplicado")

else:
    # Caso incorrecto: scaler es un ndarray
    X_scaled = df.values


# Predicción
prob = model.predict(X_scaled)[0][0] #primera prediccion
pred = int(prob >= 0.3280) #umbral optimizado visto en desarrollo


# Resultado
print("\nRESULTADO DE LA PREDICCIÓN")
print(f"Probabilidad de lluvia: {prob:.4f}")

if pred == 1:
    print("Predicción: LLOVERÁ")
else:
    print("Predicción: NO LLOVERÁ")
