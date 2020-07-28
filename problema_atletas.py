import pandas as pd
from math import *
from numpy import * 

print("Determinar si la diferencia de altura de las personas de dos deportes es significativamente distinta. A continuación, se debe ingresar dos nombres de deportes.")
#Entradas
deporte1 = input("Ingresa primer deporte: ").lower()
deporte2 = input("Ingresa segundo deporte: ").lower()        

#DataFrame
df = pd.read_csv("athlete_events.csv")
df['Sport'] = df['Sport'].str.lower()

#Seleccionar solo la columna de deportes
deportes = df_select['Sport'].unique()
#Ordenar alfabeticamente (por defecto, creciente)
deportes.sort()

#Verificando primer deporte
while deporte1 not in deportes:
    print('\nDeportes disponibles: {}'.format( ', '.join(deportes) ))
    deporte1 = input('\nIngresar primer deporte: ').lower()
    if deporte1 not in deportes:
        print('\nEl deporte indicado no se encuentra, elige uno de la lista')

#Verificando segundo deporte
while deporte2 not in deportes:
    print('\nDeportes disponibles: {}'.format( ', '.join(deportes) ))
    deporte2 = input('\nIngresar segundo deporte: ').lower()
    if deporte2 not in deportes:
        print('\nEl deporte indicado no se encuentra, elige uno de la lista')
        
#Copiar DataFrame para trabajar
tabla = df.copy()

#Eliminar los NaN
# tabla.replace(to_replace='?', value=nan, inplace=True)
# tabla.dropna(inplace=True)

#Seleccionar solo 3 columnas para trabajar
df_select = tabla[['Height', 'Year', 'Sport']]
#Total de años
years = sort(df_select['Year'].unique())

#Recorre todos los años, no discrimina
coincidencias = 0
for i in range(len(years)):
    #Promedios
    XA = df_select[(df_select['Sport'] == deporte1) & (df_select['Year'] == years[i])].agg({'Height': ['mean']})
    XB = df_select[(df_select['Sport'] == deporte2) & (df_select['Year'] == years[i])].agg({'Height': ['mean']})
    XA.fillna(0, inplace=True)
    XB.fillna(0, inplace=True)
    
    #Varianzas
    VA = df_select[(df_select['Sport'] == deporte1) & (df_select['Year'] == years[i])].agg({'Height': ['var']})
    VB = df_select[(df_select['Sport'] == deporte2) & (df_select['Year'] == years[i])].agg({'Height': ['var']})
    VA.fillna(0, inplace=True)
    VB.fillna(0, inplace=True)
    
    #Cantidad
    NA = df_select[(df_select['Sport'] == deporte1) & (df_select['Year'] == years[i])].agg({'Height': ['count']})
    NB = df_select[(df_select['Sport'] == deporte2) & (df_select['Year'] == years[i])].agg({'Height': ['count']})    
    NA.fillna(0, inplace=True)
    NB.fillna(0, inplace=True)

    if(XA['Height'][0]>0):
        if(XB['Height'][0]>0):
            coincidencias += 1
            D = (XA['Height'][0]-XB['Height'][0])/(math.sqrt((VA['Height'][0]/NA['Height'][0])+(VB['Height'][0]/NB['Height'][0])))
            if(D < -1.96):
                msg = 'Hay diferencia significativa'
            else:
                if(D > 1.96):
                    msg = 'Hay diferencia significativa'
                else:
                    msg = 'No hay diferencia significativa'
            print('Año: {} D: {} {}'.format(years[i], round(D,4), msg))

#En caso que no exista ninguna coincidencia
if(coincidencias==0):
   print('No hay coincidencias') 
        