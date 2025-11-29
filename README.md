# Trabajo Práctico N°2 – Clasificación  
## Predicción de lluvia en Australia con Machine Learning y Redes Neuronales

Materia: Aprendizaje Automático 1
Autoras: Ruiz, Carolina y Quispe, Rocío.

Este proyecto consiste en el desarrollo completo de una solución de **clasificación binaria**
para predecir si lloverá al día siguiente en Australia (`RainTomorrow`), utilizando técnicas de
preprocesamiento, análisis exploratorio, modelos estadísticos, redes neuronales, explicabilidad
e implementación de MLOps mediante Docker.

---

## Dataset

Se utiliza el dataset `weatherAUS.csv`, que contiene observaciones meteorológicas de Australia
durante aproximadamente 10 años.

La variable objetivo es:

- `RainTomorrow`: indica si llovió al día siguiente (Yes/No).

Otras características incluyen:

- Temperatura
- Humedad
- Presión atmosférica
- Velocidad y dirección del viento
- Precipitación
- Localización geográfica

El dataset posee una columna `Location` que indica la ciudad desde la cual se realizó la medición.

---

## Desarrollo

El trabajo se estructura en las siguientes etapas:

### 1. Clustering de ciudades (regiones)
Las ciudades fueron agrupadas en regiones mediante algoritmos de clustering, utilizando latitud
y longitud. La cantidad de clusters fue definida empíricamente y visualizada mediante gráficos
geográficos para justificar la decisión.

---

### 2. Análisis exploratorio de datos

Incluye:

- Análisis estadístico de variables.
- Estudio de valores faltantes y estrategias de imputación.
- Visualizaciones:
  - Histogramas  
  - Boxplots  
  - Mapas
- Análisis de balanceo del dataset.
- Interpretación del comportamiento de cada variable.
- Estudio de correlaciones entre variables.

---

### 3. Preprocesamiento

Se realizaron las siguientes tareas:

- Imputación de valores faltantes.
- Codificación de variables categóricas.
- Escalado y estandarización de variables numéricas.
- Separación del dataset en:
  - Conjunto de entrenamiento
  - Conjunto de test y validación.

---

### 4. Modelos implementados

#### Modelos tradicionales

- Regresión logística
- Modelo base (baseline)

Se evaluaron mediante:

- Accuracy
- Precision
- Recall
- F1-score
- Matriz de confusión
- Curvas ROC
- Elección del umbral de decisión

Se analizaron falsos positivos y falsos negativos.

---

#### Optimización de modelos

Se optimizaron hiperparámetros utilizando:

- Grid Search
- Random Search
- Optuna

Se incorporó validación cruzada k-fold cuando fue pertinente.

---

#### Explicabilidad

Se utilizaron técnicas de **SHAP**:

- Interpretabilidad global:
  - Importancia de variables
  - Impacto general en la predicción
- Interpretabilidad local:
  - Explicación de una predicción individual

---

#### AutoML

Se implementó un modelo con **PyCaret** para analizar:

- Automatización del pipeline
- Selección de modelos
- Comparación de resultados con los modelos manuales

---

#### Redes neuronales

Se implementaron redes neuronales con:

- TensorFlow / Keras
- Optimización de arquitectura e hiperparámetros
- Comparación directa con la regresión logística
- Análisis del fitting

---

## Comparación de modelos

Se realizó una comparación global entre todos los modelos utilizando una métrica principal para
la selección del mejor modelo.

Se eligió el modelo final en función de:

- Desempeño en test
- Estabilidad
- Capacidad de generalización
- Interpretabilidad
- Viabilidad de despliegue

---

## MLOps – Docker

La carpeta `docker/` contiene:

- `inferencia.py`: script de inferencia
- `model.h5`: red neuronal entrenada
- `features.json`: variables del modelo
- `requirements.txt`: dependencias mínimas
- `Dockerfile`: definición de la imagen
- `README.md`: instrucciones para uso del contenedor

Para ejecutar la inferencia:

```bash
cd docker
docker build -t weather_nn .
docker run --rm weather_nn

