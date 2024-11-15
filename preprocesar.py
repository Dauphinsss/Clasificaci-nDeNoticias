import pandas as pd
import re
import spacy

# Cargar el modelo de SpaCy en español
def cargar_modelo_spacy():
    return spacy.load("es_core_news_sm")

# Cargar los datos y preprocesarlos
def cargar_datos(archivo_csv):
    df = pd.read_csv(archivo_csv)
    stopwords_personalizadas = ["él"]
    
    nlp = cargar_modelo_spacy()
    for palabra in stopwords_personalizadas:
        nlp.vocab[palabra].is_stop = True

    def limpiar_texto_spacy(texto):
        texto = re.sub(r'[^a-zA-ZáéíóúüñÁÉÍÓÚÜÑ\s]', '', texto)
        texto = texto.lower()
        doc = nlp(texto)
        palabras_limpias = [token.lemma_ for token in doc if not token.is_stop and token.is_alpha]
        return ' '.join(palabras_limpias)

    df['news_clean'] = df['news'].apply(limpiar_texto_spacy)
    return df
