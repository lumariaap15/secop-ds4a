import pandas as pd
import seaborn as sns
import numpy as np
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
import pickle
import joblib

drop = ['NormalizedDelay','Unnamed: 0', 'Nombre Entidad','Dias Adicionados', 
        'Fecha de Inicio del Contrato', 'Fecha de Fin del Contrato']

df = pd.read_csv('assets/csv/SECOP_Electronicos_Cleaned.csv').drop(drop, axis=1)

cat_cols = ['Departamento', 'Orden', 'Sector', 'Rama','Entidad Centralizada', 'Estado Contrato', 'Tipo de Contrato', 'Modalidad de Contratacion',
            'Es Grupo','Es Pyme', 'Destino Gasto', 'EsPostConflicto','Obligaciones Postconsumo','Obligación Ambiental', 'Delay']
cat_values = {key:'category' for key in cat_cols}

df = df.astype(cat_values)