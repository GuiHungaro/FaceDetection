#01.Importar as bibliotecas necessárias.
import streamlit as st
from PIL import Image
import opencv-python as cv2
import numpy as np

#02.Logo aplicativo.
logo = Image.open("FaceDetection.png")
st.image(logo, caption='', use_column_width=True)

#03. Foto para fazer reconhecimento facial.
st.title("Foto para fazer reconhecimento facial:")
foto_reconhecimento = st.checkbox("Fazer upload.")
if foto_reconhecimento:

  #03.a.Fazendo upload da foto desejada.
  uploaded_file = st.file_uploader("Escolha um arquivo", type=None)
  if uploaded_file is not None:
      
      #03.b.Convertendo o arquivo para uma imagem opencv.
      file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)
      imagem_original = cv2.imdecode(file_bytes, 1)
  

      #03.c.Transformando a foto em escalas de cinza.
      imagem_cinza = cv2.cvtColor(imagem_original, cv2.COLOR_BGR2GRAY)

      #03.d.Rodando o modelo.
      haar_cascade_face = cv2.CascadeClassifier('/content/haarcascade_frontalface_default.xml')
      faces = haar_cascade_face.detectMultiScale(imagem_cinza,
                                           scaleFactor=1.09,
                                           minNeighbors=5,
                                           minSize=(25,25))
      for (x,y,largura,altura) in faces:
                cv2.rectangle(imagem_original,
                (x,y),
                (x+largura, y+altura),
                (0,255,0),
                2)   

      #03.e.Exibindo a imagem
      quantidade_faces = len(faces)

      if quantidade_faces < 1:
        st.image(imagem_original, caption='Nenhuma face detectada', use_column_width=True, channels="BGR")

      elif quantidade_faces == 1:
        st.image(imagem_original, caption='Uma face detectada', use_column_width=True, channels="BGR")
      
      else:
        st.image(imagem_original, caption='{} faces detectadas'.format(quantidade_faces), use_column_width=True, channels="BGR")
