import streamlit as st
import json
import pandas as pd
import numpy as np
import streamlit as st

st.image('/Users/herminiapadialromera/ironhackb/Proyecto_final/Images/logo.png', use_column_width='always')

st.title(":blue[Sistema de recomendación de cursos]")

#funciones
def lectura_input(path): 
    pd.set_option('display.max_colwidth', None)
    df_input_json = pd.read_json(path)
    columnas_explode = ['Etapa', 'Formato', 'Temática', 'Objetivos'] 
    df_input_json_merge = df_input_json.explode(['Etapa']).explode(['Formato']).explode(['Objetivos']).explode(['Temática'])
    return df_input_json_merge  #DF1

def lectura_cursos():
    data_course_df = pd.read_csv('/Users/herminiapadialromera/ironhackb/Proyecto_final/data/Datos_ampliados.csv', sep=";", encoding='utf8')
    data_course_df = pd.DataFrame(data_course_df)
    data_course_df['Tipo de contenido'].fillna('No innovador', inplace=True)
    columnas_explode_curso = ['Etapa', 'Formato', 'Temática', 'Objetivos'] 
    data_course_df = data_course_df.explode(['Etapa']).explode(['Formato']).explode(['Temática'])
    return data_course_df #DF2

def merge(df_input_json_merge, data_course_df):
    df_merge = pd.merge(df_input_json_merge, data_course_df, on=['Provincia', 'Etapa', 'Formato', 'Temática'])
    df_merge = df_merge.iloc[:, 1:]
    return df_merge  #DF FINAL

def lectura_datos(path):
   
    df_input_json_merge = lectura_input(path)  # Llamada a la función lectura_input
    data_course_df = lectura_cursos()  # Llamada a la función lectura_cursos
    prueba_lectura = merge(df_input_json_merge, data_course_df)  # Llamada a la función merge

    return prueba_lectura

##SR1

def filtro_tematica_etapa_formato(df_merge, sesiones):
    tematica_unique_list = df_merge['Temática'].unique()
    formato_unique_list = df_merge['Formato'].unique()
    etapa_unique_list = df_merge['Etapa'].unique()

    filtro_tematica_df = pd.DataFrame()
    for tematica in tematica_unique_list:
        df_tematica_temp = df_merge[(df_merge['Nº Sesiones'] <= int(f"{sesiones}")) & (df_merge['Temática'] == tematica)].iloc[:1,:]
        filtro_tematica_df = pd.concat([filtro_tematica_df, df_tematica_temp])
        #print("filtro_tematica_df ---> ", tematica)
        #display(filtro_tematica_df)

    filtro_formato_df = pd.DataFrame()
    for formato in formato_unique_list:
        df_formato = df_merge[(df_merge['Nº Sesiones'] <= int(f"{sesiones}")) & (df_merge['Formato'] == formato)].iloc[:1,:]
        filtro_formato_df = pd.concat([filtro_formato_df, df_formato])
        #print("filtro_formato_df ---> ", formato)
        #display(filtro_formato_df)

    filtro_etapa_df = pd.DataFrame()
    for etapa in etapa_unique_list:
        df_etapa = df_merge[(df_merge['Nº Sesiones'] <= int(f"{sesiones}")) & (df_merge['Etapa'] == etapa)].iloc[:1,:]
        filtro_etapa_df = pd.concat([filtro_etapa_df, df_etapa])
        #print("filtro_etapa_df ---> ", etapa)
        #display(filtro_etapa_df)

    recomendaciones_df = pd.concat([filtro_tematica_df,filtro_formato_df,filtro_etapa_df]).drop_duplicates().reset_index(drop=True)

    return recomendaciones_df

def filtro_precio(tematica_formato_etapa_df):
    if (tematica_formato_etapa_df['Precios por taller'] == 'Menos de 100').any():
        precio_df = tematica_formato_etapa_df[(tematica_formato_etapa_df['Precio por taller'] < 100)]
        print("menos de 100 ---> existe")

    elif (tematica_formato_etapa_df['Precios por taller'] == 'Entre 100 y 300').any():
        precio_df = tematica_formato_etapa_df[(tematica_formato_etapa_df['Precio por taller'] >= 100) & (tematica_formato_etapa_df['Precio por taller'] <= 300)]
        print("entre 100 y 300 ---> existe")

    else:
        precio_df = tematica_formato_etapa_df[(tematica_formato_etapa_df['Precio por taller'] > 300)]
        print("más de 300 ---> existe")
    precio_df= precio_df.reset_index(drop=True)
    
    return precio_df

##SR2
def filtro_valoracion_tematica(df_merge, sesiones):
    tematica_unique_list = df_merge['Temática'].unique()

    filtro_tematica_df = pd.DataFrame()
    for tematica in tematica_unique_list:
        df_tematica= df_merge[(df_merge['Nº Sesiones'] <= int(sesiones)) & (df_merge['Temática'] == tematica)].sort_values(by='Valoración', ascending=False).reset_index(drop=True)
        filtro_tematica_df = pd.concat([filtro_tematica_df, df_tematica.head(2)])
        #print("filtro_tematica_df ---> ", tematica)
    
    recomendaciones_valoracion_tema_df = filtro_tematica_df.drop_duplicates()

    return recomendaciones_valoracion_tema_df

##SR3
def filtro_innovación_tematica (df_merge, sesiones):
    tematica_unique_list = df_merge['Temática'].unique()

    filtro_inno_tematica_df = pd.DataFrame()
    for tematica in tematica_unique_list:
        df_inno_tematica = df_merge[(df_merge['Nº Sesiones'] <= int(f"{sesiones}")) & (df_merge['Tipo de contenido'] == 'Innovador') & (df_merge['Temática'] == tematica)]
        filtro_inno_tematica_df = pd.concat([filtro_inno_tematica_df, df_inno_tematica.head(2)])
        #print("filtro_inno_tematica_df ---> ", tematica)

    recomendaciones_innovacion_tema_df = filtro_inno_tematica_df.drop_duplicates().reset_index(drop=True)

    return recomendaciones_innovacion_tema_df

##SR4
def check_educ_creci():
    path = '/Users/herminiapadialromera/ironhackb/Proyecto_final/notebooks/input_sist_recom_4.json'
    pd.set_option('display.max_colwidth', None)
    df_input_json = pd.read_json(path)
    
    if df_input_json['Temática'].str.contains('Educación & Crecimiento').any():
        pass
    
    else:
        df_input_json['Temática'][0].append('Educación & Crecimiento')
        print("Se agregó 'Educación & Crecimiento' a df_input_json['Temática']")
        columnas_explode = ['Etapa', 'Formato', 'Temática', 'Objetivos'] 
        df_input_json_merge = df_input_json.explode(['Etapa']).explode(['Formato']).explode(['Objetivos']).explode(['Temática'])
        data_course_df = lectura_cursos()  # Llamada a la función lectura_cursos
        prueba_lectura = merge(df_input_json_merge, data_course_df)  # Llamada a la función merge
        
        return prueba_lectura
    
def filtro_edcrecim_tematica (df_merge, sesiones):
    tematica_unique_list = df_merge['Temática'].unique()

    filtro_crecim_tematica_df = pd.DataFrame()
    for tematica in tematica_unique_list:
        df_crecim_tematica = df_merge[(df_merge['Nº Sesiones'] <= int(f"{sesiones}")) & (df_merge['Temática'] == tematica)]
        filtro_crecim_tematica_df = pd.concat([filtro_crecim_tematica_df, df_crecim_tematica.head(1)])

    recomendaciones_filtro_crecim_tematica_df = filtro_crecim_tematica_df.drop_duplicates().reset_index(drop=True)

    return recomendaciones_filtro_crecim_tematica_df

##FUNCIÓN OBJETIVO
def objetivo_analisis(lectura):
    #objetivos = ['Ofrecer formación variada', 'Aumentar la participación de las familias', 'Sorprender con contenidos innovadores y formatos novedosos']
    path = '/Users/herminiapadialromera/ironhackb/Proyecto_final/notebooks/input_sist_recom_4.json'
    pd.set_option('display.max_colwidth', None)
    df_input_json = pd.read_json(path)
    
    print("Contenido de lectura['Objetivos']:")
    #print(lectura['Objetivos'])
    ob1= 'Ofrecer formación variada'
    ob2= 'Aumentar la participación de las familias'
    ob3= 'Sorprender con contenidos innovadores y formatos novedosos'

    if lectura['Objetivos'].str.contains(ob1).any():

        print("Condición de objetivos cumplida:")
        tematica_formato_etapa_df_test = filtro_tematica_etapa_formato(lectura, 5)
        filtro_precio_df = filtro_precio(tematica_formato_etapa_df_test)
        return filtro_precio_df
    
    elif lectura['Objetivos'].str.contains(ob2).any():
        print("Está el 2")
        filtro_valoracion_tematica_df = filtro_valoracion_tematica(lectura, 5)
        return filtro_valoracion_tematica_df
    
    elif lectura['Objetivos'].str.contains(ob3).any():
        print("Nada 2") 
        filtro_innovación_tematica_df = filtro_innovación_tematica(lectura, 5)
        return filtro_innovación_tematica_df 

    else:
        #resultado_check_educ_creci = check_educ_creci()
        df_sr4 = check_educ_creci()
        return filtro_edcrecim_tematica(df_sr4, 5)
if __name__ == '__main__':

    #sr = input("Seleccione Sistema de Recomendación (1, 2, 3 o 4): ")
    objetivo = st.radio('**:red[Nuestra recomendación siempre parte del objetivo seleccionado por cliente]:**', ('Ofrecer formación variada', 'Aumentar la participación de las familias', 'Sorprender con contenidos innovadores y formatos novedosos', 'Solucionar problemas de comunicacion y actitud de niños y familias'))

    if objetivo == 'Ofrecer formación variada':
        path_de_lectura = '/Users/herminiapadialromera/ironhackb/Proyecto_final/notebooks/input_.json'
        lectura = lectura_datos(path=path_de_lectura)
        resultado = filtro_tematica_etapa_formato(lectura, 5)
    elif objetivo == 'Aumentar la participación de las familias':
        path_de_lectura = '/Users/herminiapadialromera/ironhackb/Proyecto_final/notebooks/input_sist_recom_2.json'
        lectura = lectura_datos(path=path_de_lectura)
        resultado = filtro_valoracion_tematica(lectura, 5)
    elif objetivo == 'Sorprender con contenidos innovadores y formatos novedosos':
        path_de_lectura = '/Users/herminiapadialromera/ironhackb/Proyecto_final/notebooks/input_sist_recom_3.json'
        lectura = lectura_datos(path=path_de_lectura)
        resultado = filtro_innovación_tematica(lectura, 5)
    else:
        path_de_lectura = '/Users/herminiapadialromera/ironhackb/Proyecto_final/notebooks/input_sist_recom_4.json'
        lectura = lectura_datos(path=path_de_lectura)
        resultado = filtro_edcrecim_tematica(lectura, 5)

    
    st.write(':red[A partir del cuestionario de cliente, internamente generamos un Data Frame con todas las posibles opciones según sus preferencias:]')
    df_input_json_merge = lectura_input(path = path_de_lectura)  # Llamada a la función lectura_input
    
    st.dataframe(df_input_json_merge)    #imprimo el df con las opciones de cliente
    
    data_course_df = lectura_cursos()  # Llamada a la función lectura_cursos
    prueba_lectura = merge(df_input_json_merge, data_course_df)  # Llamada a la función merge
    lectura = lectura_datos(path = path_de_lectura)   # Llamada a la función lectura_datos
    tematica_formato_etapa_df_test = filtro_tematica_etapa_formato(lectura, 5) ## Llamada a filtro_tematica_etapa_formato
    filtro_precio_df = filtro_precio(tematica_formato_etapa_df_test) ## LLamada a filtro_precio
    filtro_valoracion_tematica_df = filtro_valoracion_tematica(lectura, 5) ## Llamada a filtro_valoracion_tematica
    filtro_innovación_tematica_df = filtro_innovación_tematica(lectura, 5) ## Llamada a filtro_innovación_tematica
    df_sr4 = check_educ_creci() ## Llamada a check_educ_creci
    filtro_edcrecim_tematica(df_sr4, 5) ## Llamada a filtro_edcrecim_tematica
    resultado = objetivo_analisis(lectura) ##Llamada a objetivo_analisis
    print(resultado)
    
    #Streamlit
    
    st.write('En relación al objetivo seleccionado y teniendo en cuenta el resto de criterios previamente seleccionados, le proponemos la siguiente recomendación:')

    st.dataframe(resultado[['Título','Formato','Etapa','Temática', 'Nº Sesiones']])    #imprimo el df resultado

st.subheader(':book: :blue[Descarga tu recomendación]')

@st.cache_data
def convert_df(df):
    return df.to_csv(index=False).encode('utf-8')

recomend = pd.DataFrame(resultado)  

csv = convert_df(recomend)

st.download_button(
    "Download",
    csv,
    "recomendacion.csv",
    "text/csv",
    key='download-csv'
)

st.subheader('Si necesitas más información, te animamos a visitar nuestra web')
link = 'https://schoolandfamily.es/'
st.markdown(link, unsafe_allow_html=True)