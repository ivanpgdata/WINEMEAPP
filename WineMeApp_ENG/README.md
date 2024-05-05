# Winemeapp! Wine Recommender

🍷 https://winemeapp-eng.streamlit.app/ 🍷

## 🍇Data🍇
We have extracted all 4800 Spanish wines available on the website bodeboca.com using packages like Beautiful Soup.

## 🍇Preprocessing🍇

We have cleaned, reviewed NAs in the dataset. Then, for string type variables/columns, we converted them to lowercase, removed official Spanish stop words, and other customized stop words we created for each column. We also normalized, tokenized, and lemmatized them to have cleaner strings (NLP processing).

## 🍇EDA🍇
We have reviewed the data through Exploratory Data Analysis.

# 🍷Recommendation Model🍷
Once the tasting notes and pairing text are normalized, we merge them into a column: "description", which will be used as the wine element to evaluate.

We use a pre-trained model (transfer learning: Google Universal Sentence Encoder version 4 (USE)), to convert the tasting and pairing notes (description) into 512-dimensional vectors to capture the semantic meaning. USE utilizes a deep neural network architecture trained on large text corpora.

Finally, we use cosine similarities between two vectors representing wines to calculate similarity values between them. This is what we use for recommendation, obtaining those with values closest to 1 and thus determining the most similar wines based on tasting and pairing.

# 🍷TOPSIS Model🍷

Once the recommendation model is done, we use the TOPSIS model, a decision-making method used to evaluate the best option among a set of alternatives based on multiple criteria, which has the following steps:

Once the criteria to be used to evaluate the alternatives have been established along with which alternatives will be compared (using the recommendation model), and after normalizing the data by scaling them between values ​​0 and 1, a decision matrix is ​​constructed where the rows represent the alternatives and the columns represent the normalized criteria. With the normalized data, weights are applied to each attribute according to the provided values and a DataFrame with weighted characteristics is created.

After that, two reference solutions are determined: the ideal solution, which maximizes each criterion, and the anti-ideal solution, which minimizes each criterion.

Subsequently, the Euclidean distance between each alternative and the ideal and anti-ideal solutions is calculated. This distance measures the proximity of each alternative to each of these reference solutions.

Finally, the similarity index is calculated for each alternative by dividing the distance to the anti-ideal solution by the sum of the distance to the ideal solution and the distance to the anti-ideal solution. This index quantifies how close each alternative is to being the best or worst possible solution.
