# -*- coding: utf-8 -*-
"""
Spyder Editor
This is a temporary script file.
"""
#include <stdio.h>
from time import sleep
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
# PIN-Assignment
A=17
B=18
C=21
D=22
E=4
time = 0.001


# defining the PINs
GPIO.setup(A,GPIO.OUT)
GPIO.setup(B,GPIO.OUT)
GPIO.setup(C,GPIO.OUT)
GPIO.setup(D,GPIO.OUT)
GPIO.setup(E,GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.output(A, False)
GPIO.output(B, False)
GPIO.output(C, False)
GPIO.output(D, False)
Button_State = GPIO.input(E)
# driving the motor
def Step1():
 GPIO.output(A, True)
 GPIO.output(D, True)
 sleep (time)
 GPIO.output(A, False)
 GPIO.output(D, False)
def Step2():
 GPIO.output(A, True)
 GPIO.output(B, True)
 sleep (time)
 GPIO.output(A, False)
 GPIO.output(B, False)

def Step3():
 GPIO.output(B, True)
 GPIO.output(C, True)
 sleep (time)
 GPIO.output(B, True)
 GPIO.output(C, False)
def Step4():
 GPIO.output(B, True)
 GPIO.output(C, True)
 sleep (time)
 GPIO.output(B, False)
 GPIO.output(C, False)

def Step5():

 GPIO.output(C, True)
 GPIO.output(D, True)
 sleep (time)
 GPIO.output(C, False)
 GPIO.output(D, False)

def Step6():
 GPIO.output(D, True)
 GPIO.output(A, True)
 sleep (time)
 GPIO.output(D, False)
 GPIO.output(A, False)
 
 # start one complete turn
if Button_State== True:
  for i in range (512):
   Step1()
   Step2()
   Step3()
   Step4()
   Step5()
   Step6()
  GPIO.cleanup()
else: 
  print("abdjkashbdkjashdjkas")
  GPIO.cleanup()

