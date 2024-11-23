import pandas as pd
import re
import spacy

nlp = spacy.load("es_core_news_sm")
# Cargar el modelo de SpaCy en español
def cargar_modelo_spacy():
    nlp =  spacy.load("es_core_news_sm")
    return nlp

# Función para limpiar texto
def limpiar_texto_spacy(texto):
    if not isinstance(texto, str) or pd.isnull(texto):
        return ""  # Si no es una cadena, devolver vacío
    # Eliminar caracteres no deseados y convertir a minúsculas
    doc = nlp(texto.lower())
    # Filtrar palabras que no son stopwords y son alfabéticas
    tokens = [token.text for token in doc if not token.is_stop and token.is_alpha]
    return " ".join(tokens)


# Cargar los datos y preprocesarlos
def cargar_datos(archivo_csv):
    # Cargar datos del CSV
    df = pd.read_csv(archivo_csv)
    
    # Stopwords personalizadas (sin duplicados y en minúsculas)
    stopwords_personalizadas = list(set(["estar", "año", "mes", "el", "de", "en", "que", 
                                         "y", "una", "uno", "a", "del", "por", "ser", "ese", 
                                         "para", "con", "su", "al", "este", "haber", "más", 
                                         "como", "o", "no", "tener","bbva"]))
    
    # Agregar stopwords personalizadas al vocabulario de SpaCy
    for palabra in stopwords_personalizadas:
        nlp.Defaults.stop_words.add(palabra)
        lex = nlp.vocab[palabra]
        lex.is_stop = True

    # Limpiar textos en la columna 'news'
    df['news_clean'] = df['news'].apply(limpiar_texto_spacy)
    return df

