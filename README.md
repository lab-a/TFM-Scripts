# Segmentación de lesiones de esclerosis múltiple en resonancias magnéticas mediante Detectron2

Proyecto desarrollado como Trabajo Fin de Máster centrado en la segmentación automática de lesiones de esclerosis múltiple en imágenes de resonancia magnética mediante modelos basados en Mask R-CNN y la librería Detectron2.

El objetivo principal es estudiar el comportamiento de distintas arquitecturas, modalidades de entrada y configuraciones de entrenamiento sobre imágenes médicas multimodales, evaluando su rendimiento mediante métricas de segmentación.

---

# Vista rápida

|     Predicción y Máscara real      |
| :--------------------------------: | 
| **![ModelTest-C4-101-3x](/results/ModelTest-C4-101-3x.png)** |
| **![ModelTest-DC5-101-3x](/results/ModelTest-DC5-101-3x.png)** |
| **![ModelTest-FPN-101-3x](/results/ModelTest-FPN-101-3x.png)** |

---

# Mejores resultados obtenidos

Los siguientes GIF muestran ejemplos de inferencias realizadas por los tres modelos seleccionados como mejores candidatos tras el proceso de entrenamiento y optimización.

|            Modelo R_50_FPN            |            Modelo R_101_FPN            |            Modelo X_101_32x8d            |
| :----------------------------: | :----------------------------: | :----------------------------: |
| **![Modelo R_50_FPN](/results/R_50_FPN.gif)** | **![Modelo R_101_FPN](/results/R_101_FPN.gif)** | **![Modelo X_101_32x8d](/results/X_101_32x8d.gif)** |

---

# Descripción

El proyecto implementa un flujo completo de procesamiento y entrenamiento sobre imágenes médicas, incluyendo:

* Conversión de imágenes NIfTI a PNG.
* Generación de imágenes RGB a partir de distintas modalidades.
**![Generación Escaneos RGB](/results/RGBScan.png)**
* Procesado de máscaras y anotaciones.
* Entrenamiento mediante Detectron2.
* Validación cruzada.
* Evaluación de métricas.
* Optimización de hiperparámetros mediante algoritmos evolutivos.

---

# Pipeline seguido

```text
Imágenes MRI (.nii.gz)
        │
        ▼

Preprocesado

        │
        ▼

Conversión a PNG

        │
        ▼

Generación de imágenes RGB

        │
        ▼

Generación de máscaras y anotaciones

        │
        ▼

Entrenamiento con Detectron2

        │
        ▼

Inferencia

        │
        ▼

Evaluación de resultados
```

---

# Estructura del proyecto

```text
CodigoFuente/

├── preProcessFunctions.py      # Funciones de preprocesado
├── processMasks.py             # Procesado de máscaras
├── divisionDataset.py          # División del dataset

├── trainDetectron.py           # Entrenamiento estándar
├── trainDetectronkCV.py        # Entrenamiento con validación cruzada
├── inference.py                # Inferencia y evaluación

├── mainPreProcessDataset.py    # Pipeline de preprocesado
├── mainDivDataset.py           # División train/validación
├── mainDivDatasetkCV.py        # División para k-fold
├── mainInferencekCV.py         # Inferencia
├── mainkCrossVal.py            # Validación cruzada

├── mainAE.py                   # Algoritmo evolutivo

├── individuo.py                # Representación de individuos
├── f1evaluator.py              # Métricas de evaluación

├── posiblesConfs.yaml
├── posiblesConfsExtended.yaml
└── environmentDet.yml
```

---

# Dataset

El proyecto trabaja sobre el conjunto de datos **MSLesSeg**, utilizando las siguientes modalidades:

* FLAIR
* T1
* T2

Durante el preprocesado se generan imágenes RGB combinando dichas modalidades y las máscaras correspondientes para el entrenamiento.

---

# Entrenamiento y optimización

Durante el desarrollo del trabajo se evaluaron distintas configuraciones y arquitecturas basadas en Mask R-CNN utilizando:

* Entrenamiento estándar.
* Validación cruzada (*k-fold cross validation*).
* Búsqueda de hiperparámetros.
* Algoritmos evolutivos.
* Comparación entre modalidades.

Las configuraciones utilizadas pueden encontrarse en los distintos archivos YAML incluidos en el repositorio.

---

# Métricas utilizadas

Las métricas empleadas para evaluar el rendimiento de los modelos han sido:

* Dice Score (F1)
* Precisión
* Recall
* IoU
* mAP

---

# Entorno

El entorno necesario para ejecutar los experimentos puede reproducirse mediante:

```text
environmentDet.yml
```

---

# Autor
Alba Cano Lara.

Trabajo Fin de Máster en Ingeniería del Software e Inteligencia Artificial.

Universidad de Málaga.
