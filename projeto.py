# -*- coding: utf-8 -*-
"""Projeto.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1CzUE4_F_NJdsqdvTRTTMKurW6VhCqSTi

Primeiro Projeto
"""

import pandas as pd # Importando o Pandas

# Carregando os dados
df = pd.read_csv("KAG_conversion_data.csv")

df.head() #Retornando as 5 primeiras linhas

df.tail() # Retorna as 5 ultimas lnhas

df.columns #Retorna o nome das colunas

df.index # Retorna nº de linhas do index (começa em, termina em, passos)

df.shape # Qtd Linhas e colunas
linhas, colunas = df.shape

print(linhas)
print(colunas)

df["Clicks"] # Retorna Série para coluna Clicks
ser_clicks = df["Clicks"] 

print(ser_clicks)

df.info() # Resumo do Conjunto de Dados