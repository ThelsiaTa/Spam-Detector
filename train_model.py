import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import pickle
import re
import nltk

dataset = pd.read_csv('spam.csv', encoding='latin-1')[['v1', 'v2']]
dataset = dataset.drop_duplicates(keep='first')

#Tokenize the dataset
nltk.download('punkt')
dataset['num_characters'] = dataset['v2'].apply(len)
dataset['num_words'] = dataset['v2'].apply(lambda x:len(nltk.word_tokenize(x)))
dataset['num_sentences'] = dataset['v2'].apply(lambda x:len(nltk.sent_tokenize(x)))
dataset.head()

#Cleaning the texts
nltk.download('stopwords')
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
corpus = []
all_stopwords = stopwords.words('english')
all_stopwords.remove('not')
all_stopwords.remove("isn't")
all_stopwords.remove("aren't")
for i in range(0, 5169):
  message = re.sub('[^a-zA-Z]', ' ', str(dataset['v2'].iloc[i]))
  if pd.isna(message):
        message = ""
  else:
        message = str(message)    
  message = message.lower()
  message = nltk.word_tokenize(message)
  ps = PorterStemmer()
  message = [ps.stem(word) for word in message if not word in set(all_stopwords)]
  message = ' '.join(message)
  corpus.append(message)

#Creating Bag of Words model
from sklearn.feature_extraction.text import TfidfVectorizer
tf = TfidfVectorizer()
X = tf.fit_transform(corpus).toarray()
y = dataset.iloc[:,0].values

#Encoding the dependent variable
from sklearn.preprocessing import LabelEncoder
le = LabelEncoder()
y=le.fit_transform(y)

#Splitting the dataset into training set and test set
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.20, random_state = 0)

#Dealing with imbalanced dataset
from imblearn.over_sampling import SMOTE
smote = SMOTE(random_state=42)
X_resampled, y_resampled = smote.fit_resample(X_train, y_train)


#Training on Naive Bayes
from sklearn.naive_bayes import MultinomialNB
classifier = MultinomialNB()
classifier.fit(X_resampled, y_resampled)

#Save the model and vectorizer to disk
pickle.dump(tf, open('vectorizer.pkl', 'wb'))
pickle.dump(classifier, open('model.pkl', 'wb'))