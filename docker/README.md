# Docker - Inferencia modelo de lluvia

Este contenedor ejecuta un modelo de red neuronal entrenado para predecir
si mañana lloverá en Australia, en base a variables meteorológicas.

El modelo fue entrenado en el notebook del proyecto utilizando datos previamente escalados.

---

## Contenido de la carpeta

- `inferencia.py` : script de inferencia
- `model.h5` : modelo entrenado (Keras/TensorFlow)
- `features.json` : lista de variables usadas por el modelo
- `scaler.pkl` : archivo auxiliar (no se utiliza en esta versión, por lo dicho antes)
- `Dockerfile` : definición de la imagen Docker
- `requirements.txt` : dependencias necesarias
- `README.md` : instrucciones de uso

---

## Construcción de la imagen

Desde la carpeta `docker/` ejecutar:

```bash
docker build -t weather_nn .
