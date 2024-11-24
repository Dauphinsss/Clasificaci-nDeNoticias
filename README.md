# Proyecto de Programación - Inteligencia Artificial
Implementación del Aprendizaje No Supervisado - Clasificación

# Problemática
Se abordará la problemática del agrupamiento automático de contenidos textuales, centrándose en el desarrollo de soluciones que permitan clasificar y organizar textos de manera eficiente y precisa.

# Ejecución del Proyecto
Para el correcto funcionamiento del proyecto debe correr el mismo en su computadora, para ello necesita de:

1. Instalar Python desde [python.org](https://www.python.org/).
2. Instalar [Visual Studio Code](https://code.visualstudio.com/). (Preferencialmente o ejecutar el programa en un shell)
3. Ejecutar los siguientes comandos en su terminal de preferencia (Nosotros usamos powershell, pero puede emplearse la terminal integrada de VSCode)

# Instalación de Librerías Automatizadas

   ## Si usas Windows
   ## Ejecutar el archivo setup.bat haciendo doble click sobre el o ejecutando en el shell el comando:
         setup.bat

   ## Si usas Linux
   ## Haz el archivo ejecutable con:
         chmod +x setup.sh
   ## Luego ejecutalo
         ./setup.sh

# Instalación de Librerías Manualmente

   ## Instale las dependencias
      pip install scikit-learn pandas matplotlib matplotlib numpy spacy
      python -m spacy download es_core_news_sm

   ## Si utilizas Linux debes utilizar este comando extra para usar tkinter
      sudo apt-get install python3-tk (Ubuntu/Debian)
      sudo dnf install python3-tkinter (Fedora)
  
# Finalmente ejecute el main.py y vea el proyecto
      python .\ClasificacionDeNoticias\main.py
