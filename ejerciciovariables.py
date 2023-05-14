# Librerías que usaré para el proyecto owo
import pandas as pd
import ipywidgets as widgets
from IPython.display import display
import matplotlib.pyplot as plt
import numpy as np


df = pd.read_csv('random_data.csv')

def create_plot(item, importance_edad, importance_peso, importance_altura, importance_velocidad):
    
    total_importance = importance_edad + importance_peso + importance_altura + importance_velocidad #Importancia total
    
    rel_importance_edad = importance_edad / total_importance
    rel_importance_peso = importance_peso / total_importance
    rel_importance_altura = importance_altura / total_importance
    rel_importance_velocidad = importance_velocidad / total_importance

    item_data = df[df['Nombre'] == item].iloc[0]
    
    plt.bar(['Edad', 'Peso', 'Altura', 'Velocidad'], [item_data['Edad'] * rel_importance_edad,
                                                      item_data['Peso'] * rel_importance_peso,
                                                      item_data['Altura'] * rel_importance_altura,
                                                      item_data['Velocidad'] * rel_importance_velocidad])
    
    plt.show()

edad_slider = widgets.FloatSlider(min=0, max=1, step=0.01, value=0.25, description='Edad')
peso_slider = widgets.FloatSlider(min=0, max=1, step=0.01, value=0.25, description='Peso')
altura_slider = widgets.FloatSlider(min=0, max=1, step=0.01, value=0.25, description='Altura')
velocidad_slider = widgets.FloatSlider(min=0, max=1, step=0.01, value=0.25, description='Velocidad')

item_selector = widgets.Dropdown(options=list(df['Nombre']), description='Selecciona un ítem:')


def on_value_change(change):

    item = item_selector.value
    importance_edad = edad_slider.value
    importance_peso = peso_slider.value
    importance_altura = altura_slider.value
    importance_velocidad = velocidad_slider.value
    

    create_plot(item,importance_edad, importance_peso, importance_altura, importance_velocidad)


item_selector.observe(on_value_change, names='value')
edad_slider.observe(on_value_change, names='value')
peso_slider.observe(on_value_change, names='value')
altura_slider.observe(on_value_change, names='value')
velocidad_slider.observe(on_value_change, names='value')

# Mostrar los elementos de interacción
display(item_selector)
display(edad_slider)
display(peso_slider)
display(altura_slider)
display(velocidad_slider)