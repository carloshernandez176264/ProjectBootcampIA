#importar biblioteca nltk
import nltk

#descargar stopwords
nltk.download('stopwords')

#importar stopwords
from nltk.corpus import stopwords

#imprimir stopwords
print(stopwords.words('english'))