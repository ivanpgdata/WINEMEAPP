import streamlit as st
from streamlit_option_menu import option_menu
from funciones_sistema_recomendacion_vinos import *
import requests

# data = "WineMeApp/df_vinos_modelos.csv"
data = pd.read_csv('WineMeApp_FRA/df_vinos_modelos.csv')


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
	options = ["Accueil", "WineMeApp!", "Ressources", "À propos de nous"],
	icons = ['house-door', "menu-button-wide-fill","journals", "person lines fill"],
	menu_icon = "",
	orientation = "horizontal",
	styles={
    "container": {"padding": "0!important", "background-color": "#FFFFFF"},
    "icon": {"color": "black", "font-size": "30px"},
    "nav-link": {"font-size": "20px", "text-align": "left","font-family": 'Cooper Black',"color": "black", "margin":"0px", "--hover-color": "#0000"},
    "nav-link-selected": {"background-color": "#e51133"},
})
if selected =="Accueil":
    st.markdown(""" <style> .font {
            font-size:35px ; font-family: 'Cooper Black'; color: #FFFFF;} 
            </style> """, unsafe_allow_html=True)
    st.markdown('<p class="font">Introduction</p>', unsafe_allow_html=True)
    col1, col2, col3= st.columns([0.5, 0.3, 0.2])
    with col1:  # To display the header text using css style
        st.write("Nous vous présentons un moteur de recommandation de vins qui va au-delà du conventionnel !")
        st.write(
            "Oubliez les suggestions basées uniquement sur le type de vin. Notre système innovant analyse vos préférences et besoins,"
            " en utilisant des notes de dégustation détaillées et des accords mets-vins pour trouver l'option parfaite pour chaque occasion.")
        st.markdown(""" <style> .font {
                    font-size:35px ; font-family: 'Cooper Black'; color: #FFFFF;} 
                    </style> """, unsafe_allow_html=True)
        st.markdown("<p class=""font"">¿Qu'est-ce qui nous rend différents ?</p>", unsafe_allow_html=True)
        st.markdown("* **Recommandations personnalisées :** Ajustez l'importance du prix et de la note pour trouver des vins qui correspondent à votre budget et à vos goûts.")
        st.markdown("* **Au-delà des stéréotypes :** Nous ne vous limitons pas à un seul type de vin. Découvrez de nouveaux favoris, des rouges légers aux blancs frais ou pétillants.")
        st.markdown("* **Données sélectionnées par des experts :** Nos recommandations sont basées sur des notes de dégustation et des accords mets-vins approfondis, ce qui vous garantit de trouver des vins que vous apprécierez vraiment.")
        st.markdown("* **Dites adieu aux expériences de vin moyennes :** Laissez notre moteur vous guider vers de nouvelles découvertes et des moments inoubliables.")
        st.markdown("#####  Voulez-vous en savoir plus ?")
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
    st.markdown('<p class="font">Motivation</p>', unsafe_allow_html=True)
    st.write(
        "Beaucoup d'entre nous se sont retrouvés dans la situation inconfortable de ne pas savoir quel vin commander dans un restaurant ou lors de l'achat "
        "dans une boutique spécialisée. Souvent, nous finissons par opter pour la même chose ou pour ce que quelqu'un d'autre commande, sans explorer la large gamme d'options disponibles.")
    st.write(
        "C'est dans ces moments-là qu'un système de recommandation de vins, que ce soit dans la section vins des grands magasins ou des supermarchés gastronomiques, ou lorsque vous commandez"
        " des boissons dans un restaurant, serait très utile. Et c'est précisément là que notre recommandateur <span style='color: #E51133; font-weight: bold;'>WineMeApp!</span> entre en jeu !",
        unsafe_allow_html=True)

    st.write(
        "En tant que membres de l'équipe, lors de notre expérience en tant qu'expatriés au Royaume-Uni, nous avons remarqué que les vins blancs de Chardonnay étaient une option particulièrement courante. Bien que cette variété soit populaire, "
        "nous avons été surpris que les diverses options offertes par le monde du vin ne soient pas explorées, y compris les vins espagnols des régions comme Jerez de la Frontera (Palomino, Pedro Ximénez, Tintilla de Rota) ou Zamora"
        " (Malvasía Castellana, Moscatel de Grano Menudo, Verdejo).")
    st.write(
        "C'est pourquoi nous avons développé <span style='color: #E51133; font-weight: bold;'>WineMeApp!</span>, un moteur de recommandation qui vous aide à choisir le vin parfait pour chaque occasion. En tenant compte de vos préférences,"
        " du type de repas et de l'occasion, <span style='color: #E51133; font-weight: bold;'>WineMeApp!</span> vous offre"
        " des recommandations personnalisées pour que vous puissiez découvrir de nouveaux vins et profiter pleinement de chaque expérience.",
        unsafe_allow_html=True)

    st.markdown(""" <style> .font {
            font-size:35px ; font-family: 'Cooper Black'; color: #FFFFF;} 
            </style> """, unsafe_allow_html=True)
    st.markdown('<p class="font">Objectif</p>', unsafe_allow_html=True)
    st.write(
        "Le projet utilise un modèle hybride d'apprentissage automatique pour recommander des vins en fonction des préférences de l'utilisateur concernant les notes de dégustation et les accords mets-vins. L'utilisateur saisit le "
        "nom du vin, vérifie sa disponibilité dans la base de données, puis définit une fourchette de prix et l'importance du prix et de la note du vin pour obtenir des recommandations personnalisées.")

# -----------------------------------------------------------------------------

if selected =="WineMeApp!":
    st.markdown("# Modèle de recommandation")
    st.write("Le modèle de recommandation créé dans ce projet est un modèle "
             "hybride qui combine deux approches puissantes")
    st.markdown("## :wine_glass: Modèle 1: Recommandateur basé sur la dégustation et l'accord mets-vins")
    st.write("Nous avons d'abord mis en place un système de recommandation basé sur les notes de dégustation"
             " et l'accord mets-vins à l'aide du Traitement du Langage Naturel (NLP).")
    st.write(
        "Lors de la saisie d'un vin pour rechercher des recommandations similaires, le système recherche des vins avec"
        " une plus grande similarité sémantique, en appliquant la similarité cosinus, dans les notes de dégustation et l'accord mets-vins,"
        " fournissant un classement des 10 vins les plus similaires.")
    # ---- BUSQUEDA EN LA LISTA DE 4K VINOS ----
    st.markdown("#### Étape 1: Vérifiez si votre vin préféré est dans notre base de données")
    texto_busqueda = st.text_input(' ')
    if st.button("Trouvez votre vin 🔎 "):  # Si se pulsa el botón
        st.markdown(" ##### Résultats trouvés dans notre base de données : ")
        st.dataframe(buscar_vino(data, texto_busqueda, embeddings2))

    # ----- RECOMENDATOR ----
    st.markdown("#### Étape 2: Entrez le nom du vin pour lequel vous souhaitez rechercher une recommandation")
    nombre_vino = st.text_input("")
    if st.button("Recommandateur 🍀 "):  # Si se pulsa el botón
        st.markdown(f" ##### Voici les vins que nous vous recommandons pour *{nombre_vino}* ")
    recomendaciones = recomendar_vino(data, nombre_vino, embeddings2)
    st.dataframe(recomendaciones)

    # ---- TOPSIS ----
    st.markdown("##  :wine_glass::wine_glass: Modèle 2: TOPSIS")
    st.write("La versión actual de WineMeApp! tiene definidos por defecto un filtrado de los vinos con"
             " precios comprendidos entre 5 y 150 euros  y de los pesos otorgados a las variables precio (80%) y rating (20%)  ")
    st.markdown("##### Étape 3: Vérifiez votre recommandation avec le modèle TOPSIS*")

    vinos = filtrar_por_precio(recomendaciones, precio_min, precio_max)

    if st.button("Topsis :tada:"):  # Si se pulsa el botón
        st.write(topsis_general(recomendaciones, nombre_vino))
    # ------



# -----------------------------------------------------------------------------
if selected =="Ressources":
    col1, col2, col3, col4, col5 = st.columns([0.20, 0.20, 0.20, 0.20, 0.20])
    with col1:
        st.markdown("##  Sites Web ")
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
        st.markdown("##  Librairies  ")
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
if selected == "À propos de nous":
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
            Actuellement, je suis en train de changer de cap dans ma carrière professionnelle en me formant en tant que Data Scientist.
            """)

            st.write("""
            Auparavant, j'ai consacré près de 10 ans au développement intégral de projets architecturaux. Je me considère comme une personne responsable,
             engagée et ayant une grande capacité de travail. J'aime travailler en équipe, apporter des idées personnelles et apprendre de la manière de travailler des autres membres de manière positive.
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
        st.write("""Curieux de nature, novice en données et esprit inquiet.""")
        st.write(
            """J'ai décidé de réorienter ma carrière vers la science des données grâce à un Bootcamp en Data Science et Machine Learning. Avec une expérience internationale dans des postes de responsabilité où j'ai pu constater l'importance des données.""")
        st.write("""Toujours avec un projet en tête.""")
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
        Scientifique et analyste de données avec plus de 10 ans d'expérience en recherche et en
        consulting multidisciplinaire à l'échelle internationale, travaillant et se formant dans 6 pays différents.""")
        st.write("""J'adore faire de la recherche et développer de nouvelles connaissances. C'est pourquoi je suis enthousiaste à l'idée de continuer à progresser professionnellement dans le
        secteur technologique, pour avoir un impact positif sur la vie des gens et des entreprises grâce à la recherche de solutions et de décisions
        plus durables basées sur les données.""")

        st.write("""[Github](https://github.com/Salvarez-codesal),
             [LinkedIn](https://www.linkedin.com/in/sorayaalvarezcodesal/) """)

    st.write("-------")
    frase = "#### 'Celui qui sait déguster ne boit pas trop de vin, mais savoure ses doux secrets.' ― Salvador Dalí."
    st.markdown(frase)
