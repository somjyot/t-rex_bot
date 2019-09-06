from PIL import ImageGrab, ImageOps
import numpy
import pyautogui
import time
from array import array
import math


class Cordinate():
    replaybtn=(350,430)
    diano=(170,450)


def restart():          
    pyautogui.click(Cordinate.replaybtn)
    pyautogui.keyDown('down')

def jump():
    pyautogui.keyUp('down')
    pyautogui.keyDown('space')
    time.sleep(0.45)
    #print('JUMP DINO JUMP')
    pyautogui.keyUp('space')
    pyautogui.keyDown('down')    

def ImageGr():
    box=(Cordinate.diano[0]+60,Cordinate.diano[1],Cordinate.diano[0]+100,Cordinate.diano[1]+30)
    image=ImageGrab.grab(box)                 
    grayImage=ImageOps.grayscale(image)
    a=numpy.array(grayImage.getcolors()) 
    return a.sum()
   
if __name__ == "__main__":
    restart()
    x=0
    while True:
        e=ImageGr() 
        if e!=1530:
            jump()
            x=x+1
            print(x)
             
        
        
         