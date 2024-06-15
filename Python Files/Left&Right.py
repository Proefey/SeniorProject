import serial
import keyboard
import re

#This python module reads the lines you would see on the arduino serial monitor, and presses a button should it find it.

#This is the same port that you open on the serial monitor.
#You cannot run this file and open the serial monitor at the same time
ser = serial.Serial("COM4", 9600)

print("connected to: " + ser.portstr)

#If below this threshold, throw out
threshold = 75
while True:
     cc=str(ser.readline())
     print(cc)
     match = re.search(r'\((\d+)\)', cc)
     if match:
          #Get Confidence Rating, Drop If Too Low
          if int(match.group(1)) < threshold:
               continue
          if "Found left" in cc:
               keyboard.send("left arrow")
          elif "Found right" in cc:
               keyboard.send("right arrow")