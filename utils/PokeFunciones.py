import requests
from bs4 import BeautifulSoup
from simplejson import JSONDecodeError
import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt 
import csv 
import seaborn as sns
import re
import plotly.graph_objects as go
from plotly.offline import iplot
import plotly.express as px


def filltype(df):
    df['type2'] = df['type2'].fillna(df['type1'])
    
    
# Función para eliminar 'Generation-' y dejar solo el número romano en mayúsculas
def clean_generation(cell_value):
    # Utilizar una expresión regular para encontrar 'Generation-' seguido de números romanos
    result = re.search(r'Generation-(\w+)', cell_value)
    if result:
        return result.group(1).upper()  # Devolver el número romano en mayúsculas
    else:
        return cell_value  # Devolver el valor original si no se encuentra 'Generation-'
    
    
# Metodo para comparar atributos pokemon
def compara(df,p1, p2, c):
    comp = df[(df['name'] == p1) | (df['name'] == p2)]
    sns.barplot(x = 'name', y = c, data = comp,hue= 'name', legend=False, palette = "Set1")
    
    
def combate(df, p1, p2, p3, p4, p5):
    # Selecciona los datos de los Pokémon en el DataFrame
    x = df[df["name"] == p1]
    # Crea un gráfico polar para el primer Pokémon
    trace1 = go.Scatterpolar(
        r = [x['hp'].values[0], x['atk'].values[0], x['def'].values[0], 
             x['spatk'].values[0], x['spdef'].values[0], x['speed'].values[0], 
             x["hp"].values[0]],
        theta = ['hp', 'atk', 'def', 'spatk', 'spdef', 'speed'],
        fill = 'toself',
        name = p1
    )
    
    # Repite el proceso para los otros Pokémon
    x = df[df["name"] == p2]
    trace2 = go.Scatterpolar(
        r = [x['hp'].values[0], x['atk'].values[0], x['def'].values[0], 
             x['spatk'].values[0], x['spdef'].values[0], x['speed'].values[0], 
             x["hp"].values[0]],
        theta = ['hp', 'atk', 'def', 'spatk', 'spdef', 'speed'],
        fill = 'toself',
        name = p2
    )
    
    x = df[df["name"] == p3]
    trace3 = go.Scatterpolar(
        r = [x['hp'].values[0], x['atk'].values[0], x['def'].values[0], 
             x['spatk'].values[0], x['spdef'].values[0], x['speed'].values[0], 
             x["hp"].values[0]],
        theta = ['hp', 'atk', 'def', 'spatk', 'spdef', 'speed'],
        fill = 'toself',
        name = p3
    )
    
    x = df[df["name"] == p4]
    trace4 = go.Scatterpolar(
        r = [x['hp'].values[0], x['atk'].values[0], x['def'].values[0], 
             x['spatk'].values[0], x['spdef'].values[0], x['speed'].values[0], 
             x["hp"].values[0]],
        theta = ['hp', 'atk', 'def', 'spatk', 'spdef', 'speed'],
        fill = 'toself',
        name = p4
    )
    
    x = df[df["name"] == p5]
    trace5 = go.Scatterpolar(
        r = [x['hp'].values[0], x['atk'].values[0], x['def'].values[0], 
             x['spatk'].values[0], x['spdef'].values[0], x['speed'].values[0], 
             x["hp"].values[0]],
        theta = ['hp', 'atk', 'def', 'spatk', 'spdef', 'speed'],
        fill = 'toself',
        name = p5
    )
    
    # Configuración del layout del gráfico
    layout = go.Layout(
        xaxis=dict(domain=[0, 0.45]),
        yaxis=dict(domain=[0, 0.45]),
        xaxis2=dict(domain=[0.55, 1]),
        xaxis3=dict(domain=[0, 0.45], anchor='y3'),
        xaxis4=dict(domain=[0.55, 1], anchor='y4'),
        yaxis2=dict(domain=[0, 0.45], anchor='x2'),
        yaxis4=dict(domain=[0.55, 1], anchor='x4'),
        showlegend=True,
        title="Combate Pokémon"
    )

    # Crea el objeto figura con los datos y el layout
    data = [trace1, trace2, trace3, trace4, trace5]
    fig = go.Figure(data=data, layout=layout)

    # Muestra el gráfico
    iplot(fig, filename="Pokemon stats")