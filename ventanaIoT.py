"""
Created on Thu May 28 15:39:07 2020

@author: pablomartineztellez
"""

import Adafruit_DHT
import RPi.GPIO as GPIO
from time import sleep
from gpiozero import DistanceSensor


sensor = DistanceSensor(echo=21, trigger=20)

DHT_SENSOR = Adafruit_DHT.DHT22
DHT_PIN = 4

GPIO.setmode(GPIO.BCM)


GPIO.setup(23,GPIO.OUT)
GPIO.setup(24,GPIO.OUT)
GPIO.setup(25,GPIO.OUT)


while True:
     humidity, temperature = Adafruit_DHT.read_retry(DHT_SENSOR, DHT_PIN)
     distancia = sensor.distance * 100

     if temperature > 30 and distancia > 9 :
#       while distancia > 5:
 #        distancia = sensor.distance * 100
         print("Temperatura={0:0.1f}'C Humedad ={1:0.1f}%".format(temperature, humidity))
         print("Distancia",distancia)
         print("Abrir")
         GPIO.output(23,GPIO.HIGH)
         GPIO.output(24,GPIO.LOW)
         GPIO.output(25,GPIO.HIGH)
         sleep(4)
     elif temperature < 30 and distancia < 19 :
  #     while distancia < 29 :
   #      distancia = sensor.distance * 100
         print('Distance: ', distancia)
         print("Temperatura={0:0.1f}'C Humedad ={1:0.1f}%".format(temperature, humidity))
         print("Cerrar")
         GPIO.output(23,GPIO.LOW)
         GPIO.output(24,GPIO.HIGH)
         GPIO.output(25,GPIO.HIGH)
         sleep(5)
     else:
         print("Distancia ", distancia)
         print("Temperatura={0:0.1f}'C Humedad ={1:0.1f}%".format(temperature, humidity))
         GPIO.output(25,GPIO.LOW)
GPIO.cleanup()

