import pickle
import pandas as pd
import re
import nltk
nltk.download('stopwords')
nltk.download('punkt')
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer

# Load the pre-trained model and vectorizer
classifier = pickle.load(open('model.pkl', 'rb'))
tf = pickle.load(open('vectorizer.pkl', 'rb'))

def predict_spam_or_ham(message: str) -> int:
    """
    Predict whether a given text message is spam or ham.

    Parameters:
    message (str): The text message to be classified.

    Returns:
    int: 1 if the message is spam, 0 if it is ham.
    """
    #Cleaning the text
    message = re.sub('[^a-zA-Z]', ' ', str(message))
    if pd.isna(message):
        message = ""
    else:
        message = str(message)    
    message = message.lower()
    message = nltk.word_tokenize(message)
    ps = PorterStemmer()
    all_stopwords = stopwords.words('english')
    all_stopwords.remove('not')
    all_stopwords.remove("isn't")
    all_stopwords.remove("aren't")
    message = [ps.stem(word) for word in message if not word in set(all_stopwords)]
    message = ' '.join(message)

    # Transform the message using the vectorizer
    message_transformed = tf.transform([message])

    # Predict using the pre-trained model
    prediction = classifier.predict(message_transformed)[0]

    # The prediction is a list with a single element, get the first element
    return prediction
# Example usage
if __name__ == "__main__":
    test_message = "Where are u"
    result = predict_spam_or_ham(test_message)
    print("Spam" if result == 1 else "Ham")