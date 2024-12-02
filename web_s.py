

#%%writefile app.py

import streamlit as st
import requests
from streamlit_lottie import st_lottie
from PIL import Image
import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
import openai
from sklearn.linear_model import LogisticRegression



#Funcion para nuestra animacion
def load_lottieurl(url):
  r = requests.get(url)
  if r.status_code != 200:
    return None
  return r.json()

#lottie_coding = load_lottieurl("https://assets1.lottiefiles.com/packages/lf20_0yfsb3a1.json")
imagen_video = Image.open("D:\\Curso IA\\Pagina WEB Py\\im.jpg" ) #Pon la ruta de tu imagen
imagen_video1 = Image.open("D:\\Curso IA\\Pagina WEB Py\\titanic.jpg")


with st.container():

  st.image(imagen_video)




with st.container():
  st.subheader("Hola, bienvenido a nuestro proyecto")
  st.title("TITANIC")
  st.write("")
  st.write("[SOBREVIVIENTES DEL TITANIC >](https://www.youtube.com/watch?v=_Uh4VyayYKQ")



with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)

    with left_column:
        st.header("Mi objetivo")
        st.write(
            """
            Bienvenido a Titanic: ¿Sobrevivirías al hundimiento?

            Sumérgete en una experiencia interactiva única que te permite revivir uno de los desastres más famosos de la historia. En nuestra simulación, podrás experimentar el hundimiento del RMS Titanic desde la perspectiva de un pasajero.Con solo conocer algunas características, nuestro algoritmo basado en estadísticas históricas calculará tu probabilidad de supervivencia usando  modelos de Maching learning y redes neuronales.
            """
        )

    with right_column:
        st.header("My Objective")
        st.write(
            """
            Welcome to Titanic: Would You Survive the Sinking?

            Dive into a unique interactive experience that allows you to relive one of the most famous disasters in history. In our simulation, you will experience the sinking of the RMS Titanic from the perspective of a passenger. By knowing just a few characteristics, our algorithm, based on historical statistics, will calculate your probability of survival using machine learning models and neural networks.
            """
        )



   
    #st.write("[Youtube >](https://youtube.com)")
    

with st.container():
  st.write("--")
  st.header("Mis videos")
  image_column, text_column = st.columns((1, 2))
  with image_column:
    st.image(imagen_video1)
  with text_column:
    st.write(
      """
      texto aquí, escribe una descripción
      """
    )
    st.markdown("[Ver video...](https://www.youtube.com/watch?v=moOhQ0Mcg-Q&ab_channel=LesicsEspa%C3%B1ola)")

# grafica del titanic
