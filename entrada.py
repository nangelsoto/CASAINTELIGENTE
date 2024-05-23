
import paho.mqtt.client as paho
import time
import json
import streamlit as st
import cv2
import numpy as np
#from PIL import Image
from PIL import Image as Image, ImageOps as ImagOps
from keras.models import load_model

def on_publish(client,userdata,result):             #create function for callback
    print("el dato ha sido publicado \n")
    pass

def on_message(client, userdata, message):
    global message_received
    time.sleep(2)
    message_received=str(message.payload.decode("utf-8"))
    st.write(message_received)

        


broker="broker.mqttdashboard.com"
port=1883
client1= paho.Client("Natalia")
client1.on_message = on_message
client1.on_publish = on_publish
client1.connect(broker,port)

model = load_model('keras_model.h5')
data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)

st.title("Cerradura Inteligente")
from PIL import Image

image = Image.open('casa.jpeg')
st.image(image)


img_file_buffer = st.camera_input("Indica si quieres abrir o cerrar la puerta")

if img_file_buffer is not None:
    # To read image file buffer with OpenCV:
    data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
   #To read image file buffer as a PIL Image:
    img = Image.open(img_file_buffer)

    newsize = (224, 224)
    img = img.resize(newsize)
    # To convert PIL Image to numpy array:
    img_array = np.array(img)

    # Normalize the image
    normalized_image_array = (img_array.astype(np.float32) / 127.0) - 1
    # Load the image into the array
    data[0] = normalized_image_array

    # run the inference
    prediction = model.predict(data)
    print(prediction)
    if prediction[0][0]>0.3:
      if st.header('Abriendo')
         client1.publish("nataliamensaje","{'gesto': 'Abre'}",qos=0, retain=False)
         time.sleep(0.2) #el mensaje es el de collab, igual que el cliente
         st.markdown("![Alt Text](https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExamNoYnIyYzFtMGJrZ3hieW1xbmx4OXU0NDA3dGVzM2kyeGQ3ZnVxNyZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/NVsnJH2H6NKGOr8FDJ/giphy.gif)")
    if prediction[0][1]>0.3:
      if st.header('Cerrando')
         client1.publish("nataliamensaje","{'gesto': 'Cierra'}",qos=0, retain=False)
         time.sleep(0.2)
         st.markdown("![Alt Text](https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExN2ZhNHQ2MmpkYWNoNWhtZHMxcXQyMjdxY2ExYTBhM25jYnJ5bmtqNyZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/mjzTbdoUZH8KdtFaoF/giphy.gif)")

