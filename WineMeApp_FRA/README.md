# WineMeApp
![This is an alt text.](https://github.com/ivanpgdata/WineMeApp/blob/main/WineMeApp/images/banner_img.jpg?raw=true "This is a sample image.")

🍷 https://winemeapp-fra.streamlit.app/ 🍷


## 🍇Données🍇

Nous avons extrait tous les 4800 vins espagnols disponibles sur le site web bodeboca.com en utilisant des packages comme Beautiful Soup.

## 🍇Prétraitement🍇

Nous avons nettoyé, examiné les valeurs manquantes dans l'ensemble de données. Ensuite, pour les variables/colonnes de type chaîne de caractères, nous les avons converties en minuscules, supprimé les mots vides officiels espagnols et d'autres mots vides personnalisés que nous avons créés pour chaque colonne. Nous les avons également normalisées, tokenisées et lemmatisées pour obtenir des chaînes de caractères plus propres (traitement NLP).

## 🍇EDA🍇

Nous avons examiné les données à travers une Analyse Exploratoire des Données.

# 🍷Modèle de Recommandation🍷

Une fois que les notes de dégustation et le texte d'association sont normalisés, nous les fusionnons dans une colonne : "description", qui sera utilisée comme élément de vin à évaluer.

Nous utilisons un modèle pré-entraîné (apprentissage par transfert : Google Universal Sentence Encoder version 4 (USE)), pour convertir les notes de dégustation et d'association (description) en vecteurs de 512 dimensions pour capturer le sens sémantique. USE utilise une architecture de réseau neuronal profond entraînée sur de grands corpus de texte.

Enfin, nous utilisons des similarités cosinus entre deux vecteurs représentant des vins pour calculer les valeurs de similarité entre eux. C'est ce que nous utilisons pour la recommandation, en obtenant ceux avec des valeurs les plus proches de 1 et en déterminant ainsi les vins les plus similaires en fonction de la dégustation et de l'association.

# 🍷Modèle TOPSIS🍷

Une fois que le modèle de recommandation est terminé, nous utilisons le modèle TOPSIS, une méthode de prise de décision utilisée pour évaluer la meilleure option parmi un ensemble d'alternatives en fonction de plusieurs critères, qui comporte les étapes suivantes :

Une fois que les critères à utiliser pour évaluer les alternatives ont été établis ainsi que les alternatives à comparer (en utilisant le modèle de recommandation), et après avoir normalisé les données en les mettant à l'échelle entre les valeurs 0 et 1, une matrice de décision est construite où les lignes représentent les alternatives et les colonnes représentent les critères normalisés. Avec les données normalisées, des poids sont appliqués à chaque attribut selon les valeurs fournies et un DataFrame avec des caractéristiques pondérées est créé.

Après cela, deux solutions de référence sont déterminées : la solution idéale, qui maximise chaque critère, et la solution anti-idéale, qui minimise chaque critère.

Ensuite, la distance euclidienne entre chaque alternative et les solutions idéale et anti-idéale est calculée. Cette distance mesure la proximité de chaque alternative à chacune de ces solutions de référence.

Enfin, l'indice de similarité est calculé pour chaque alternative en divisant la distance à la solution anti-idéale par la somme de la distance à la solution idéale et la distance à la solution anti-idéale. Cet indice quantifie à quel point chaque alternative est proche d'être la meilleure ou la pire solution possible.
