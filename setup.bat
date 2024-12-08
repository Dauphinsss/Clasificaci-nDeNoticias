@echo off
echo Instalando dependencias...
pip install -r requirements.txt
echo Instalando modelo de SpaCy...
python -m spacy download es_core_news_sm
echo Instalación completa.
pause