print('Hello Streamlit')
#1. Chargement des librairies
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from sklearn.compose import make_column_selector as selector
from sklearn.preprocessing import OrdinalEncoder
from sklearn.linear_model import  Ridge
from sklearn.preprocessing import OneHotEncoder
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split
import plotly.express as px
#cd C:\Users\Admin\Desktop\bigdata
#  python test_LEVanLoi.py
# streamlit run test_LEVanLoi.py

# Demande du nom de l'utilisateur
user_name = st.text_input("👤 Entrez votre Nom et prénom :")
if user_name:
    st.success(f"Bonjour {user_name} 👋 Bienvenue dans l'application !")

st.write("Hello,world! This is a Streamlit app.")

st.title("Données sur le diabète des patients")
st.subheader("Try out the app!")
st.text("This is a simple text element")

#Choix dans une list déroulante (dans la sidebar)
graph_type = st.selectbox("Choissisez un type de graphique:",["Ligne","Barres","Aucun"])

st.write(f"Vous avez choisi le type de graphique: {graph_type}")

#5. UPLOAD CSV FILE
uploaded_file = st.file_uploader("📁 Téléchargez un fichier CSV", type=["csv"])

if uploaded_file is not None:

    #4 Dispaly panda dataframe
    import pandas as pd
    df = pd.read_csv(uploaded_file)
    st.write("Voici un aperçu de votre fichier :")
    st.dataframe(df.head())

    #5 Affichage du graphique en fonction du type choisi
    if graph_type == "Ligne":
        st.line_chart(df)
    elif graph_type == "Barres":
        st.bar_chart(df)
    else:
        st.write("Aucun graphique sélectionné.")
st.write("Merci d'avoir utilisé notre application Streamlit !")

# 7.Calcul et affichage des corrélations
st.subheader("📉 Matrice de corrélation")
corr = df.select_dtypes(include='number').corr()
st.dataframe(corr)

import numpy as np
# Checkbox
if st.checkbox("Afficher un tableau aléatoire"):
    st.write(pd.DataFrame(np.random.randn(5, 3), columns=['A', 'B', 'C']))