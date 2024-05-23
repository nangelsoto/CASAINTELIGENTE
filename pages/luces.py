import paho.mqtt.client as paho
import time
import streamlit as st
import json
from PIL import Image as Image, ImageOps as ImagOps
values = 0.0
act1="OFF"

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
client1= paho.Client("nataliaapp")
client1.on_message = on_message



st.title("Control de Luces")
image = Image.open('luces.jpeg')
st.image(image)

st.text('Indica si quieres prender o apagar los leds')

if st.button('ON LUZ ROJA'):
    act1="ON LUZ ROJA"
    client1= paho.Client("nataliaapp")                           
    client1.on_publish = on_publish                          
    client1.connect(broker,port)  
    message =json.dumps({"Act1":act1})
    ret= client1.publish("swich", message)
 
    #client1.subscribe("Sensores")
if st.button('ON LUZ VERDE'):
    act1="ON LUZ VERDE"
    client1= paho.Client("nataliaapp")                           
    client1.on_publish = on_publish                          
    client1.connect(broker,port)  
    message =json.dumps({"Act1":act1})
    ret= client1.publish("swich", message)
 
    #client1.subscribe("Sensores")
    
    
else:
    st.write('')

if st.button('OFF LUZ ROJA'):
    act1="OFF LUZ ROJA"
    client1= paho.Client("nataliaapp")                           
    client1.on_publish = on_publish                          
    client1.connect(broker,port)  
    message =json.dumps({"Act1":act1})
    ret= client1.publish("swich", message)

if st.button('OFF LUZ VERDE'):
    act1="OFF LUZ VERDE"
    client1= paho.Client("nataliaapp")                           
    client1.on_publish = on_publish                          
    client1.connect(broker,port)  
    message =json.dumps({"Act1":act1})
    ret= client1.publish("swich", message)
  
    
else:
    st.write('')

#values = st.slider('Selecciona el rango de valores',0.0, 100.0)
st.write('Values:', values)

#if st.button('Enviar valor analógico'):
    #client1= paho.Client("nataliaapp")                           
    #client1.on_publish = on_publish                          
    #client1.connect(broker,port)   
    #message =json.dumps({"Analog": float(values)})
    #ret= client1.publish("analogo", message)
    
 
#else:
    #st.write('')
