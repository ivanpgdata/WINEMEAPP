import streamlit as st
from streamlit_option_menu import option_menu
from funciones_sistema_recomendacion_vinos import *
import requests

# data = "WineMeApp/df_vinos_modelos.csv"
data = pd.read_csv('WineMeApp_ENG/df_vinos_modelos.csv')


# Tab Info
st.set_page_config(
	page_title = "WineMeApp!",
    page_icon=":wine_glass:",
    layout="wide")
# ------------------------------------------------

# Importar imagen desde GDrive
file_id = "1FUeYXfNwHDSxVzn3HsctD8b7oQU4fXPz"
url = f"https://drive.google.com/uc?export=view&id={file_id}"
response = requests.get(url)
st.image(response.content)

# -----------------------


selected = option_menu(
	menu_title = None,
	options = ["Home", "WineMeApp!", "Resources", "About Us"],
	icons = ['house-door', "menu-button-wide-fill","journals", "person lines fill"],
	menu_icon = "",
	orientation = "horizontal",
	styles={
    "container": {"padding": "0!important", "background-color": "#FFFFFF"},
    "icon": {"color": "black", "font-size": "30px"},
    "nav-link": {"font-size": "20px", "text-align": "left","font-family": 'Cooper Black',"color": "black", "margin":"0px", "--hover-color": "#0000"},
    "nav-link-selected": {"background-color": "#e51133"},
})
if selected =="Home":
    st.markdown(""" <style> .font {
            font-size:35px ; font-family: 'Cooper Black'; color: #FFFFF;} 
            </style> """, unsafe_allow_html=True)
    st.markdown('<p class="font">Introducción</p>', unsafe_allow_html=True)
    col1, col2, col3= st.columns([0.5, 0.3, 0.2])
    with col1:  # To display the header text using css style
        st.write("Introducing a wine recommendation engine that goes beyond the conventional!")
        st.write(
            "Forget about suggestions based solely on the type of wine. Our innovative system analyzes your preferences and needs,"
            " using detailed tasting notes and pairing recommendations to find the perfect option for every occasion.")
        st.markdown(""" <style> .font {
                    font-size:35px ; font-family: 'Cooper Black'; color: #FFFFF;} 
                    </style> """, unsafe_allow_html=True)
        st.markdown('<p class="font">What makes us different?</p>', unsafe_allow_html=True)
        st.markdown(
            "* **Personalized recommendations:** Adjust the importance of price and rating to find wines that fit your budget and taste.")
        st.markdown(
            "* **Beyond stereotypes:** We don't limit you to just one type of wine. Discover new favorites, from smooth reds to crisp whites or sparkling.")
        st.markdown(
            "* **Expertly curated data:** Our recommendations are based on extensive tasting notes and pairing, ensuring you find wines you'll truly enjoy.")
        st.markdown(
            "* **Say goodbye to average wine experiences.** Let our engine guide you towards new discoveries and unforgettable moments.")
        st.markdown("##### Wanna know more about WineMeApp?")
    with col2:
        st.write("")
        # Importar imagen desde GDrive
        file_id = "1ncIfBeSzk-BaKjU2gaM037-L_kCF8_cf"
        url = f"https://drive.google.com/uc?export=view&id={file_id}"
        response = requests.get(url)
        st.image(response.content)

    st.markdown(""" <style> .font {
            font-size:35px ; font-family: 'Cooper Black'; color: #FFFFF;} 
            </style> """, unsafe_allow_html=True)
    st.markdown('<p class="font">Motivación</p>', unsafe_allow_html=True)
    st.write(
        "Many of us have found ourselves in the awkward situation of not knowing what wine to order at a restaurant or when buying"
        " from a specialized store. Often, we end up opting for the same old thing or what someone else orders, without exploring the wide"
        " range of options available.")

    st.write(
        'These are the moments when a wine recommendation system, whether in the wine section of large department stores or gourmet supermarkets,'
        ' or when ordering drinks at a restaurant, would be extremely useful. And it is precisely here where our '
        'recommender <span style="color: #E51133; font-weight: bold;">WineMeApp!</span> comes into play!',
        unsafe_allow_html=True)

    st.write(
        "As part of the team, during our experience as expatriates in the United Kingdom, we noticed that Chardonnay white wines were a particularly"
        " recurrent choice. While this variety is popular, "
        "we were surprised that the diverse options offered by the world of wine were not explored, including Spanish wines from regions such"
        " as Jerez de la Frontera (Palomino, Pedro Ximénez, Tintilla de Rota) or Zamora"
        " (Malvasía Castellana, Moscatel de Grano Menudo, Verdejo).")
    st.write(
        'That is why we have developed <span style="color: #E51133; font-weight: bold;">WineMeApp!</span>, a recommendation engine that'
        ' helps you choose the perfect wine for every occasion. By considering your preferences,'
        ' the type of food, and the occasion, <span style="color: #E51133; font-weight: bold;">WineMeApp!</span> provides you with'
        ' personalized recommendations so you can discover new wines and fully enjoy each experience.',
        unsafe_allow_html=True)

    st.markdown(""" <style> .font {
            font-size:35px ; font-family: 'Cooper Black'; color: #FFFFF;} 
            </style> """, unsafe_allow_html=True)
    st.markdown('<p class="font">Goal</p>', unsafe_allow_html=True)
    st.write(
        "The project uses a hybrid machine learning model to recommend wines based on user preferences regarding tasting notes and pairing."
        " The user inputs the "
        "name of the wine, checks its availability in the database, and then sets a price range and the importance of price and wine rating to"
        " get personalized recommendations.")

# -----------------------------------------------------------------------------

if selected =="WineMeApp!":
    st.markdown("# Recommendation Model")
    st.write(
        "The recommendation model created in this project is a hybrid model that combines two powerful approaches.")

    st.markdown("## :wine_glass: Model 1: Tasting Notes and Pairing Recommender")
    st.write("First, we implemented a recommendation system based on tasting notes"
             " and pairing using Natural Language Processing (NLP).")
    st.write("When entering a wine to search for similar recommendations, the system looks for wines with"
             " greater semantic similarity, applying cosine similarity, in the tasting notes and pairing,"
             " providing a ranking of the top 10 most similar wines.")

    # ---- BUSQUEDA EN LA LISTA DE 4K VINOS ----
    st.markdown("#### Step 1: Check if your favorite wine is in our database")
    texto_busqueda = st.text_input(' ')
    if st.button("Find your wine in our database 🔎 "):  # Si se pulsa el botón
        st.markdown(" ##### Results found in our database: ")
        st.dataframe(buscar_vino(data, texto_busqueda, embeddings2))

    # ----- RECOMENDATOR ----
    st.markdown("#### Step 2: Copy and paste the name of the wine for which you want to search for recommendations")
    nombre_vino = st.text_input("")
    if st.button("Recommend me a wine 🍀 "):  # Si se pulsa el botón
        st.markdown(f" ##### These are the wines we recommend for *{nombre_vino}* ")
    recomendaciones = recomendar_vino(data, nombre_vino, embeddings2)
    st.dataframe(recomendaciones)

    # ---- TOPSIS ----
    st.markdown("##  :wine_glass::wine_glass: Model 2: TOPSIS")
    st.write(
        "The current version of WineMeApp! has default filtering of wines with prices ranging from 5 to 150 euros"
        " and weights assigned to the price (80%) and rating (20%) variables.")

    st.markdown("##### Step 3: Check your recommendation with the TOPSIS* model")

    vinos = filtrar_por_precio(recomendaciones, precio_min, precio_max)

    if st.button("Topsis :tada:"):  # Si se pulsa el botón
        st.write(topsis_general(recomendaciones, nombre_vino))
    # ------



# -----------------------------------------------------------------------------
if selected =="Resources":
    col1, col2, col3, col4, col5 = st.columns([0.20, 0.20, 0.20, 0.20, 0.20])
    with col1:
        st.markdown("##  Websites ")
        st.markdown(" * **Vinetur** ")
        st.markdown(" * **Vinissimus** ")
        st.markdown(" * **Bodeboca** ")
        st.markdown(" * **OEMV** ")
    with col2:
        st.header(" ")
        st.write(" ")
        st.write(" ")
        st.write(" ")
        st.write("""[www.vinetur.com](https://www.vinetur.com/)""")
        st.write("""[www.vinissimus.com/](https://www.vinissimus.com/es/)""")
        st.write("""[www.bodeboca.com](https://www.bodeboca.com/)""")
        st.write("""[www.oemv.es](https://www.oemv.es/)""")

    with col3:
        st.markdown("##  Libraries  ")
        st.markdown(" * Pandas")
        st.markdown(" * Numpy")
        st.markdown(" * Seaborn")
        st.markdown(" * Matplotlib")
    with col4:
        st.markdown(" ")
        st.write(" ")
        st.write(" ")
        st.write(" ")
        st.markdown(" * Sklearn")
        st.markdown(" * TensorFlow")
        st.markdown(" * Plotly")
        st.markdown(" * Scipy")
    st.write("----")

# -----------------------------------------------------------------------------
if selected == "About Us":
    col1, col2, col3 = st.columns([0.3, 0.3, 0.3])
    with col1:  # To display the header text using css style
        with st.container():
            # Importar imagen desde GDrive
            file_maria_id = "1sCRq07Z-kYc8bGhZOAtBj_UyqSe7ZogQ"
            url_pic_maria = f"https://drive.google.com/uc?export=view&id={file_maria_id}"
            response_maria = requests.get(url_pic_maria)
            st.image(response_maria.content)
            st.markdown(
                """ #### María Pérez Sebastián :computer:""")
            st.write("""
            Currently, I'm making a career shift by training as a Data Scientist.
            """)
            st.write("""
            Previously, I've dedicated almost 10 years to the comprehensive development of architectural projects.
             I consider myself a responsible, committed person with a high capacity for work. I enjoy working in teams,
              contributing personal ideas, and learning from the positive work methods of other team members.
            """)

            st.write("""[Github](https://github.com/marpezseb),
                 [LinkedIn](https://www.linkedin.com/in/-mps2024/) """)
    with col2:
        # Importar imagen desde GDrive

        file_ivan_id = "1s0koO8Ug2J-7nhTvdMQTIKCZZpfaMfq6"
        url_pic_ivan = f"https://drive.google.com/uc?export=view&id={file_ivan_id}"
        response_ivan = requests.get(url_pic_ivan)
        st.image(response_ivan.content)
        st.markdown(
            """
            #### Iván Pinto Grilo :computer:
            """)
        st.write("""Naturally curious, data rookie, and restless mind.""")
        st.write("""I've decided to redirect my career towards data science through a Data Science and Machine Learning Bootcamp. 
        With international experience in positions of responsibility where I've seen the importance of data.
        """)
        st.write("""Always with some project in mind.""")
        st.write(""" [Github ](https://github.com/ivanpgdata), 
            [LinkedIn](https://www.linkedin.com/in/ivanpgdata/) """)
    with col3:
        # Importar imagen desde GDrive
        file_soraya_id = "1rzJvRfXgB61WgJloyBSYFRtUnirBW2j8"
        url_pic_soraya = f"https://drive.google.com/uc?export=view&id={file_soraya_id}"
        response_soraya = requests.get(url_pic_soraya)
        st.image(response_soraya.content)
        st.markdown(
            """
            #### Soraya Alvarez Codesal  :computer:""")
        st.write("""
        Data Scientist and Analyst with over 10 years of experience in multidisciplinary research and consulting at an international level, working and training in 6 different countries.""")
        st.write("""I love researching and developing new knowledge. Therefore, I'm excited to continue growing professionally in the 
                technology sector, to make a positive impact on people's lives and businesses through the pursuit of solutions and decisions
                 more sustainable based on data.
        """)
        st.write("""[Github](https://github.com/Salvarez-codesal),
             [LinkedIn](https://www.linkedin.com/in/sorayaalvarezcodesal/) """)

    st.write("-------")
    frase = "#### 'The one who knows how to taste does not drink too much wine, but enjoys its gentle secrets.' ― Salvador Dalí."
    st.markdown(frase)
