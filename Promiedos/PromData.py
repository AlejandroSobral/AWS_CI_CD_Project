import pandas as pd
import argparse
from tabulate import tabulate

equipos_copas = ['Belgrano Athletic', 'Alumni', 'Rosario Athletic', 'Quilmes Athletic Club', 
 'Club Atlético San Isidro', 'Estudiantes de Buenos Aires', 'Newells Old Boys', 
 'Racing Club', 'Rosario Central', 'River Plate', 'Independiente', 'Porteño', 'Boca Juniors', 
 'Banfield', 'Huracán', 'Tiro Federal de Rosario', 'Sportivo Barracas', 'Sportivo Balcarce', 
 'Nueva Chicago', 'Central Córdoba (R)', 'San Lorenzo de Almagro', 'San Martín de Tucumán', 
 'Estudiantes de La Plata', 'Atlanta', 'Gimnasia y Esgrima de La Plata', 'Arsenal Fútbol Club', 
 'Vélez Sarsfield', 'Lanús', 'Tigre','Club Atlético Colón']

equipos_ligas = ['Saint Andrews', 'Lomas Athletic', 'Lomas Academy', 'Belgrano Athletic', 'English High School', 'Alumni', 
                 'Quilmes', 'Porteño', 'Racing Club', 'Estudiantes de La Plata', 'Boca Juniors', 'River Plate', 'Huracán', 'Independiente', 
                 'San Lorenzo de Almagro', 'Gimnasia y Esgrima La Plata', 'Estudiantil Porteño', 'Sportivo Barracas', 'Dock Sud', 'Vélez Sarsfield', 
                 'Chacarita Juniors', 'Rosario Central', 'Newells Old Boys', 
                 'River  Plate', 'Ferro Carril Oeste', 'Argentinos Juniors', 'Lanús', 'Vélez Sarsfield', 'Bánfield', 'Arsenal F.C.']

set_copas = set(equipos_copas)
set_ligas = set(equipos_ligas)
set_equipos = set_ligas.union(set_copas)
list_equipos = list((set_equipos))

import PySimpleGUI as psg
#set the theme for the screen/window
psg.theme('SandyBeach')
#define layout

layout=[[psg.Text('Elegir equipo',size=(20, 1), font='Lucida',justification='left')],
        [psg.Combo(list_equipos,default_value='San Lorenzo de Almagro',key='equipo')],
        [psg.Button('SAVE', font=('Times New Roman',12)),psg.Button('CANCEL', font=('Times New Roman',12))]]
#Define Window
win =psg.Window('Customise your Journey',layout)
#Read  values entered by user
e,v=win.read()
#close first window
win.close()
#access the selected value in the list box and add them to a string
strx=""
for val in v:
    strx=strx+ " "+ val+","
        
#display string in a popup         
psg.popup('Equipo seleccionado :'+ v["equipo"])



#print("Información disponible para: ",list_equipos)
equipo = v["equipo"]
hasta_anio = False
desde_anio = False
show = True
# equipo = args.equipo
# desde_anio = args.desde_anio
# hasta_anio = args.hasta_anio
# show = args.show

import Ligas                                  
import CopNac
import Conmebol

tabla_conmebol = Conmebol.tabla_conmebol
tabla_ligas = Ligas.tabla_ligas
tabla_copas_nac = CopNac.tabla_copas_nac

year_list = []
data_list = []
team_list = []
type_list = []
i = 0
for element in tabla_ligas:
    if (i == 0):
        year_list.append(element)
        i = i + 1
        continue
    if(i == 1):
        data_list.append(element)
        i = i + 1
        continue
    if(i == 2):
        type_list.append(element)
        i = i + 1
        continue
    if(i == 3):
        team_list.append(element)
        i = 0
        
int_list = []
for year in year_list:
    int_list.append(int(year))
df_ligas = pd.DataFrame({"Anio": int_list,
                   "Competicion": data_list,
                   "Tipo Competición": type_list,
                  "Campeón": team_list
                    })


year_list = []
data_list = []
team_list = []
type_list = []
i = 0
for element in tabla_copas_nac:
    if (i == 0):
        year_list.append(element)
        i = i + 1
        continue
    if(i == 1):
        data_list.append(element)
        i = i + 1
        continue
    if(i == 2):
        type_list.append(element)
        i = i + 1
        continue
    if(i == 3):
        team_list.append(element)
        i = 0

int_list = []
for year in year_list:
    int_list.append(int(year))
df_cop_nac = pd.DataFrame({"Anio": int_list,
                   "Competicion": data_list,
                   "Tipo Competición": type_list,
                  "Campeón": team_list
                    })

year_list = []
data_list = []
team_list = []
i = 0
for element in tabla_conmebol:
    if (i == 0):
        year_list.append(element)
        i = i + 1
        continue
    if(i == 1):
        data_list.append(element)
        i = i + 1
        continue
    if(i == 2):
        team_list.append(element)
        i = 0

int_list = []
for year in year_list:
    int_list.append(int(year))
df_conmebol = pd.DataFrame({"Anio": int_list,
                   "Competicion": data_list,
                  "Campeón": team_list
                    })

total_titulos = 0
titulos_amateurs = 0
titulos_profesionales = 0
titulos_conmebol = 0


if(equipo):
    ## CONMEBOL
    rslt_df = df_conmebol[df_conmebol["Campeón"] == equipo]
    #print("Copas Nacionales\n", rslt_df)
    camps_list = rslt_df["Campeón"].unique()
    for camp in camps_list:
        rslt_df_2 = rslt_df[rslt_df["Campeón"] == camp]

        
        if (len(rslt_df_2)>0):
            print("----------------")
            print("El equipo", camp, "ganó",len(rslt_df_2), "Copas Conmebol")
            titulos_conmebol = len(rslt_df_2)
            total_titulos = len(rslt_df_2) + total_titulos
            if(show):
                print("----------------")
                print(tabulate(rslt_df_2, headers='keys', tablefmt='psql'))
                #psg.popup(tabulate(rslt_df_2, headers='keys', tablefmt='psql'))
    ## COPAS NACIONALES
    rslt_df = df_cop_nac[df_cop_nac["Campeón"] == equipo]
    #print("Copas Nacionales\n", rslt_df)
    camps_list = rslt_df["Campeón"].unique()
    for camp in camps_list:
        rslt_df_2 = rslt_df[rslt_df["Campeón"] == camp]
        if (len(rslt_df_2)>0):
            titulos_amateurs = len(rslt_df[rslt_df["Tipo Competición"] == "Amateur"])
            titulos_profesionales = len(rslt_df[rslt_df["Tipo Competición"] == "Profesional"]) 
            print("----------------")
            print("El equipo", camp, "ganó",len(rslt_df_2), "Copas Nacionales")
            total_titulos = len(rslt_df_2) + total_titulos
            if(show):
                print("----------------")
                print(tabulate(rslt_df_2, headers='keys', tablefmt='psql'))
                #psg.popup(tabulate(rslt_df_2, headers='keys', tablefmt='psql'))
    ## LIGAS LOCALES
    rslt_df = df_ligas[df_ligas["Campeón"] == equipo]
    #print("Ligas Locales\n", rslt_df)
    camps_list = rslt_df["Campeón"].unique()
    for camp in camps_list:
        titulos_amateurs = len(rslt_df[rslt_df["Tipo Competición"] == "Amateur"]) + titulos_amateurs
        titulos_profesionales = len(rslt_df[rslt_df["Tipo Competición"] == "Profesional"]) + titulos_profesionales
        rslt_df_2 = rslt_df[rslt_df["Campeón"] == camp]
        if (len(rslt_df_2)>0):
            print("El equipo", camp, "ganó",len(rslt_df_2), "Ligas Locales")
            total_titulos = len(rslt_df_2) + total_titulos
            if(show):
                print("----------------")
                print(tabulate(rslt_df_2, headers='keys', tablefmt='psql'))
                #psg.popup(tabulate(rslt_df_2, headers='keys', tablefmt='psql'))
print("\n")
print("----------------")

resultados_obj = {
    "Total títulos Amateurs": titulos_amateurs,
    "Total títulos Profesionales": titulos_profesionales,
    "Total títulos Conmebol": titulos_conmebol,
    "Total títulos": total_titulos
}
import json

#df_resultados_prety = pd.DataFrame(resultados_obj)
#print(df_resultados_prety)
input("")                