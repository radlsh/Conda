import nltk
import re
import numpy as np
import tensorflow as tf

from nltk.corpus import stopwords
from gensim.models import Word2Vec
    
Word2Vec_model = Word2Vec.load(r"C:\TTTT\nlp\models\Word2Vec.model")

def process_text(sentence):
    russian_stopwords = stopwords.words("russian")
    lemmatize = nltk.WordNetLemmatizer()
    #удаляем неалфавитные символы
    text = re.sub("[^а-яА-Яa-zA-Z]"," ", sentence.lower()) 
    # токенизируем слова
    text = nltk.word_tokenize(text, language = "russian")
    # лемматирзируем слова
    text = [lemmatize.lemmatize(word) for word in text if not word in set(russian_stopwords)]
    words_vecs = [Word2Vec_model.wv[word] for word in text if word in Word2Vec_model.wv]
    if len(words_vecs) == 0:
        return np.zeros(600)
    words_vecs = np.array(words_vecs)



    model = tf.keras.models.load_model(r"C:\TTTT\nlp\models\10ep_3.keras")

    # Example sequences
    sequences = words_vecs  
    # Pad sequences
    padded_sequences = tf.keras.preprocessing.sequence.pad_sequences(sequences, padding='post', dtype='float32')
    # Predict
    prediction = model.predict(padded_sequences)
    
    return str(f'ЗП: {round(prediction[0][0][0])} \n')
