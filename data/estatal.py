#import gspread as gs
import pandas as pd
import plotly.express as px

#Lectura de base de datos estatal
estatal = pd.read_csv('data/datos_estatales.csv', encoding='latin', sep=';')


# Limpiamos y homogeneziamos los datos

estatal = estatal.dropna(axis=1, how='all')
estatal = estatal.dropna(axis=0, how='all')
estatal['FEMINICIDIOS'] = estatal['FEMINICIDIOS'].fillna(0).astype(int)
estatal['Fecha'] = pd.to_datetime(estatal[[ 'day', 'month', 'year']])
estatal['Fecha_NUEVA'] = estatal['Fecha'].dt.strftime('%d-%m-%Y').fillna("-")
estatal['TIPO DE RECURSO'] = estatal['TIPO DE FUENTE'].replace({'AGENTE ESTATAL': 'Escuelas'})

cols = ['PAIS', 'ESTADO', 'FUENTE','TIPO DE FUENTE']
for i in cols:
    estatal[i] = estatal[i].str.title()


paises_estatales =  estatal['PAIS'].unique()

anos_estatal = estatal['PERIODO'].unique()
